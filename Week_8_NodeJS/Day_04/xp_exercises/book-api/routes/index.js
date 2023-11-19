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
        .select("*").from("books")
        .then(books =>
                res.status(200).send(books)
        )
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal Server Error' });
    }

});

router.get("/:id", (req, res) => {
  const bookId = req.params.id;
  try {
    db("books")
    .where({id: bookId})
    .then(books =>
                res.status(200).send(books)
        )
  } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post("/", (req, res) => {
  const { title, author, publishedYear } = req.body;
  console.log(req.body);
  try {
    db("books")
    .insert({ title: title, author: author, publishedyear: publishedYear }, ["title", "author", "publishedyear"])
    .then(books =>
        res.status(201).send(books)
    )
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

export default router;