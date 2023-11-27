import './App.css';
import UserFavoriteAnimals from "./UserFavoriteAnimals.js";
import Exercise from "./Exercise3.js";

// Create a constant variable with JSX const myelement = <h1>I Love JSX!</h1>;, and render it on the page.
const myelement = <h1>I Love JSX!</h1>;

// Create a constant variable named sum, which value is 5 + 5. 
// Render on the page, the following sentence "React is <sum> times better with JSX"

const myelement1 = <h2>React is {5 + 5} times better with JSX</h2>;

// In the App.js file, render the first name and the last name of the user in two <h3>.

export const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

// In the App.js file, display a “Hello World!” message in a paragraph.
export function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Hello, World!
        </p>
        <Exercise />
        <h3>{user.firstName}</h3>
        <h3>{user.lastName}</h3>
        {myelement}
        {myelement1}
        <UserFavoriteAnimals />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}