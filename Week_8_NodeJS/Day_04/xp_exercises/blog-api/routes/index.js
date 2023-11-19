import express from "express";
const router = express.Router();
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

router.get("/", (req, res) => {
    try {
        db
        .select("*").from("posts")
        .then(posts =>
                res.send(posts)
        )
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal Server Error' });
    }

});

router.get("/:id", (req, res) => {
  const postId = req.params.id;
  try {
    db("posts")
    .where({id: postId})
    .then(posts =>
                res.send(posts)
        )
  } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post("/", (req, res) => {
  const { title, content } = req.body;
  try {
    db("posts")
    .insert({ title: title, content: content }, ["title", "content"])
    .then(posts =>
        res.send(posts)
    )
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.put("/:id", (req, res) => {
  const postId = req.params.id;
  const { title, content } = req.body;
  try {
  db("posts")
        .where("id", postId)
        .update({
            title: title,
            content: content
        },
            ["id", "title", "content"])
        .then(posts =>
            res.send(posts)
        )
  } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.delete("/:id", (req, res) => {
  const postId = req.params.id;
  try {
  db("posts")
        .where("id", postId)
        .del(["id", "title", "content"])
        .then(posts =>
            res.send(posts)
        )
  } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal Server Error' });
  }
});

export default router;