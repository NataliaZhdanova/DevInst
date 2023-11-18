// 🌟 Exercise 1 : Building A RESTful API With Database Connection
// Instructions
// You’re tasked with building a RESTful API for a blog platform.
// Users should be able to create, read, update, and delete blog posts using different endpoints.

// Create a directory named blog-api.


// Inside the blog-api directory, open a terminal and run npm init to initialize a new Node.js project. Follow the prompts to set up your project.


// Install the express package by running npm install express in the terminal.


// Create a file named server.js.


// In server.js, require the express package and set up an Express app.


// Create a posts table in postgres database, with the properties like id, title, and content.


// Implement the following routes using Express:

// GET /posts: Return a list of all blog posts.
// GET /posts/:id: Return a specific blog post based on its id.
// POST /posts: Create a new blog post.
// PUT /posts/:id: Update an existing blog post.
// DELETE /posts/:id: Delete a blog post.


// Create this directory structure:

// server
//     |_ config
//     |_ controllers
//     |_ models
//     |_ routes


// Implement error handling for invalid routes and server errors.


// Start the Express app and listen on a specified port (e.g., 3000).



// 🌟 Exercise 2 : Building A Basic CRUD API With Database Connection
// Instructions
// In this exercise, you’ll build a basic CRUD (Create, Read, Update, Delete) API using Express.js. Your task is to create routes to manage a collection of books.

// Create a new directory named book-api.


// Inside the book-api directory, initialize a new Node.js project and install the express package.


// Create a new file named app.js in the book-api directory.


// In app.js, import the express module and create an instance of an Express app.


// Define a basic data books table with properties like id, title, author, and publishedYear.


// Create this directory structure:

// server
//     |_ config
//     |_ controllers
//     |_ models
//     |_ routes


// Set up the app to listen on port 5000. Print a message in the console to indicate that the server is running.


// Implement the “Read all” route by defining a route at GET /api/books. Send a JSON response with the books array.


// Implement the “Read” route by defining a route at GET /api/books/:bookId. Extract the bookId parameter from the URL and use it to find the corresponding book in the books array. If the book is found, send a JSON response with the book details and a status code of 200 (OK). If the book is not found, send a 404 status with a “Book not found” message.


// Implement the “Create” route at POST /api/books.

