const updateButton = document.querySelector('#update_header');
updateButton.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});
