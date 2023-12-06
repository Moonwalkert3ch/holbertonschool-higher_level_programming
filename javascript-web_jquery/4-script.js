// Add a click event listener to the #toggle_header div
$('#toggle_header').click(function () {
  // Toggle the 'red' and 'green' classes on the <header>
  $('header').toggleClass('red green');
});
