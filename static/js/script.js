$(document).ready(function() {
  // Add event listener to navigation menu
  $(".navbar-nav a").on("click", function(event) {
    event.preventDefault();
    var href = $(this).attr("href");
    $.ajax({
      type: "GET",
      url: href,
      success: function(data) {
        $("#content").html(data);
      }
    });
  });
});
