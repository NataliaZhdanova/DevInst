// Instructions
// 1. Set up a new Express.js application.
// 2. Implement the following routes using express.Router:

// GET /tasks: Retrieve a list of all tasks from a JSON file.
// GET /tasks/:id: Retrieve a specific task by ID from the JSON file.
// POST /tasks: Create a new task and store it in the JSON file.
// PUT /tasks/:id: Update a task by ID in the JSON file.
// DELETE /tasks/:id: Delete a task by ID from the JSON file.
// 3. Create a JSON file (e.g., tasks.json) to store task data. Initialize it with an empty array [].
// 4. Use appropriate validation to ensure the user provides necessary data when creating or updating tasks.
// 5. Implement error handling for file read/write operations and route validation.
// 6. Test your API using tools like Postman or curl.


import express from "express";
import router from "./routes/index.js";

const app = express();
const port = 9000;

app.use(express.json());

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });

app.use("/tasks", router);

app.use((req, res) => {
    res.status(404).json({ error: "Route not found" });
  });

app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: "Internal Server Error" });
  });
