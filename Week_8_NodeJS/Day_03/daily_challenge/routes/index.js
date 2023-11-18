import express from "express";
const router = express.Router();

const triviaQuestions = [
  {
    question: "What is the capital of France?",
    answer: "Paris",
  },
  {
    question: "Which planet is known as the Red Planet?",
    answer: "Mars",
  },
  {
    question: "What is the largest mammal in the world?",
    answer: "Blue whale",
  },
];

let currentQIndex = 0;
let userScore = 0;

router.get("/", (req, res) => {
  if (currentQIndex < triviaQuestions.length) {
    const currentQuestion = triviaQuestions[currentQIndex].question;
    const currentAnswer = triviaQuestions[currentQIndex].answer;
    res.json({ question: currentQuestion, answer: currentAnswer});
  } else {
    res.json({ question: "Quiz completed!", answer: "completed"});
  }
});

router.post("/", express.json(), (req, res) => {
  const userAnswer = req.body.answer;
  const correctAnswer = req.body.correctAnswer;
  if (userAnswer === correctAnswer) {
    userScore++;
    res.json({ correct: true, userScore });
    } else {
      res.json({ correct: false, userScore });
    }
  currentQIndex++;
});

export default router;