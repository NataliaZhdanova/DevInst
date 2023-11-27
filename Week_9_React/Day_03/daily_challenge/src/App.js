import './App.css';
import { Carousel } from 'react-responsive-carousel';
import img1 from "./jrfyzvgzvhs1iylduuhj.jpg";
import img2 from "./liw377az16sxmp9a6ylg.webp";
import img3 from "./e8fnw35p6zgusq218foj.webp";
import img4 from "./c1cklkyp6ms02tougufx.webp";

function App() {
  return (
      <Carousel>
          <div>
              <img src={img1} />
              <p className="legend">Hong Kong</p>
          </div>
          <div>
              <img src={img2} />
              <p className="legend">Las Vegas</p>
          </div>
          <div>
              <img src={img3} />
              <p className="legend">Japan</p>
          </div>
          <div>
              <img src={img4} />
              <p className="legend">Macao</p>
          </div>
      </Carousel>
);
}

export default App;
