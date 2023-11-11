// Exercise 1:
// Create another file named shop.js.
// In shop.js, require the product objects from the products.js module.
// Create a function that takes a product name as a parameter and searches for the corresponding product object.
// Call this function with different product names and print the details of the products.
// Run shop.js and verify that the correct product details are displayed.

import products from "./product.js";

function findProduct(name) {
    const product = products.find(product => product.name === name);
    return product;
}

console.log(findProduct("Coffee"));
console.log(findProduct("Chess"));

// Exercise 2:
// Create another file named app.js.
// In app.js, import the array of person objects from the data.js module.
// Write a function that calculates and prints the average age of all the persons in the array.
// Use the imported array and the average age function in app.js.
// Run app.js and confirm that the average age is correctly calculated and displayed.


import people from "./data.js";

function avgAge(people) {
  const totalAge = people.reduce((sum, person) => sum + person.age, 0);
  const avgAge = totalAge / people.length;
  return avgAge;
}

console.log(avgAge(people));

// Exercise 3:
// Create another file named app.js.
// In app.js, import the functions from the fileManager.js module.
// Use the imported functions to read the content of the “Hello World.txt” text file and then write to the “Bye World.txt” with the content “Writing to the file”.
// Run app.js and verify that the file reading and writing operations are successful.


import { readFile, writeFile } from "./fileManager.js";

console.log(readFile("./Hello_World.txt"));

writeFile("Bye_World.txt", "Writing to the file");

console.log(readFile("./Bye_World.txt"));

// Exercise 4:
// In app.js, import the TodoList class from the todo.js module.
// Create an instance of the TodoList class.
// Add a few tasks, mark some as complete, and list all tasks.
// Run app.js and verify that the todo list operations are working correctly.

import TodoList from "./todo.js";

const myTodo = new TodoList();

myTodo.addTask("Do something 1");
myTodo.addTask("Do something 2");
myTodo.addTask("Do something 3");


myTodo.completeTask("Do something 1");

myTodo.allTasks();

// Exercise 5:
// Create a file named app.js in the same directory.
// In app.js, require the lodash package and the custom math module.
// Use the exported functions from the math module and the utility functions from the lodash package to perform calculations.
// Run app.js using Node.js and verify that the calculations are correct.

import _ from "lodash";
import { add, multiply } from "./math.js";


const sum = _.sum([10, 5, 20, 30]);
const mult = _.multiply(6, 8);

const sumMath = add(33, 66);
const multMath = multiply(6, 8);

console.log(sum);
console.log(mult);
console.log(sumMath);
console.log(multMath);

// Exercise 6:
// In app.js, require the chalk package and use it to color and style text in the terminal.
// Write a simple script that uses chalk to print a colorful message.
// Run app.js using Node.js and observe the colorful output in the terminal.

import chalk from "chalk";

console.log(chalk.blue("Hello, blue World!"));
console.log(chalk.green.bold("Bye, green World!!"));
console.log(chalk.red.underline("Bye, red people!"));

// Exercise 7:
// Create a directory named file-explorer.
// Inside the file-explorer directory, create a file named copy-file.js.
// In copy-file.js, use the fs module to read the content from a file named source.txt and then write the same content to a new file named destination.txt.

import fs1 from "fs";

fs1.readFile("./Hello_World.txt", (err, data) => {
	if (err) {
	console.log("error!");
	}
	fs1.writeFile("destination.txt", data, err => {
        if (err) {
        console.log(err);
        }
    });
    
});

// Create another file named read-directory.js.
// In read-directory.js, use the fs module to read the list of files in a specified directory and display their names in the terminal.
// Open a terminal in the file-explorer directory.
// Run node copy-file.js to copy the content from source.txt to destination.txt.
// Run node read-directory.js to list the files in the directory.

import fs from "fs";

const path = './';

fs.readdir(path, (err, files) => {
  if (err) {
    console.log("error!");
  }

  console.log("The following files are in the directory:");
  files.forEach(file => {
    console.log(file);
  });
});
