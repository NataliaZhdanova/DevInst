// Use an attribute to pass a size to the Garage component, <Garage size="small" />.

// Use the Garage component inside the Car component and pass the size ‘small’. 
// The Garage component should render Who lives in my <size> Garage?


function Garage({size}) {
    return (
        <div>
          <h2>Who lives in my {size} Garage?</h2>
        </div>
      );
  }

export default Garage;