import Car from "./Components/Car";
import Events from "./Components/Events";
import Phone from "./Components/Phone";
import Color from "./Components/Color";

export const carInfo = {name: "Ford", model: "Mustang"};

export function App() {
  return (
    <div>
      <Car />
      <Events />
      <Phone />
      <Color />
    </div>
    
  );
}
