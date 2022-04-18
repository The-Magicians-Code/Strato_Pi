$(function() {

  $(".progress").each(function() {
    var value = $(this).attr('data-value');

    var left = $(this).find('.progress-left .progress-bar');
    var right = $(this).find('.progress-right .progress-bar');

    if (value > 0) {
      if (value <= 0.5) {
        right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
      } else {
        right.css('transform', 'rotate(180deg)')
        left.css('transform', 'rotate(' + percentageToDegrees(value - 0.5) + 'deg)')
      }
    }
  })

  function percentageToDegrees(percentage) {

    return percentage * 360

  }

});