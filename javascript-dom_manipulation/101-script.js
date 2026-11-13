document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.querySelector('#btn_translate');
  btnTranslate.addEventListener('click', function () {
    const langCode = document.querySelector('#language_code').value;
    if (langCode) {
      fetch(`https://hellosalut.stefanbohacek.com/?lang=${langCode}`)
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          const helloDiv = document.querySelector('#hello');
          helloDiv.textContent = data.hello;
        });
    }
  });
});
