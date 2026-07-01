// Wait until the HTML document is fully loaded.
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id hello.
  const helloElement = document.querySelector('#hello');

  // Fetch the French translation of "hello" from the API.
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      // Convert the response to JSON.
      return response.json();
    })
    .then(function (data) {
      // Display the translation inside the hello element.
      helloElement.textContent = data.hello;
    });
});
