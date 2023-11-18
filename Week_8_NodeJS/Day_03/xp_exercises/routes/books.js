// routes/books.js
// Sample in-memory database for storing books
// Get all books
// Add a new book
// Update a book by ID
// Delete a book by ID

import express from "express";
const bookRouter = express.Router();

const books = [];

bookRouter.get("/", (req, res) => {
    res.json(books);
  });

bookRouter.get("/:id", (req, res) => {
    const { id } = req.params;
    const bookToGet = books.find(book => book.id === parseInt(id));
    if (!bookToGet) {
        return res.status(404).json({ message: "Book not found" });
    }
    res.json(bookToGet);
});

bookRouter.post("/", (req, res) => {
    const newBook = { id: todos.length + 1, title: req.body.title, author: req.body.author };
    books.push(newBook);
    res.status(201).json(newBook);
  });
  
bookRouter.put("/:id", (req, res) => {
    const { id } = req.params;
    const { title } = req.body.title;
    const { author } = req.body.author;
    const bookToUpdate = books.find(book => book.id === parseInt(id));
    if (bookToUpdate) {
      bookToUpdate.title = title;
      bookToUpdate.author = author;
      res.json(bookToUpdate);
      res.status(200).json("Book updated")
    } else {
      res.status(404).json({ message: "Book not found" });
    }
  });
  
bookRouter.delete("/:id", (req, res) => {
    const { id } = req.params;
    const indexToRemove = books.findIndex(book => book.id === parseInt(id));
    if (indexToRemove !== -1) {
      books.splice(indexToRemove, 1);
      res.status(200).json({ message: "Book deleted successfully" });
    } else {
      res.status(404).json({ message: "Book not found" });
    }
  });
  
export default bookRouter;

// GET http://localhost:3000/books (Get all books)
// POST http://localhost:3000/books (Create a new book with a JSON request body)
// PUT http://localhost:3000/books/:id (Update a book by ID with a JSON request body)
// DELETE http://localhost:3000/books/:id (Delete a book by ID)
