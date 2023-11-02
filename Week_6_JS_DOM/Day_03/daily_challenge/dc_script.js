// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank inputs with different word types 
// (ie : noun, adjective, verb), and then a story is generated based on the words you chose, and sometimes the story is surprisingly funny.

// In this exercise you work with the HTML code presented below.

{/* <h1>Mad Libs</h1>

<form id="libform">
    <label for="noun">Noun:</label><input type="text" id="noun"><br>
    <label for="adjective">Adjective:</label><input type="text" id="adjective"><br>
    <label for="person">Someone's Name:</label><input type="text" id="person"><br>
    <label for="verb">Verb:</label><input type="text" id="verb"><br>
    <label for="place">A place:</label><input type="text" id="place"><br>
    <button id="lib-button">Lib it!</button>
</form>

<p>Generated story: 
<span id="story"></span>
</p> */}

// Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed 
// (but keep the values entered by the user). The user could click the button at least three times and get a new story. 
// Display the stories randomly.

{/* <h1>Mad Libs</h1>

<form id="libform">
    <label for="adjective1">Adjective:</label><input type="text" id="adjective1"><br>
    <label for="noun1">Noun:</label><input type="text" id="noun1"><br>
    <label for="person">Someone's Name:</label><input type="text" id="person"><br>
    <label for="noun2">Noun:</label><input type="text" id="noun2"><br>
    <label for="verb">Verb:</label><input type="text" id="verb"><br>
    <label for="noun3">Noun:</label><input type="text" id="noun3"><br>
    <label for="adjective2">Adjective:</label><input type="text" id="adjective2"><br>
    <label for="noun4">Noun:</label><input type="text" id="noun4"><br>
    <label for="noun5">Noun:</label><input type="text" id="noun5"><br>
    <label for="place">A place:</label><input type="text" id="place"><br>
    <button id="lib-button">Lib it!</button>
</form>

<p>Generated story: 
<span id="story"></span>
</p> */}

let form = document.getElementById("libform");
let btn = document.getElementById("lib-button");
let storyFinal = document.getElementById("story");
let shuffleBtn = document.getElementById("shuffle");

form.addEventListener("submit", story);

function story(e) {
    e.preventDefault();

    let adj1 = document.getElementById("adjective1").value;
    let noun1 = document.getElementById("noun1").value;
    let person = document.getElementById("person").value;
    let noun2 = document.getElementById("noun2").value;
    let verb = document.getElementById("verb").value;
    let noun3 = document.getElementById("noun3").value;
    let adj2 = document.getElementById("adjective2").value;
    let noun4 = document.getElementById("noun4").value;
    let noun5 = document.getElementById("noun5").value;
    let place = document.getElementById("place").value;

    if (noun1 && noun2 && noun3 && noun4 && noun5 && adj1 && adj2 && person && verb && place) {
        let story = `The Hilarious Date: One evening, during a ${adj1} ${noun1}, the ${person} tripped and spilled ${noun2} all over the couple. Trying to ${verb} his date, the gentleman decided to join in, turning the ${noun3} into a ${adj2} ${noun4}. In the end, they laughed so hard that they attracted the ${noun5} of the entire ${place}.`
        storyFinal.textContent = story;
    }
};

shuffleBtn.addEventListener("click", shuffle);

function shuffle() {
    let adj1 = document.getElementById("adjective1").value;
    let noun1 = document.getElementById("noun1").value;
    let person = document.getElementById("person").value;
    let noun2 = document.getElementById("noun2").value;
    let verb = document.getElementById("verb").value;
    let noun3 = document.getElementById("noun3").value;
    let adj2 = document.getElementById("adjective2").value;
    let noun4 = document.getElementById("noun4").value;
    let noun5 = document.getElementById("noun5").value;
    let place = document.getElementById("place").value;
    
    let stories = [
        `The Hilarious Date: One evening, during a ${adj1} ${noun1}, the ${person} tripped and spilled ${noun2} all over the couple. Trying to ${verb} his date, the gentleman decided to join in, turning the ${noun3} into a ${adj2} ${noun4}. In the end, they laughed so hard that they attracted the ${noun5} of the entire ${place}.`,
        `The Unfortunate Camping Trip: While on a camping trip, a group of friends decided to tell ${adj1} stories around the ${noun1}. However, the ${person}'s ${noun2} started playing creepy sounds, scaring everyone. In their rush to ${verb}, they stumbled into a nearby ${noun3}, only to find out later that it was just a ${adj2} ${noun4} by another ${noun5} in the ${place}.`,
        `The Absent-Minded Professor: In the middle of a ${adj1} ${noun1}, the absent-minded ${person} accidentally used his ${noun2} as a pointer, much to the confusion of the students. When he finally noticed, he tried to ${verb} it off as a new teaching ${noun3}, leaving the ${adj2} ${noun4} bewildered yet thoroughly entertained. His ${noun5} in the ${place} remained unchanged.`
    ];

    let index = Math.floor(Math.random() * stories.length);
    storyFinal.textContent = stories[index];
};