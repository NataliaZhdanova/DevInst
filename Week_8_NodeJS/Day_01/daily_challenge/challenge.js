// Challenge Task: Integrating Everything

// Create a file named challenge.js.
// In challenge.js, require the modules from the previous tasks: greeting.js, colorful-message.js, and read-file.js.
// Use the greet function to greet the user, display the colorful message, and read and display the file’s content.
// Run challenge.js using Node.js and see the complete challenge in action.
// By completing this challenge, you’ll have a Node.js application that demonstrates module system usage, integration of NPM modules, and file operations. It’s a comprehensive exercise that brings together concepts from the previous exercises into a single daily challenge.


import { greet } from "./greetings.js";
import { colorMessage } from "./colorful-message.js";
import { readFile } from "./read-file.js";

let username = "Max";
colorMessage(greet(username), "green");
readFile();



