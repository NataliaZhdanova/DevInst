// 🌟 Exercise 1 : List Of People
// Instructions
const people = ["Greg", "Mary", "Devon", "James"];
console.log(people);

// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.
people.shift();
console.log(people);

// Write code to replace “James” to “Jason”.
people[2] = "Jason";
console.log(people);

// Write code to add your name to the end of the people array.
people.push("Natalia");
console.log(people);

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
let index = people.indexOf("Mary");
console.log(index);

// Write code to make a copy of the people array using the slice method.
let peopleCopy = people.slice();
console.log(people);
console.log(peopleCopy);

// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method
let peopleNoMary = people.slice(1);
console.log(peopleNoMary);

// Write code that gives the index of “Foo”. Why does it return -1 ? - because there is no such element in an array
let indexFoo = people.indexOf("Foo");
console.log(indexFoo);

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
let last = people[people.length -1];
console.log(last);


// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.
for (let index = 0; index < people.length; index++) {
    console.log(people[index]);
}

// Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
// Hint: take a look at the break statement in the lesson.

for (let index = 0; index < people.length; index++) {
    if (people[index] === "Jason") {
        break;
    }
    else {
        console.log(people[index]);
    }
}    


// 🌟 Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

let colors = ["red", "green", "blue", "black", "violet", "teal"];
let suf = ["st", "nd", "rd", "th", "th", "th"]
for (let index = 0; index < colors.length; index++) {
    console.log("My #" + (index + 1) + " choice is " + (colors[index]));
}

for (let index = 0; index < colors.length; index++) {
    console.log("My " + (index + 1) + (suf[index]) + " choice is " + (colors[index]));
}

// 🌟 Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// let number = prompt("Provide a number...");
// let numType = typeof(number);
// console.log(numType);


// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// let numberNew = ""
// while (Number(numberNew) < 10) {
//     numberNew = prompt("Provide a number...")
// }


// 🌟 Exercise 4 : Building Management
// Instructions:
const building = {
     numberOfFloors: 4,
     numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
     nameOfTenants: ["Sarah", "Dan", "David"],
     numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
};

console.log("There are " + building.numberOfFloors + " floors in the building.");
console.log("There are " + (building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor) + " apartments on floors 1 and 3.");
console.log(Object.keys(building.numberOfRoomsAndRent)[1] + " has " + building.numberOfRoomsAndRent.dan[0] + " rooms in his apartment.");

if ((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 2200;
    console.log(building.numberOfRoomsAndRent.dan[1]);
}

// Copy and paste the above object to your Javascript file.
// Console.log the number of floors in the building.
// Console.log how many apartments are on the floors 1 and 3.
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.


// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
    father : "John",
    mother : "Mary",
    daughter : "Rosa",
    son : "Bob"
}

let keys = [];
let values = []; 

for (let key in family) { 
    keys.push(key);
    values.push(family[key]);
}
console.log(keys.toString());
console.log(values.toString());


// Exercise 6 : Rudolf
// Instructions
const details = {
   my: 'name',
   is: 'Rudolf',
   the: 'raindeer'
 }
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”

let fullText = ""

for (let detail in details) { 
    fullText += (detail) + " " + details[detail] + " ";
}
console.log(fullText);

// Exercise 7 : Secret Group
// Instructions
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

let namesSorted = names.sort();
console.log(namesSorted);

let secretName = "";
for (let index = 0; index < namesSorted.length; index++) {    
    secretName += namesSorted[index][0]; 
}
console.log(secretName);