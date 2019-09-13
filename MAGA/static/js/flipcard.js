document.querySelector(".flip-card").classList.toggle("flip-card-inner");
$('.flip-card').bind({
  click: function() {
    $('.flip-card .flip-card-inner').toggleClass('flip-hover');
  },
  mouseenter: function() {
    $('.flip-card .flip-card-inner').addClass('flip-hover');
  },
  mouseleave: function() {
    $('.flip-card .flip-card-inner').removeClass('flip-hover');
  }
});