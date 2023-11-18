// Sample in-memory database for storing to-do items
// Get all to-do items
// Add a new to-do item
// Update a to-do item by ID
// Delete a to-do item by ID

import express from "express";
const todoRouter = express.Router();

const todos = [];

todoRouter.get("/", (req, res) => {
    res.json(todos);
  });

todoRouter.get("/:id", (req, res) => {
    const { id } = req.params;
    const todoToGet = todos.find(todo => todo.id === parseInt(id));
    if (!todoToGet) {
        return res.status(404).json({ message: "Todo not found" });
    }
    res.json(todoToGet);
});

todoRouter.post("/", (req, res) => {
    const newTodo = { id: todos.length + 1, title: req.body };
    todos.push(newTodo);
    res.status(201).json(newTodo);
  });
  
todoRouter.put("/:id", (req, res) => {
    const { id } = req.params;
    const { title } = req.body;
    const todoToUpdate = todos.find(todo => todo.id === parseInt(id));
    if (todoToUpdate) {
      todoToUpdate.title = title;
      res.json(todoToUpdate);
      res.status(200).json("Todo is updated")
    } else {
      res.status(404).json({ message: "Todo not found" });
    }
  });
  
todoRouter.delete("/:id", (req, res) => {
    const { id } = req.params;
    const indexToRemove = todos.findIndex(todo => todo.id === parseInt(id));
    if (indexToRemove !== -1) {
      todos.splice(indexToRemove, 1);
      res.status(200).json({ message: "Todo deleted successfully" });
    } else {
      res.status(404).json({ message: "Todo not found" });
    }
  });
  
export default todoRouter;