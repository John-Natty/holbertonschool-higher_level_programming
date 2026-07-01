// Select the element with the id add_item.
const addItem = document.querySelector('#add_item');

// Select the list with the class my_list.
const myList = document.querySelector('.my_list');

// Listen for a click on the addItem element.
addItem.addEventListener('click', function () {
  // Create a new li element.
  const newItem = document.createElement('li');

  // Add the text Item inside the new li element.
  newItem.textContent = 'Item';

  // Add the new li element at the end of the list.
  myList.appendChild(newItem);
});
