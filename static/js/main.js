// The following function gets the current year appends it to the
//  copyright message. The message is appended to the footer.

$(document).on('click', '#signOutLink', function() {
  $('#signOutBtn').click()
});

$(document).ready(function(){
    current_year = new Date().getFullYear()
    $('#copyright-text').html(`&copy; Valencia Tennis Club ${current_year}`);
  })
  
  // The following function initialises all Materialize JS components.
  $(document).ready(function(){
    $('.sidenav').sidenav();
  });