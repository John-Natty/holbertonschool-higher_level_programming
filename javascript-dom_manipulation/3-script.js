// Select the header element from the HTML document.
const header = document.querySelector('header');

// Select the element with the id toggle_header.
const toggleHeader = document.querySelector('#toggle_header');

// Listen for a click on the toggleHeader element.
toggleHeader.addEventListener('click', function () {
  // Toggle the red class on the header element.
  header.classList.toggle('red');

  // Toggle the green class on the header element.
  header.classList.toggle('green');
});
