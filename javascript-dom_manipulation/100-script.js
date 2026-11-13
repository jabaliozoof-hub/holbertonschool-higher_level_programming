document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });

  removeItem.addEventListener('click', function () {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  clearList.addEventListener('click', function () {
    while (myList.firstChild) {
      myList.removeChild(myList.firstChild);
    }
  });
});
