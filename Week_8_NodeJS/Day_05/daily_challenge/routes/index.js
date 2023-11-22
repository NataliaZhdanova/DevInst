import express from "express";
const router = express.Router();
import bcrypt from "bcrypt";
import { promises as fs } from "fs";
import path from "path";
import bodyParser from "body-parser";
import { fileURLToPath } from "url";
import { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

router.use(bodyParser.json());

router.use(express.static(path.join(__dirname, "public")));

const usersFilePath = path.join(__dirname, "../data/users.json");

router.get("/users", async (req, res) => {
    try {
        const data = await fs.readFile(usersFilePath, "utf-8");
        const users = JSON.parse(data);
        res.status(200).json(users);
        
    } catch (error) {
        console.error("Error getting users:", error.message);
        res.status(500).json({ error: "Internal Server Error" });
    }

});

router.get("/register", (req, res) => {
    res.sendFile(path.join(__dirname, "../register.html"));
});
router.get("/login", (req, res) => {
    res.sendFile(path.join(__dirname, "../login.html"));
});

router.get("/users/:id", async (req, res) => {
  const userId = req.params.id;
  const userIndex = (userId - 1);
  try {
    const data = await fs.readFile(usersFilePath, "utf-8");
    const users = JSON.parse(data);
    const user = users[userIndex];

    if (user) {
        res.status(200).json(user);
    } else {
        res.status(404).json({ error: "User not found" });
    }    
  } catch (error) {
        console.error("Error getting user:", error.message);
        res.status(500).json({ error: "Internal Server Error" });
  }
});

router.put("/users/:id", async (req, res) => {
    const userId = req.params.id;
    const { username, password } = req.body;

    try {
        const data = await fs.readFile(usersFilePath, "utf-8");
        const users = JSON.parse(data);
        const userIndex = (userId - 1);
        const hashedPassword = await bcrypt.hash(password, 10);

        if (userIndex < users.length) {
            users[userIndex] = { ...users[userIndex], username, password: hashedPassword };
            await fs.writeFile(usersFilePath, JSON.stringify(users, null, 2));

            res.status(200).json({ message: "User updated successfully" });
        } else {
            res.status(404).json({ error: "User not found" });
        }    
    } catch (error) {
          console.error("Error updating user:", error.message);
          res.status(500).json({ error: "Internal Server Error" });
    }
  });

router.post("/register", async (req, res) => {
    const { username, password } = req.body;

    try {
        const data = await fs.readFile(usersFilePath, "utf-8");
        const users = JSON.parse(data);

        if (users.find(user => user.username === username)) {
            return res.status(400).json({ error: "Username already exists" });
        }

        const hashedPassword = await bcrypt.hash(password, 10);

        users.push({ username, password: hashedPassword });

        await fs.writeFile(usersFilePath, JSON.stringify(users, null, 2));

        res.status(201).json({ message: "User registered successfully" });
    } catch (error) {
        console.error("Error registering user:", error.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
});

router.post("/login", async (req, res) => {
    const { username, password } = req.body;

    try {
        const data = await fs.readFile(usersFilePath, "utf-8");
        const users = JSON.parse(data);

        const user = users.find(user => user.username === username);
        if (!user) {
            return res.status(401).json({ error: "Invalid credentials" });
        }
        const passwordMatch = await bcrypt.compare(password, user.password);

        if (passwordMatch) {
            res.status(200).json({ message: "Login successful" });
        } else {
            res.status(401).json({ error: "Invalid credentials" });
        }
    } catch (error) {
        console.error("Error logging in:", error.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
});

export default router;