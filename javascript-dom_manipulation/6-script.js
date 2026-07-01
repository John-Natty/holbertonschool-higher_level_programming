// Select the element with the id character.
const character = document.querySelector('#character');

// Fetch the Star Wars character data from the API.
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    // Convert the response to JSON.
    return response.json();
  })
  .then(function (data) {
    // Display the character name inside the character element.
    character.textContent = data.name;
  });
  