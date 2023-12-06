// Make an AJAX request to fetch translation
$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function(translation) {
        // Update with the translation
        $('#hello').text(translation.hello);
    },
});
