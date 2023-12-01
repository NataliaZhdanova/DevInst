// Create a new Functional Component named Phone. Use the state hook to create the following state variables:

// brand: "Samsung"
// model: "Galaxy S20"
// color: "black"
// year: 2020

// In the return of the Phone component, display the values of the state variables.
// Import the Phone component and display it in your App.js.

// In the Phone component create a function named changeColor that updates the state variable to ‘blue’
// In the return, add a button with an onClick event that will call the changeColor function to change the color state variable.


// Phone.js

import { useState } from "react";

function Phone() {

  const [brand, setBrand] = useState("Samsung");
  const [model, setModel] = useState("Galaxy S20");
  const [color, setColor] = useState("black");
  const [year, setYear] = useState(2020);


  function changeColor() {
    setColor("blue");
  };

  return (
    <div>
      <h2>Phone Details</h2>
      <p>Brand: {brand}</p>
      <p>Model: {model}</p>
      <p>Color: {color}</p>
      <p>Year: {year}</p>
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
};

export default Phone;
