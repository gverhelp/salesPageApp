const toastTrigger = document.getElementById('toastSuccessBtn')
const toastLiveExample = document.getElementById('toastSuccess')

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
  toastTrigger.addEventListener('click', () => {
    toastBootstrap.show()
  })
}