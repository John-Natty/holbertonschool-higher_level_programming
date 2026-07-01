// Select the header element from the HTML document.
const header = document.querySelector('header');

// Select the element with the id red_header.
const redHeader = document.querySelector('#red_header');

// Listen for a click on the redHeader element.
redHeader.addEventListener('click', function () {
  // Add the red class to the header element.
  header.classList.add('red');
});
