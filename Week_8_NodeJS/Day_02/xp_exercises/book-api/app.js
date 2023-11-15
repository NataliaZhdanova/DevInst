// 🌟 Exercise 2: Building A Basic CRUD API With Express.Js
// Instructions
// In this exercise, you’ll build a basic CRUD (Create, Read, Update, Delete) API using Express.js. 
//Your task is to create routes to manage a collection of books.

// In app.js, import the express module and create an instance of an Express app.

import express from "express";
const app = express();


// Define a basic data array containing a few book objects. Each book object should have properties like id, title, author, and publishedYear.

let books = [
    { id: 1, title: "Book1", author: "Author1", publishedYear: 2020 },
    { id: 2, title: "Book2", author: "Author2", publishedYear: 2021 },
    { id: 3, title: "Book3", author: "Author3", publishedYear: 2022 },
    { id: 4, title: "Book4", author: "Author4", publishedYear: 2023 },
    { id: 5, title: "Book5", author: "Author5", publishedYear: 2024 }
  ];

// Set up the app to listen on port 5000. Print a message in the console to indicate that the server is running.

const port = 5000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });

// Implement the “Read all” route by defining a route at GET /api/books. Send a JSON response with the books array.

app.use(express.json());

app.get("/api/books", (req, res) => {
    res.json(books);
  });

// Implement the “Read” route by defining a route at GET /api/books/:bookId. Extract the bookId parameter 
// from the URL and use it to find the corresponding book in the books array. If the book is found, 
// send a JSON response with the book details and a status code of 200 (OK). If the book is not found, 
// send a 404 status with a “Book not found” message.

app.get("/api/books/:bookId", (req, res) => {
    const bookId = parseInt(req.params.bookId);
    const book = books.find((book) => book.id === bookId);
  
    if (book) {
      res.json(book);
      res.status(200).send("OK!");
    } else {
      res.status(404).send("The book was not found!");
    }
  });


// Implement the “Create” route at POST /api/books. Use the express.json() middleware to parse JSON body content. 
// Inside the route handler, create a new book object with an incremented ID and the data from the request body. 
// Add the new book to the books array and return a JSON response with the new book and a status code of 201 
// (Created).


app.post("/api/books", (req, res) => {
  const newBook = {
    id: books.length + 1,
    title: req.body.title,
    author: req.body.author,
    publishedYear: req.body.publishedYear
  };

  books.push(newBook);
  res.status(201).send("Created");
});



