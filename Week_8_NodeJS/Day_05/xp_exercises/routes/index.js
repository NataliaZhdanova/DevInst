import express from "express";
const router = express.Router();
import { promises as fs } from "fs";
import path from "path";
import bodyParser from "body-parser";
import { fileURLToPath } from "url";
import { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

router.use(bodyParser.json());

const tasksFilePath = path.join(__dirname, "../data/tasks.json");

router.get("/", async (req, res) => {
  try {
    const data = await fs.readFile(tasksFilePath, "utf-8");
    const tasks = JSON.parse(data);
    res.json(tasks);
  } catch (error) {
    console.error("Error reading tasks:", error.message);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

router.get("/:id", async (req, res) => {
  const taskId = req.params.id;
  try {
    const data = await fs.readFile(tasksFilePath, "utf-8");
    const tasks = JSON.parse(data);
    const task = tasks.find((t) => t.id === taskId);
    if (!task) {
      res.status(404).json({ error: "Task not found" });
      return;
    }
    res.json(task);
  } catch (error) {
    console.error("Error reading tasks:", error.message);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

router.post("/", async (req, res) => {
  const newTask = req.body;
  console.log(newTask);

  try {
    const data = await fs.readFile(tasksFilePath, "utf-8");
    const tasks = JSON.parse(data);
    console.log(tasks);
    tasks.push(newTask);
    console.log(tasks);
    await fs.writeFile(tasksFilePath, JSON.stringify(tasks, null, 2));
    res.status(201).json(newTask);
  } catch (error) {
    console.error("Error writing tasks:", error.message);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

router.put("/:id", async (req, res) => {
  const taskId = req.params.id;
  const updatedTaskData = req.body;

  try {
    const data = await fs.readFile(tasksFilePath, "utf-8");
    let tasks = JSON.parse(data);
    const taskIndex = (taskId - 1);
    if (taskIndex >= tasks.length) {
      res.status(404).json({ error: "Task not found" });
      return;
    }
    tasks[taskIndex] = { ...tasks[taskIndex], ...updatedTaskData };
    
    await fs.writeFile(tasksFilePath, JSON.stringify(tasks, null, 2));
    res.json(tasks[taskIndex]);
  } catch (error) {
    console.error("Error writing tasks:", error.message);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

router.delete("/:id", async (req, res) => {
  const taskId = req.params.id;
  try {
    const data = await fs.readFile(tasksFilePath, "utf-8");
    const taskIndex = (taskId - 1);
    let tasks = JSON.parse(data);
    tasks.splice(taskIndex, 1);
    
    await fs.writeFile(tasksFilePath, JSON.stringify(tasks, null, 2));
    res.json({ message: "Task deleted successfully" });
  } catch (error) {
    console.error("Error writing tasks:", error.message);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

export default router;
