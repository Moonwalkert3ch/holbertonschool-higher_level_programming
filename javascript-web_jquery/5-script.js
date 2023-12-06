// Add a click event listener to the #add_item div
$('#add_item').click(function() {
    // Create a new <li> element with the text "Item"
    const createElement = $('<li>').text('Item');
    
    // Append the new <li> element to the ul
    $('ul.my_list').append(createElement);
  });
  