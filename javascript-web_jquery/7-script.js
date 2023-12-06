// Make an AJAX request to fetch character information
$.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function(content) {
        // Update content with character name
        $('#character').text(content.name);
    },
});
