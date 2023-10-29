// 🌟 Exercise 1 : Find The Numbers Divisible By 23
// Instructions
// Create a function call displayNumbersDivisible() that takes no parameter.

function displayNumbersDivisible() {
    let sumResult = 0;
    let outcome = "";
    for (let index = 0; index <= 500; index++) {
        if ((index % 23) === 0) {
            outcome += index + " ";
            sumResult += index;
        }
    }
    console.log(sumResult);
    console.log(outcome);
}

displayNumbersDivisible();

// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 
// 368 391 414 437 460 483
// Sum : 5313


// Bonus: Add a parameter divisor to the function.
// displayNumbersDivisible(divisor)

function displayNumbersDivisibleNew(divisor) {
    let sumResultNew = 0;
    let outcomeNew = "";
    for (let index = 0; index <= 500; index++) {
        if ((index % divisor) === 0) {
            outcomeNew += index + " ";
            sumResultNew += index;
        }
    }
    console.log(sumResultNew);
    console.log(outcomeNew);
}

displayNumbersDivisibleNew(45);

// Example:
// displayNumbersDivisible(3) : Console.log all the numbers divisible by 3, 
// and their sum
// displayNumbersDivisible(45) : Console.log all the numbers divisible by 45, 
// and their sum


// 🌟 Exercise 2 : Shopping List
// Instructions
 const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry": 1
}; 
// Add the stock and prices objects to your js file.

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. 
// It means that you have 1 banana, 1 orange and 1 apple in your cart.

let shoppingList = ["banana", "orange", "apple"];

// Create a function called myBill() that takes no parameters.

function myBill() {
    let total = 0;
    for (let index = 0; index < shoppingList.length; index++) {
        if (shoppingList[index] in stock && stock[shoppingList[index]] != 0) {
            total += prices[shoppingList[index]];
            stock[shoppingList[index]] -= 1;
        }
    }
    return total;
}
console.log(stock);
console.log("Total price: $" + myBill());
console.log(stock);

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1


// Exercise 3 : What’s In My Wallet ?
// Instructions
// Note: Read the illustration (point 4), while reading the instructions

// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.

let change = {    
    0: 0.25, 
    1: 0.10, 
    2: 0.05,
    3: 0.01
}; 

function changeEnough(itemPrice, amountOfChange) {
    let sum = 0
    for (let index = 0; index < amountOfChange.length; index++) {
        sum += (amountOfChange[index] * change[index]);

    }
    if (sum >= itemPrice) {
        return true;
    } else {
        return false;
    }
}
console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));


// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01

// 4. To illustrate:
// After you created the function, invoke it like this:
// changeEnough(4.25, [25, 20, 5, 0])
// The value 4.25 represents the item’s price
// The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)
// Examples
// changeEnough(14.11, [2,100,0,0]) => returns false
// changeEnough(0.75, [0,0,20,5]) => returns true


// 🌟 Exercise 4 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().

// function hotelCost() {
//     let nightsNum = 0;
//     while (true) {
//         let nights = prompt("Specify the number of nights you would like to stay in the hotel:");
//         if (isNaN(parseInt(nights)) === true) {
//             alert("Please enter a valid number");
//         } else {
//             nightsNum = parseInt(nights);
//             break;
//         }
//     }
//     let totalCost = nightsNum * 140;
//     return totalCost;
// };
    
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

// function planeRideCost() {
//     while (true) {
//         let price = 0
//         let destination = prompt("Specify your destination:");
//         if (destination != "") {
//             if (destination === "London") {
//                 price = 183;
//             }
//             else if (destination === "Paris") {
//                 price = 220;
//             }
//             else {
//                 price = 300;
//             }
//             return price;            
//         } else {
//             alert("Please enter a valid destination");            
//         }   
//     }
// };

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.

// function rentalCarCost() {
//     let rentNum = 0;
//     while (true) {
//         let rentDays = prompt("Specify the number of days you would like to rent a car:");
//         if (isNaN(parseInt(rentDays)) === true) {
//             alert("Please enter a valid number");
//         } else {
//             rentNum = parseInt(rentDays);
//             break;
//         }
//     }
//     if (rentNum <= 10) {
//         let rentCost = rentNum * 40;
//         return rentCost;
//     } else {
//         rentCost = rentNum * 40 * 0.95;
//         return rentCost;
//     }   
// };

// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().
// Call the function totalVacationCost()

// function totalVacationCost() {
//     let hotel = hotelCost();
//     let plane = planeRideCost();
//     let car = rentalCarCost();
//     console.log("The hotel costs: $" + hotel + ", the plane tickets cost: $" + plane + ", and the car costs: $" + car);
//     console.log("The total cost of your vacation is: $" + (hotel + plane + car));
// };

// totalVacationCost();

// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

// function hotelCostNew(nightsNumNew) {
//     let totalCostNew = nightsNumNew * 140;
//     return totalCostNew;
// };
    
// function planeRideCostNew(destinationNew) {
//     let priceNew = 0;
//     if (destinationNew === "London") {
//         priceNew = 183;
//     }
//     else if (destinationNew === "Paris") {
//         priceNew = 220;
//     }
//     else {
//         priceNew = 300;
//     }
//     return priceNew;            
// };

// function rentalCarCostNew(rentNumNew) {
//     let rentCostNew = 0;
//     if (rentNumNew <= 10) {
//         rentCostNew = rentNumNew * 40;
//     } else {
//         rentCostNew = rentNumNew * 40 * 0.95;
        
//     } 
//     return rentCostNew;  
// };

