// Create A Trivia Quiz Game With Express.Js And Express.Router
// Instructions
// 1. Set up a new Express.js application.
// 2. Create a trivia quiz model with a set of hard-coded questions and answers.
// 3. Implement the following routes using express.Router:

// GET /quiz: Start the quiz and display the first question.
// POST /quiz: Submit an answer to the current question and move to the next question.
// GET /quiz/score: Display the user’s final score at the end of the quiz.
// 4. Keep track of the user’s score as they progress through the quiz.
// 5. Provide appropriate feedback on correct and incorrect answers.
// 6. Implement simple game logic such as displaying the next question after answering one.


import express from "express";
import router from "./routes/index.js";

const app = express();
const port = 9000;

app.use(express.static("public"));

app.use(express.json());

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });

app.use("/quiz", router);


