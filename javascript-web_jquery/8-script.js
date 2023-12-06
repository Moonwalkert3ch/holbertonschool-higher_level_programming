// Make an AJAX request to fetch movie content
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (content) {
    // traverse through movie titles
    content.results.forEach(function (movie) {
      // append titles to #list_movies
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
