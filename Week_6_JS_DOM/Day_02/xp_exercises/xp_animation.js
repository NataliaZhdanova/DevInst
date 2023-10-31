// 🌟 Exercise 1: Timer
// Instructions
// Using this HTML code:

// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         p {
//           background: yellow;
//           color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <div id="container"></div>
//         <button id="clear">Clear Interval</button>
//     </body>
//     </html>


// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.
 
// function hello() {
//     alert("Hello, world!");
//  }

//  setTimeout(hello, 2000);


// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

// function addP() {
//     let div = document.getElementById("container");
//     let newP = document.createElement("p");
//     let helloW = document.createTextNode("Hello World");
//     newP.appendChild(helloW);
//     div.appendChild(newP);
// }

// setTimeout(addP, 2000);

// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.


let timer = setInterval(stopFive, 2000);
let btn = document.getElementById("clear");
btn.addEventListener("click", stopOutput);

function stopOutput() {
    clearInterval(timer);
}

function stopFive() {
    let div = document.getElementById("container");
    let newP = document.createElement("p");
    let helloW = document.createTextNode("Hello World");
    newP.appendChild(helloW);
    let pArr = document.getElementsByTagName("p");
    if (pArr.length < 6) {
        div.appendChild(newP);
    } else {
        clearInterval(timer);
    }
};

// 🌟 Exercise 2 : Move The Box
// Instructions
// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         #containerAn {
//           width: 400px;
//           height: 400px;
//           position: relative;
//           background: yellow;
//         }
//         #animate {
//           width: 50px;
//           height: 50px;
//           position: absolute;
//           background-color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <p><button onclick="movingSquare()">Click Me</button></p>
//         <div id="containerAn">
//           <div id="animate"></div>
//         </div>
//     </body>
//     </html>


// Copy the code above, to a structured HTML file.
// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions


function movingSquare() {
    let square = document.getElementById("animate");
    let containerWidth = document.getElementById("containerAn").offsetWidth;
    let position = 0;
    let timer = setInterval(move, 1);
    function move() {
        if (position == containerWidth - 50) {
            clearInterval(timer);
        } else {
            position++;
            square.style.left = position + "px";
        }
    }
}