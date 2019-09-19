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
  var tree_scale = document.getElementById("TreeValue");

  // Define the functions to change the value and the grayscale percentage
  pbag_slider.oninput = function()
  {
    document.getElementById("impacts_container").style.opacity = 1;
    document.getElementById("impacts_container").style.transition = "opacity 1.5s";
    // Update the value below the slider
    pbagval_output.innerHTML = this.value;

    //Set grayscale value
    var grey = (((15 - this.value)/15)*100).toString();
    document.getElementById("pBagImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    //Set the tree scale values
    var trees = 0.0016*parseInt(pbag_slider.value)*52 +
              0.0057*parseInt(diaper_slider.value)*52 +
              0.0014*parseInt(coffee_slider.value)*52 +
              0.0021*parseInt(milk_slider.value)*52;
    tree_scale.innerHTML = (trees).toFixed(2);

    // Set grayscale for the tree image according to the value
    var gray_trees = (trees/20)*100;
    document.getElementById("TreeImage").style.filter = "grayscale("+gray_trees+"%)";

    // calculate impact alternatives
    document.getElementById("TreeCO2Val").innerHTML = (co2/6000).toFixed(2);
    document.getElementById("CarCO2Val").innerHTML = (co2/170).toFixed(2);
    document.getElementById("TreeOxyVal").innerHTML = (trees/2).toFixed(2);
    document.getElementById("TreeVal").innerHTML = (300/trees).toFixed(2);

    // compare with the national average
    if ((co2/1000) > 22 ){
      document.getElementById("CO2result").innerHTML = "You exceed the national average of 22Kg per year for these items";
      document.getElementById("CO2result").style.color = "red";
    }
    else {
      document.getElementById("CO2result").style.color = "green";
      document.getElementById("CO2result").innerHTML = "You are under the national average of 22Kg per year for these items";
    }

    //Make the smoke more opaque as the value increases
    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc;
  }


  diaper_slider.oninput = function()
  {
    document.getElementById("impacts_container").style.opacity = 1;
    document.getElementById("impacts_container").style.transition = "opacity 1.5s";

    diaper_output.innerHTML = this.value;
    var grey = (((70 - this.value)/70)*100).toString();
    document.getElementById("DiaperImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    //Set the tree scale values
    var trees = 0.0016*parseInt(pbag_slider.value)*52 +
              0.0057*parseInt(diaper_slider.value)*52 +
              0.0014*parseInt(coffee_slider.value)*52 +
              0.0021*parseInt(milk_slider.value)*52;
    tree_scale.innerHTML = (trees).toFixed(2);

    // calculate impact alternatives
    document.getElementById("TreeCO2Val").innerHTML = (co2/6000).toFixed(2);
    document.getElementById("CarCO2Val").innerHTML = (co2/170).toFixed(2);
    document.getElementById("TreeOxyVal").innerHTML = (trees/2).toFixed(2);
    document.getElementById("TreeVal").innerHTML = (300/trees).toFixed(2);

    // Set grayscale for the tree image according to the value
    var gray_trees = (trees/20)*100;
    console.log(trees)
    console.log(gray_trees);
    document.getElementById("TreeImage").style.filter = "grayscale("+gray_trees+"%)";
    document.getElementById("TreeOxyVal").innerHTML = (trees/2).toFixed(2);

    // compare with the national average
    if ((co2/1000) > 22 ){
      document.getElementById("CO2result").innerHTML = "You exceed the national average of 22Kg per year for these items";
      document.getElementById("CO2result").style.color = "red";
    }
    else {
      document.getElementById("CO2result").style.color = "green";
      document.getElementById("CO2result").innerHTML = "You are under the national average of 22Kg per year for these items";
    }

    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc.toString();
  }
  coffee_slider.oninput = function()
  {
    document.getElementById("impacts_container").style.opacity = 1;
    document.getElementById("impacts_container").style.transition = "opacity 1.5s";

    coffee_output.innerHTML = this.value;
    var grey = (((20 - this.value)/20)*100).toString();
    document.getElementById("CoffeeImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    //Set the tree scale values
    var trees = 0.0016*parseInt(pbag_slider.value)*52 +
              0.0057*parseInt(diaper_slider.value)*52 +
              0.0014*parseInt(coffee_slider.value)*52 +
              0.0021*parseInt(milk_slider.value)*52;
    tree_scale.innerHTML = (trees).toFixed(2);

    // calculate impact alternatives
    document.getElementById("TreeCO2Val").innerHTML = (co2/6000).toFixed(2);
    document.getElementById("CarCO2Val").innerHTML = (co2/170).toFixed(2);
    document.getElementById("TreeOxyVal").innerHTML = (trees/2).toFixed(2);
    document.getElementById("TreeVal").innerHTML = (300/trees).toFixed(2);

    // Set grayscale for the tree image according to the value
    var gray_trees = (trees/20)*100;
    console.log(trees)
    console.log(gray_trees);
    document.getElementById("TreeImage").style.filter = "grayscale("+gray_trees+"%)";
    document.getElementById("TreeOxyVal").innerHTML = (trees/2).toFixed(2);

    // compare with the national average
    if ((co2/1000) > 22 ){
      document.getElementById("CO2result").innerHTML = "You exceed the national average of 22Kg per year for these items";
      document.getElementById("CO2result").style.color = "red";
    }
    else {
      document.getElementById("CO2result").style.color = "green";
      document.getElementById("CO2result").innerHTML = "You are under the national average of 22Kg per year for these items";
    }

    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc;

  }
  milk_slider.oninput = function()
  {
    document.getElementById("impacts_container").style.opacity = 1;
    document.getElementById("impacts_container").style.transition = "opacity 1.5s";

    milk_output.innerHTML = this.value;
    var grey = (((5 - this.value)/5)*100).toString();
    document.getElementById("MilkImage").style.filter = "grayscale("+grey+"%)";

    //Set the CO2 scale values
    var co2 = 8*parseInt(pbag_slider.value)*52 +
              9*parseInt(diaper_slider.value)*52 +
              13.96*parseInt(coffee_slider.value)*52 +
              22*parseInt(milk_slider.value)*52;
    co2_scale.innerHTML = (co2/1000).toFixed(2);

    //Set the tree scale values
    var trees = 0.0016*parseInt(pbag_slider.value)*52 +
              0.0057*parseInt(diaper_slider.value)*52 +
              0.0014*parseInt(coffee_slider.value)*52 +
              0.0021*parseInt(milk_slider.value)*52;
    tree_scale.innerHTML = (trees).toFixed(2);

    // calculate impact alternatives
    document.getElementById("TreeCO2Val").innerHTML = (co2/6000).toFixed(2);
    document.getElementById("CarCO2Val").innerHTML = (co2/170).toFixed(2);
    document.getElementById("TreeOxyVal").innerHTML = (trees/2).toFixed(2);
    document.getElementById("TreeVal").innerHTML = (300/trees).toFixed(2);

    // Set grayscale for the tree image according to the value
    var gray_trees = (trees/20)*100;
    console.log(trees)
    console.log(gray_trees);
    document.getElementById("TreeImage").style.filter = "grayscale("+gray_trees+"%)";
    document.getElementById("TreeOxyVal").innerHTML = (trees/2).toFixed(2);
    // compare with the national average
    if ((co2/1000) > 22 ){
      document.getElementById("CO2result").innerHTML = "You exceed the national average of 22Kg per year for these items";
      document.getElementById("CO2result").style.color = "red";
    }
    else {
      document.getElementById("CO2result").style.color = "green";
      document.getElementById("CO2result").innerHTML = "You are under the national average of 22Kg per year for these items";
    }

    var co2_perc = ((co2/1000).toFixed(2)/40);
    document.getElementById("earth-base").style.opacity = co2_perc;
  }
}
