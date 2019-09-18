window.onload = function()
{
  //Set the images to grayscale 100 on load
  document.getElementById("pBagImage").style.filter = "grayscale(100%)";
  document.getElementById("DiaperImage").style.filter = "grayscale(100%)";
  document.getElementById("CoffeeImage").style.filter = "grayscale(100%)";
  document.getElementById("MilkImage").style.filter = "grayscale(100%)";

  document.getElementById("earth-base").style.opacity = "0.0";

  // Get the values of the sliders and the text elements
  var pbag_slider = document.getElementById("pBags"); // Plastic Bag slider
  var pbagval_output = document.getElementById("pBagsValue"); // Plastic bag value
  var diaper_slider = document.getElementById("Diapers"); // Diapers slider
  var diaper_output = document.getElementById("DiapersValue"); // Diapers value
  var coffee_slider = document.getElementById("Coffee"); // Coffee slider
  var coffee_output = document.getElementById("CoffeeValue"); // Coffee value
  var milk_slider = document.getElementById("Milk"); //  Milk slider
  var milk_output = document.getElementById("MilkValue"); // Milk value

  //Get the values of the impact scales
  var co2_scale = document.getElementById("CO2Value");

  // Define the functions to change the value and the grayscale percentage
  pbag_slider.oninput = function()
  {
    // Update the value below the slider
    pbagval_output.innerHTML = this.value;
    console.log("hello")
    //Set grayscale value
    var grey = (((15 - this.value)/15)*100).toString();
    document.getElementById("pBagImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    //Make the smoke more opaque as the value increases
    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc;
  }


  diaper_slider.oninput = function()
  {
    diaper_output.innerHTML = this.value;
    var grey = (((70 - this.value)/70)*100).toString();
    document.getElementById("DiaperImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc.toString();
  }
  coffee_slider.oninput = function()
  {
    coffee_output.innerHTML = this.value;
    var grey = (((20 - this.value)/20)*100).toString();
    document.getElementById("CoffeeImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc;

  }
  milk_slider.oninput = function()
  {
    milk_output.innerHTML = this.value;
    var grey = (((5 - this.value)/5)*100).toString();
    document.getElementById("MilkImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc;
  }
}
