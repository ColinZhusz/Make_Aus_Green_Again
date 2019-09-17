window.onload = function(){
var slider = document.getElementById("pBags");
var output = document.getElementById("pBagsValue");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}
}
