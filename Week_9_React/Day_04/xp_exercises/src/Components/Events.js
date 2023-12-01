// Create an arrow function called clickMe. It should alert the string ‘I was clicked’.
// In the return, create a button that when clicked on, calls the clickMe function. Use the onClick event handler.

// In the Events Functional component, in the return, create an input tag that has an onKeyDown event handler, 
// that listens to a function called handleKeyDown.
// When you type something in the input field and press the ‘Enter key’, the handleKeyDown function will check 
// if the ‘Enter key’ was pressed and will alert a message with the input text value

// In the Events Functional component, using the state hook, declare a state variable named isToggleOn and set it to true.
// In the return, create a button that has an onClick event that will switch the state variable between ‘ON’ and ‘OFF’
// Create a function that will be called by the onClick event handler. In the function you should toggle the value of the isToggleOn state variable.

import { useState } from "react";

function Events() {
    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
          alert(event.target.value);
        }
      };
    const [isToggleOn, setToggleOn] = useState(true);
    function toggleState () {
		setToggleOn(!isToggleOn);
	}
    return (
        <div>
          <button onClick={() => {alert("I was clicked")}}>Click me!</button>
          <input 
                type="text"
                placeholder="Type something and press Enter"
                onKeyDown={handleKeyDown}>
          </input>
          <p>Toggle state: {isToggleOn ? 'ON' : 'OFF'}</p>
          <button onClick={toggleState}>Toggle</button>
        </div>
     
      );
  }

export default Events;