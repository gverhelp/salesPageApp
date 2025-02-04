const toastTrigger = document.getElementById('toastSuccessBtn')
const toastLive = document.getElementById('toastSuccess')
const mailInput = document.getElementById('mailInput')
const phoneInput = document.getElementById('phoneInput')
const FormControlTextarea = document.getElementById('FormControlTextarea');
const modal = new bootstrap.Modal(document.getElementById('interestModal'));


[mailInput, phoneInput].forEach((input) => {
    input.addEventListener("input", () => {
        if (mailInput.checkValidity() || phoneInput.checkValidity()) {
            mailInput.classList.remove("is-invalid");
            phoneInput.classList.remove("is-invalid");
        }
    });
});

toastTrigger.addEventListener("click", function (event) {
    let mailValid = mailInput.checkValidity();
    let phoneValid = phoneInput.checkValidity();

    if (!mailValid && !phoneValid) {
        event.preventDefault();
        event.stopPropagation();

        mailInput.classList.add("is-invalid");
        phoneInput.classList.add("is-invalid");
    } else {
        mailInput.classList.remove("is-invalid");
        phoneInput.classList.remove("is-invalid");

        modal.hide();
        if (toastLive) {
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLive);
            toastBootstrap.show();
            mailInput.value = '';
            phoneInput.value = '';
            FormControlTextarea.value = '';
        }
    }
});