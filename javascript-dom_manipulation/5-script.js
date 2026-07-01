// Select the header element from the HTML document.
const header = document.querySelector('header');

// Select the element with the id update_header.
const updateHeader = document.querySelector('#update_header');

// Listen for a click on the updateHeader element.
updateHeader.addEventListener('click', function () {
  // Update the text content of the header.
  header.textContent = 'New Header!!!';
});