// function totalVacationCostNew() {
//     let nightsNumNew = 0;
//     let rentNumNew = 0;
//     let destinationNew = "";
//     while (true) {
//         let nightsNew = prompt("Specify the number of nights you would like to stay in the hotel:");
//         if (isNaN(parseInt(nightsNew)) === true) {
//             alert("Please enter a valid number");
//         } else {
//             nightsNumNew = parseInt(nightsNew);
//             break;
//         }
//     }
//      while (true) {
//         let rentDaysNew = prompt("Specify the number of days you would like to rent a car:");
//         if (isNaN(parseInt(rentDaysNew)) === true) {
//             alert("Please enter a valid number");
//         } else {
//             rentNumNew = parseInt(rentDaysNew);
//             break;
//         }
//     }              
//     while (true) {
//         destinationNew = prompt("Specify your destination:");
//         if (destinationNew === "") {
//             alert("Please enter a valid destination");                        
//         } else {
//             break;
//         }
//     }
   
//     console.log("The hotel costs: $" + hotelCostNew(nightsNumNew) + ", the plane tickets cost: $" + planeRideCostNew(destinationNew) + ", and the car costs: $" + rentalCarCostNew(rentNumNew));
//     console.log("The total cost of your vacation is: $" + (hotelCostNew(nightsNumNew) + planeRideCostNew(destinationNew) + rentalCarCostNew(rentNumNew)));
// };

// totalVacationCostNew();


// 🌟 Exercise 5 : Users
// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>


// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Delete the second <li> of the second <ul>.
// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)

console.log(document.getElementById("container").innerText);

document.getElementsByTagName("li")[1].innerText = "Richard";

let secondUL = document.getElementsByTagName("ul")[1];
let secondLI = secondUL.getElementsByTagName("li")[1];
secondUL.removeChild(secondLI);

for (let index = 0; index < 2; index++) {
    let elementUL = document.getElementsByTagName("ul")[index];
    let elementLI = elementUL.getElementsByTagName("li")[0];
    elementLI.innerText = "Natalia";
};

// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

for (let index = 0; index < 2; index++) {
    let elementUL = document.getElementsByTagName("ul")[index];
    elementUL.classList.add("student_list");
};

let elementUL = document.getElementsByTagName("ul")[0];
elementUL.classList.add("university", "attendance");


// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “Dan”. (the last <li> of the second <ul>)
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the first <ul>)
// Change the font size of the whole body.

let elementDiv = document.getElementById("container");
elementDiv.style.backgroundColor = 'lightblue';
elementDiv.style.padding = '20px';

let elementLIDan = document.getElementsByTagName("li")[3];
elementLIDan.style.display = "none";

let elementLIDick = document.getElementsByTagName("li")[1];
elementLIDick.style.border = "1px solid black";

// let elementBody = document.getElementsByTagName("body");
document.body.style.fontSize = "20px";

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

if (elementDiv.style.backgroundColor === 'lightblue') {
    let elementLINat = document.getElementsByTagName("li")[0].innerText;
    let elementLIDick = document.getElementsByTagName("li")[1].innerText;
    console.log("Hello, " + elementLINat + " and " + elementLIDick + "!");
    // alert("Hello, " + elementLINat + " and " + elementLIDick + "!");
};

// 🌟 Exercise 6 : Change The Navbar
// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>

// Add the code above, to your HTML file
// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

let elementNav = document.getElementById("navBar");
elementNav.setAttribute("id", "socialNetworkNavigation");


// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).

let newLI = document.createElement("li");

// Create a new text node with “Logout” as its specified text.

let newTextNode = document.createTextNode("Logout");

// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

let elementLastDiv = document.getElementById("socialNetworkNavigation");
let elementLastUL = elementLastDiv.getElementsByTagName("ul")[0];

newLI.appendChild(newTextNode);
elementLastUL.appendChild(newLI);

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). 
// Display the text of each link. (Hint: use the textContent property).
console.log(elementLastUL.lastElementChild.textContent);
console.log(elementLastUL.firstElementChild.textContent);

// Exercise 7 : My Book List
// Instructions
// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

let allBooks = [
    {"title": '"Adventures of Mr. X"', "author": "John Dow", "image": "https://www.images.com/image01.png", "alreadyRead": true},
    {"title": '"Where is the Boy?"', "author": "Jane Doe", "image": "https://www.images.com/image02.png", "alreadyRead": false}
]

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
let section = document.getElementsByClassName("listBooks")[0];
let newDiv1 = document.createElement("div");
let newDiv2 = document.createElement("div");
section.appendChild(newDiv1);
section.appendChild(newDiv2);

let book1 = document.createTextNode(allBooks[0]["title"] + " written by " + allBooks[0]["author"]);
let book2 = document.createTextNode(allBooks[1]["title"] + " written by " + allBooks[1]["author"]);

newDiv1 = section.getElementsByTagName("div")[0]
newDiv2 = section.getElementsByTagName("div")[1]

newDiv1.appendChild(book1);
newDiv2.appendChild(book2);

newDiv1.style.border = "1px solid black";
newDiv2.style.border = "1px solid black";
newDiv1.style.margin = "10px";
newDiv2.style.margin = "10px";

let image1 = document.createElement("img");
let image2 = document.createElement("img");

newDiv1.appendChild(image1);
newDiv2.appendChild(image2);

image1 = newDiv1.getElementsByTagName("img")[0];
image2 = newDiv2.getElementsByTagName("img")[0];

image1.setAttribute("src", allBooks[0]["image"]);
image2.setAttribute("src", allBooks[1]["image"]);

image1.style.width = "100px";
image2.style.width = "100px";

let divs = section.getElementsByTagName("div");

for (let index = 0; index < allBooks.length; index++) {
    if (allBooks[index]["alreadyRead"] === true) {
        divs[index].style.color = "red";
    };
};

// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.