// Select the list element with the id list_movies.
const listMovies = document.querySelector('#list_movies');

// Fetch the Star Wars movies data from the API.
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    // Convert the response to JSON.
    return response.json();
  })
  .then(function (data) {
    // Loop through all movies in the results array.
    data.results.forEach(function (movie) {
      // Create a new li element for each movie.
      const movieItem = document.createElement('li');

      // Add the movie title inside the li element.
      movieItem.textContent = movie.title;

      // Add the li element to the movies list.
      listMovies.appendChild(movieItem);
    });
  });
