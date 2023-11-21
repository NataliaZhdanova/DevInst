import express from "express";
const router = express.Router();
import bcrypt from "bcrypt";
import bodyParser from "body-parser";
import knex from "knex";

const db = knex({
  client: "pg",
  connection: {
    host: "127.0.0.1",
    user: "postgres",
    password: "postgres",
    database: "study",
    port: 5432
  }
});

router.use(bodyParser.json());

router.get("/users", (req, res) => {
    try {
        db
        .select("*").from("users")
        .then(users =>
                res.status(200).send(users)
        )
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: "Internal Server Error" });
    }

});

router.get("/users/:id", (req, res) => {
  const userId = req.params.id;
  try {
    db("users")
    .where({id: userId})
    .then(users =>
                res.status(200).send(users)
        )
  } catch (err) {
        console.error(err);
        res.status(500).json({ error: "Internal Server Error" });
  }
});

router.put("/users/:id", (req, res) => {
    const userId = req.params.id;
    const { email, username, first_name, last_name } = req.body;
    try {
    db("users")
          .where("id", userId)
          .update({
              email: email,
              username: username,
              first_name: first_name,
              last_name: last_name
          },
              ["id", "email", "username", "first_name", "last_name"])
          .then(users =>
              res.send(users)
          )
    } catch (err) {
          console.error(err);
          res.status(500).json({ error: "Internal Server Error" });
    }
  });

router.post("/register", async (req, res) => {
    try {
      const { email, username, password, first_name, last_name } = req.body;
      const exists = await db.select("username").from("users").where("username", "=", username);
  
      if (exists.length > 0) {
        return res.status(400).json({ error: "Username already exists" });
      }
  
      const hashedPassword = await bcrypt.hash(password, 10);
  
      // Store user in the database
      await db("users").insert({ email, username, first_name, last_name });
      await db("hashpwd").insert({ username, password: hashedPassword });
  
      res.status(201).json({ message: "Registration successful" });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: "Internal Server Error" });
    }
  });


router.post("/login", async (req, res) => {
    try {
        const { username, password } = req.body;
        const exists = await db.select("username").from("hashpwd").where("username", "=", username);
        const hashedPassword = await db.select("password").from("hashpwd").where("username", "=", username);
        if (exists.length == 0) {
            return res.status(401).json({ error: "Invalid credentials" });
        }
        console.log(password);
        console.log(hashedPassword[0].password);
        const passwordMatch = await bcrypt.compare(password, hashedPassword[0].password);

        if (passwordMatch) {
        res.status(200).json({ message: "Login successful" });
        } else {
        res.status(401).json({ error: "Invalid credentials" });
        }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

export default router;