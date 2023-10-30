// Instructions
// In this exercise we will be creating a webpage with a black background as the universe and we will fill the universe with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.

// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?
// <!DOCTYPE html>
// <html>
//     <head>
//         <meta charset="utf-8">
//         <title>Challenge: Create a solar system</title>
//         <style>
//             body {
//                 background-color: black;
//                 padding: 10px;
//             }
//             .planet {
//                 width: 100px;
//                 height: 100px;
//                 border-radius: 50%;
//                 text-align: center;
//                 padding: 10px;
//                 position: relative;
//                 border: 2px solid white;
//             }
//             .moon {
//                 position: absolute;
//                 width: 30px;
//                 height: 30px;
//                 border-radius: 50%;
//                 background: rgb(237, 237, 237);
//                 border: 5px solid red;
//             }
//         </style>
//     </head>
//     <body>

//     <section class="listPlanets"></section>

//     <script src="..."></script>
//     </body>
// </html>

let listPlanetsSection = document.getElementsByClassName("listPlanets")[0];

let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
let colors = ["orange", "blue", "green", "red", "yellow", "wheat", "teal", "violet"];
let moons = [0, 1, 1, 1, 0, 5, 3, 2];

planets.forEach((planet, index) => {
    let newDiv = document.createElement("div");
    newDiv.textContent = planet;
    newDiv.classList.add("planet", `planet${index + 1}`);
    listPlanetsSection.appendChild(newDiv);
    });

colors.forEach((color, index) => {
    let newDiv = listPlanetsSection.getElementsByClassName("planet")[index];
    newDiv.style.backgroundColor = color;
})

for (let index = 0; index < moons.length; index++) {
    let newDiv = listPlanetsSection.getElementsByClassName("planet")[index];
    if (moons[index] > 0) {
        for (let iterator = 1; iterator <= moons[index]; iterator++) {
            let newMoon = document.createElement("div");
            newMoon.classList.add("moon", `moon${iterator}`);
            newDiv.appendChild(newMoon);

        }
    }
}


    
