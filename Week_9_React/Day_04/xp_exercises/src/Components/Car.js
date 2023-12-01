// In the Car.js component render a header with the carInfo model, for example This car is <model>.
// Import the Car.js component to the App.js.

// Use the state hook in the Car component to add a color variable to the state.
// Return the color property, for example This car is <color> <model>.

import { carInfo } from "../App.js";
import Garage from "./Garage.js";
import { useState } from "react";

function Car() {
    const [ color, setColor ] = useState("");
    
    function recolor(carColor) {
		setColor(carColor);
	}
    return (
        <div>
          <h2>This car is {color} {carInfo.model}.</h2>
          <button onClick={() => {recolor("red")}}>Paint it!</button>
          <Garage size="small" />
        </div>
        
      );
  }

export default Car;