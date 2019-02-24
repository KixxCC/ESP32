// Create a new color picker instance
// https://iro.js.org/guide.html#Getting-Started
var colorPicker = new iro.ColorPicker(".colorPicker", {
  // color picker options
  // Option guide: https://iro.js.org/guide.html#Color-Picker-Options
  width: 280,
  color: "rgb(255, 0, 0)",
  borderWidth: 1,
  borderColor: "#fff",
});

var values = document.getElementById("values");

// https://iro.js.org/guide.html#color-change
colorPicker.on("color:change", function(color){
  // Show the current color in different formats
  // Using the selected color: https://iro.js.org/guide.html#Using-the-Selected-Color
  values.innerHTML = [
    "hex: " + color.hexString,
    "rgb: " + color.rgbString,
    "hsl: " + color.hslString,
  ].join("<br>");
});
