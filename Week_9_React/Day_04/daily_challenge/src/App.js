import { useState } from "react";


function App() {

  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaScript", votes: 0 },
    { name: "Java", votes: 0 }
  ]);

  function increaseVotes(languageIndex) {
  
    const updatedLanguages = [...languages];
    updatedLanguages[languageIndex].votes += 1;

    setLanguages(updatedLanguages);
  };

  return (
    <div>
      <h1>Voting App</h1>
      {languages.map((language, index) => (
        <div key={index}>
          <p>{language.name}: {language.votes} votes</p>
          <button onClick={() => increaseVotes(index)}>Vote for {language.name}</button>
        </div>
      ))}
    </div>
  );
};

export default App;

// Instructions : React Voting App
// Your goal is to create a voting app.

// Steps
// In the App.js create an array of objects in the state. Each object contains the language and the number of votes per language.
// Use the below object as a starting point:

// const [languages, setLanguages] = useState([
//                                             {name: "Php", votes: 0},
//                                             {name: "Python", votes: 0},
//                                             {name: "JavaSript", votes: 0},
//                                             {name: "Java", votes: 0}
//                                           ])
// <br>
// Create a function that increases the state of the votes by one, when you click on a specific language button.
