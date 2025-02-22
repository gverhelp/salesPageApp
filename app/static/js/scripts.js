////////////////////////////
/////////// Modal //////////
////////////////////////////
(function handleModal() {
    const interestModalElement = document.getElementById('interestModal');
    const toastTrigger = document.getElementById('toastSuccessBtn');
    const toastLive = document.getElementById('toastSuccess');
    const mailInput = document.getElementById('mailInput');
    const phoneInput = document.getElementById('phoneInput');
    const interestForm = document.getElementById('interestForm');

    if (!interestModalElement || !toastTrigger || !mailInput || !phoneInput || !interestForm) return;

    const modal = new bootstrap.Modal(interestModalElement);

    [mailInput, phoneInput].forEach((input) => {
        input.addEventListener("input", () => {
            if (mailInput.checkValidity() || phoneInput.checkValidity()) {
                mailInput.classList.remove("is-invalid");
                phoneInput.classList.remove("is-invalid");
            }
        });
    });

    toastTrigger.addEventListener("click", function (event) {
        event.preventDefault();

        const mailValid = mailInput.checkValidity();
        const phoneValid = phoneInput.checkValidity();

        if (!mailValid && !phoneValid) {
            mailInput.classList.add("is-invalid");
            phoneInput.classList.add("is-invalid");
        } else {
            mailInput.classList.remove("is-invalid");
            phoneInput.classList.remove("is-invalid");

            const formData = new FormData(interestForm);

            fetch(interestForm.action, {
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (response.ok) {
                    modal.hide();

                if (toastLive) {
                    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLive);
                    toastBootstrap.show();
                }

                interestForm.reset();
                } else {
                    console.error("Erreur lors de l'envoi du formulaire");
                }
            })
            .catch(error => console.error("Erreur:", error));
        }
    });
})();

  
////////////////////////////
////// Theme switcher //////
////////////////////////////
(() => {
    'use strict';
  
    const themeSwitcher = document.querySelector('#themingSwitcher');
  
    const getStoredTheme = () => localStorage.getItem('theme');
    const setStoredTheme = theme => localStorage.setItem('theme', theme);
  
    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme();
        return storedTheme || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    };
  
    const setTheme = theme => {
        if (theme === 'auto') {
            document.documentElement.setAttribute(
            'data-bs-theme',
            window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
            );
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme);
        }
    };
  
    const updateSwitcherState = theme => {
        if (theme === 'dark') {
            themeSwitcher.checked = true;
        } else {
            themeSwitcher.checked = false;
        }
    };
  
    // Initialisation : applique le thème préféré
    const preferredTheme = getPreferredTheme();
    setTheme(preferredTheme);
    updateSwitcherState(preferredTheme);
  
    // Ajout d'un écouteur sur le switch
    themeSwitcher.addEventListener('change', () => {
        const newTheme = themeSwitcher.checked ? 'dark' : 'light';
        setStoredTheme(newTheme);
        setTheme(newTheme);
    });
  
    // Écoute les changements de préférence système
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        const storedTheme = getStoredTheme();
        if (storedTheme !== 'light' && storedTheme !== 'dark') {
            setTheme(getPreferredTheme());
        }
    });
})();
  