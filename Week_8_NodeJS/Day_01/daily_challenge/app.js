// Task 1: Basic Module System
// Create another file named app.js in the same directory.
// In app.js, require the greeting.js module and use the greet function to greet a user.
// Run app.js using Node.js and see the greeting message.

import { greet } from "./greetings.js";
greet("Max");
greet("Anna");

// Task 2: Using an NPM Module

// Inside the daily-challenge directory, open a terminal and run npm init to initialize a new Node.js project. Follow the prompts to set up your project.
// Install the chalk package by running npm install chalk in the terminal.
// Create a file named colorful-message.js.
// In colorful-message.js, require the chalk package and use it to create and display a colorful message in the terminal.
// Create another file named app.js.
// In app.js, require the colorful-message.js module and call the function you’ve written to display the colorful message.
// Run app.js using Node.js and see the colorful message.

import { colorMessage } from "./colorful-message.js";
colorMessage("Hello, world!", "green");
colorMessage("Bye, world!", "blue");

// Task 3: Advanced File Operations

// Inside the daily-challenge directory, create a directory named files.
// Inside the files directory, create a file named file-data.txt and add some text content to it.
// Create a file named read-file.js.
// In read-file.js, require the fs module and read the content from the file-data.txt file. Display the content in the terminal.
// Create another file named app.js.
// In app.js, require the read-file.js module and call the function you’ve written to display the file’s content.
// Run app.js using Node.js and see the content of the file.

import { readFile } from "./read-file.js";
readFile();


