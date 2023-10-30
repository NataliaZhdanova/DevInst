// 🌟 Exercise 1 : Change The Article
// Instructions
// Copy the code below, into a structured HTML file:

{/* <article>
    <h1> Some Facts </h1>
    <h2> The Chocolate </h2>
    <h3> History of the chocolate </h3>
    <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
    Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
    <p> After the European discovery of the Americas, chocolate became 
    very popular in the wider world, and its demand exploded. </p>
    <p> Chocolate has since become a popular food product that millions enjoy every day, 
    thanks to its unique, rich, and sweet taste.</p> 
    <p> But what effect does eating chocolate have on our health?</p> 
</article> */}


// Using a DOM property, retrieve the h1 and console.log it.

const article = document.getElementsByTagName("article")[0];
const h1Text = article.querySelector("h1").textContent;
console.log(h1Text);

// Using DOM methods, remove the last paragraph in the <article> tag.

const par = article.getElementsByTagName("p");
const lastPar = par[par.length - 1];
console.log(lastPar);
article.removeChild(lastPar);

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

const h2 = article.querySelector("h2");
h2.addEventListener("click", changeColor);
h2.addEventListener("mouseover", fadeOut);
function changeColor() {
    h2.style.backgroundColor = "red"
};
function fadeOut() {
    h2.style.visibility = "hidden";
    h2.style.opacity = 0;
    h2.style.transition = "visibility 0s 2s, opacity 2s linear";
};

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

const h3 = article.querySelector("h3");
h3.addEventListener("click", hide);
function hide() {
    h3.style.display = "none"
};

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

const buttonBold = document.querySelector("button");
buttonBold.addEventListener("click", getBold);
function getBold() {
    for (let index = 0; index < par.length; index++) {
        par[index].style.fontWeight = "bold";
    }
};

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

const h1 = article.querySelector("h1");
h1.addEventListener("mouseover", changeFontSize);
function changeFontSize() {
    let size = Math.round(Math.random() * 100);
    h1.style.fontSize = `${size}px`;
};

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)


// 🌟 Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:

// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="firstname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lastname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form> 
// <ul class="usersAnswer"></ul>
// Retrieve the form and console.log it.

const formDetails = document.querySelector("form");
console.log(formDetails);

// Retrieve the inputs by their id and console.log them.

// const inputFname = document.getElementById("fname");
// console.log(inputFname);

// const inputLname = document.getElementById("lname");
// console.log(inputLname);

// const inputSubmit = document.getElementById("submit");
// console.log(inputSubmit);

// Retrieve the inputs by their name attribute and console.log them.

const inputFname = formDetails.querySelector('input[name="firstname"]');
console.log(inputFname);

const inputLname = formDetails.querySelector('input[name="lastname"]');
console.log(inputLname);

const inputSubmit = formDetails.querySelector('input[value="Submit"]');
console.log(inputSubmit);

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ? - to prevent from page reload at submit
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :
// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>

formDetails.addEventListener("submit", submitNow);

function submitNow(e) {
    e.preventDefault();
    let inputFnameValue = inputFname.value.trim();
    let inputLnameValue = inputLname.value.trim();
    if (inputFnameValue != "" && inputLnameValue !="") {
        let newLIFname = document.createElement("li");
        let newLILname = document.createElement("li");
        newLIFname.textContent = inputFnameValue;
        newLILname.textContent = inputLnameValue;
        let elementUL = document.body.getElementsByTagName("ul")[0];
        elementUL.appendChild(newLIFname);
        elementUL.appendChild(newLILname);
    } else {
        console.log("Enter the first and last name!");
    }
};


// 🌟 Exercise 3 : Transform The Sentence
// Instructions
// Add this sentence to your HTML file then follow the steps :

{/* <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
<strong>end</strong> you <strong>will</strong> be great Developers!
<strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p> */}


// In the JS file:

// Declare a global variable named allBoldItems.

const allBoldItems = [];

// Create a function called getBoldItems() that takes no parameter. 
// This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

let paragraphArr = document.body.getElementsByTagName("p");
    let parapraph = paragraphArr[paragraphArr.length - 1];
    let strongArr = parapraph.getElementsByTagName("strong");

function getBoldItems() {
    for (index = 0; index < strongArr.length; index++) {
        allBoldItems.push(strongArr[index].textContent);
    }
}

getBoldItems();
console.log(allBoldItems);

// Create a function called highlight() that changes the color of all the bold text to blue.

function highlight() {
    for (index = 0; index < strongArr.length; index++) {
        strongArr[index].style.color = "blue";
    }
}
// Create a function called returnItemsToDefault() that changes the color of all the bold text back to black.

function returnItemsToDefault() {
    for (index = 0; index < strongArr.length; index++) {
        strongArr[index].style.color = "black";
    }
}

// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function returnItemsToDefault() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

parapraph.addEventListener("mouseover", highlight);
parapraph.addEventListener("mouseout", returnItemsToDefault);

// 🌟 Exercice 4 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
// <!doctype html> 
// <html lang="en"> 
//     <head> 
//         <meta charset="utf-8"> 
//         <title>Volume of a Sphere</title> 
//         <style>  
//             body {
//                 padding-top:30px;
//             } 

//             label,input {
//                 display:block;
//             }  
//         </style> 
//     </head> 
//     <body> 
//         <p>Input radius value and get the volume of a sphere.</p> 
//         <form  id="MyForm"> 
//             <label for="radius">Radius</label><input type="text" name="radius" id="radius" required> 
//             <label for="volume">Volume</label><input type="text" name="volume" id="volume"> 
//             <input type="submit" value="Calculate" id="submit">    
//         </form> 
//     </body> 
// </html> 

const formDetailsSphere = document.getElementById("MyForm");

const inputRadius = document.getElementById("radius");
console.log(inputFname);

const inputVolume = document.getElementById("volume");
console.log(inputLname);

const inputCalculate = document.getElementById("submit");
console.log(inputCalculate);

formDetailsSphere.addEventListener("submit", calculate);

function calculate(e) {
    e.preventDefault();
    let inputRadiusValue = inputRadius.value.trim();
    
    if (inputRadiusValue != "") {
        let volume = (4 * 3.14 * inputRadiusValue * inputRadiusValue * inputRadiusValue) / 3;
        inputVolume.value = volume;
    } else {
        console.log("Enter the radius!");
    }
}