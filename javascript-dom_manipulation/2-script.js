const redButton = document.querySelector('#red_header');
redButton.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.classList.add('red');
});
