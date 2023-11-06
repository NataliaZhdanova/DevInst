// 🌟 Exercise 1 : Scope
// Instructions
// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.
// // #1
// function funcOne() {
//     const a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// funcOne();

// Answer: "a" will be equal to 3, because inner containers have access to variables of outer containers and can change their values.

// // #1.1 - run in the console:
// funcOne()
// // #1.2 What will happen if the variable is declared 
// // with const instead of let ?

// Answer: an error will be output to the console log, because one cannot change the value of a constant variable.

// //#2
// const a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// Answer: before funcTwo is executed, "a" = 0, after it is executed - "a" = 5, , because inner containers have access to variables of outer containers and can change their values.

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?

// Answer: first, "a" = 0, then an error will be output to the console log, because one cannot change the value of a constant variable.


// #3
// function funcFour() {
//     window.a = "hello";
// }

// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// #3.1 - run in the console:
// funcFour()
// funcFive()

// Answer: "a" will be equal to "hello", because "window.a" creates a variable in an outer container with regard to both functions.

//#4
// const a = 1;
// function funcSix() {
//     const a = "test";
//     alert(`inside the funcSix function ${a}`);
// }

// Answer: "a" will be equal to "test, because this value is in the nearest container."

// #4.1 - run in the console:
// funcSix()
// #4.2 What will happen if the variable is declared with const instead of let ?

// Answer: "a" will be equal to "test, because this value is in the nearest container."

// #5
// const a = 2;
// if (true) {
//     const a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared with const instead of let ?

// Answer: the result will be the same as with "let", because each alert will take a value from a variable belonging to their corresponding container.


// 🌟 Exercise 2 : Ternary Operator
// Instructions
// Using the code below:

// function winBattle(){
//     return true;
// }
// Transform the winBattle() function to an arrow function.
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
// Console.log the experiencePoints variable.

const winBattle = () => true;

const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);


// 🌟 Exercise 3 : Is It A String ?
// Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
// Check out the example below to see the expected output

const isString = (string) => typeof string === 'string';
console.log(isString('hello')); 
console.log(isString([1, 2, 4, 0]));

// 🌟 Exercise 4 : Find The Sum
// Instructions
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.

const sum = (a, b) => a + b;
console.log(sum(10, 5));


// 🌟 Exercise 5 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

// First, use function declaration and invoke it.
// Then, use function expression and invoke it.
// Write in a one line comment, the difference between function declaration and function expression.
// Finally, use a one line arrow function and invoke it.

// Declaration:
function toGrams(kilos) {
    return kilos * 1000;
}
console.log(toGrams(5));

// Expression:
const toGramsNew = function(kilos) {
    return kilos * 1000;
};
console.log(toGramsNew(3));

// Function declarations are hoisted, which means they are moved to the top of the code before execution. Function expressions are not hoisted, and therefore cannot be called before they appear in the code.

// Arrow:
const toGrams2 = kilos => kilos * 1000;
console.log(toGrams2(10));


// 🌟 Exercise 6 : Fortune Teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

(function(numberOfKids, partnerName, location, title) {
    const sentence = `You will be a ${title} in ${location}, and married to ${partnerName} with ${numberOfKids} kids.`;
    document.getElementById("output").innerHTML = sentence;
  })(3, "John", "Tel-Aviv", "Surgeon");

// 🌟 Exercise 7 : Welcome
// Instructions
// John has just signed in to your website and you want to welcome him.

// Create a Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.

(function(welcome) {
    const navbar = document.getElementById("navbar");
    const div = document.createElement("div");
    div.innerHTML = `Welcome, ${welcome}! <img src="https://images.net/profile_pic.png" alt="Profile Picture" width="50" height="50">`;
    navbar.appendChild(div);
  })("John");


// 🌟 Exercise 8 : Juice Bar
// Instructions
// You will use nested functions, to open a new juice bar.

// Part I:
// The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.

// The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like 
// The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

// Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.

// function makeJuice(size) {
//     function addIngredients(in1, in2, in3) {
//         const sentence = `The client wants a ${size} juice, containing ${in1}, ${in2}, and ${in3}.`;
//         document.getElementById("juice").innerHTML = sentence;
//     }
//     addIngredients("apple", "cucumber", "lime");
// }

// makeJuice("small");


// Part II:
// In the makeJuice function, create an empty array named ingredients.

// The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.

// Create a new inner function named displayJuice that displays on the DOM a sentence like 
// The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

// The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. 
// Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.

function makeJuice(size) {
    const ingredients = [];
    function addIngredients(in1, in2, in3) {
        ingredients.push(in1, in2, in3);
    }
    function displayJuice() {
        const sentence = `The client wants a ${size} juice, containing ${ingredients.join(", ")}.`;
        document.getElementById("juice").innerHTML = sentence;
    }
    addIngredients("apple", "cucumber", "lime");
    addIngredients("tomato", "carrot", "selery");
    displayJuice();
}

makeJuice("small");