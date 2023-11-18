// 🌟 Exercise 1: Creating A Simple Express.Js Application With Routes

import express from "express";
import router from "./routes/index.js";
import todoRouter from "./routes/todo.js";
import bookRouter from "./routes/books.js";

const app = express();
const port = 9000;

app.use(express.json());

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });

app.use("/", router);
app.use("/todos", todoRouter);
app.use("/books", bookRouter);

// 🌟 Exercise 2: Simple To-Do List Exercise Using Express.Js And Express.Router.
// 🌟 Exercise 3: Basic API For Managing A List Of Books Using Express.Js And Express.Router.
