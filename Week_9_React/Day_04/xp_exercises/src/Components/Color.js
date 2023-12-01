// Create a new Functional Component named Color, with a state variable favoriteColor which value is “red”.
// Output the value in a header tag.

// Note : The useEffect() hook is called after the component is rendered.
// In the useEffect(), alert “useEffect reached”

// Note: The return is called when a component gets updated. It re-renders the DOM, with the new changes.
// Create a button that when clicked on, calls a function that changes the value of the favoriteColor property to “blue”.

import { useState, useEffect } from "react";

function Color() {

  const [favColor, setFavColor] = useState("red");

  useEffect(() => {
    alert("useEffect reached");
  }, []); 
// The empty dependency array ensures that useEffect runs only once after the initial render

  function changeColor() {
    setFavColor("blue");
  };

  return (
    <div>
      <h2>Favorite Color</h2>
      <h3>Current Color: {favColor}</h3>
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
};

export default Color;
