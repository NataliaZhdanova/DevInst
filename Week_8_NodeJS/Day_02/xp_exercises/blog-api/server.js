// 🌟 Exercise 1: Building A RESTful API
// Create a file named server.js.
// In server.js, require the express package and set up an Express app.
// Create a data array to simulate a database. Each item in the array should represent a blog post with properties like id, title, and content.

// Implement the following routes using Express


import express from "express";
const app = express();
const port = 3000;

let data = [
  { id: 1, title: "First Post", content: "This is the content of the first post." },
  { id: 2, title: "Second Post", content: "This is the content of the second post." },
  { id: 3, title: "Third Post", content: "This is the content of the third post." },
  { id: 4, title: "Fourth Post", content: "This is the content of the fourth post." },
];

app.use(express.json());

// GET /posts: Return a list of all blog posts.

app.get("/posts", (req, res) => {
  res.json(data);
});

// GET /posts/:id: Return a specific blog post based on its id.

app.get("/posts/:id", (req, res) => {
  const postId = parseInt(req.params.id);
  const post = data.find(post => post.id === postId);
// Implement error handling for invalid routes and server errors.
  if (!post) {
    res.status(404).json({ error: "The requested post is not found on the server" });
    return;
  }
  

  res.json(post);
});

// POST /posts: Create a new blog post.

app.post("/posts", (req, res) => {
  const { title, content } = req.body;
  const newPost = { id: data.length + 1, title, content };
  data.push(newPost);
  res.status(201).json(newPost);
});

// PUT /posts/:id: Update an existing blog post.

app.put("/posts/:id", (req, res) => {
  const postId = parseInt(req.params.id);
  const postIndex = data.findIndex(post => post.id === postId);
// Implement error handling for invalid routes and server errors.
  if (postIndex === -1) {
    res.status(404).json({ error: "The requested post is not found on the server" });
    return;
  }

  const updatedPost = { ...data[postIndex], ...req.body };
  data[postIndex] = updatedPost;

  res.json(updatedPost);
});

// DELETE /posts/:id: Delete a blog post.

app.delete("/posts/:id", (req, res) => {
  const postId = parseInt(req.params.id);
  data = data.filter(post => post.id !== postId);
  res.json({ message: "The post is deleted successfully" });
});

// Implement error handling for invalid routes and server errors.
app.use((req, res) => {
  res.status(404).json({ error: "The route is invalid" });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: "Internal Server Error" });
});

// Start the Express app and listen on a specified port (e.g., 3000).

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
