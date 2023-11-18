document.addEventListener("DOMContentLoaded", () => {
    const questionText = document.getElementById("question");
    const answerForm = document.getElementById("answer-form");
    const feedback = document.getElementById("feedback");
    const scoreDisplay = document.getElementById("score");
  
    loadNewQuestion();
  
    answerForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const formData = new FormData(event.target);
      const userGuess = formData.get("answer");
      const correctGuess = await checkGuess(userGuess);
      displayFeedback(correctGuess);
      loadNewQuestion();
    });
    
    async function loadNewQuestion() {
      const response = await fetch("/quiz");
      const { question, answer } = await response.json();
      questionText.textContent = question;
      questionText.id = answer;
      updateOptions();
    }
 
    async function checkGuess(userGuess) {
      const response = await fetch("/quiz", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answer: userGuess, correctAnswer: questionText.id }),
      });
      const { correct, userScore } = await response.json();
      updateScore(userScore);
      return correct;
    }

    function updateOptions() {
      const input = document.createElement("input");
      input.name = "answer";
      answerForm.innerHTML = '<label for="answer">Your Answer:</label>';
      answerForm.appendChild(input);
      answerForm.innerHTML += '<button type="submit">Submit</button>';
      }
  
    function displayFeedback(correct) {
      feedback.textContent = correct ? "Correct!" : "Incorrect. Try again!";
    }
  
    function updateScore(userScore) {
      scoreDisplay.textContent = `Score: ${userScore}`;
    }
});
  