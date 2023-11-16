document.addEventListener("DOMContentLoaded", () => {
    const emojiDisplay = document.getElementById("emoji-display");
    const guessForm = document.getElementById("guess-form");
    const feedback = document.getElementById("feedback");
    const scoreDisplay = document.getElementById("score");
  
    loadNewEmoji();
  
    guessForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const formData = new FormData(event.target);
      const userGuess = formData.get("guess");
      const correctGuess = await checkGuess(userGuess);
      displayFeedback(correctGuess);
      loadNewEmoji();
    });
    
    async function loadNewEmoji() {
      const response = await fetch("/api/emoji");
      const { emoji, name, options } = await response.json();
      emojiDisplay.textContent = emoji;
      emojiDisplay.id = name;
      updateOptions(options);
    }
 
    async function checkGuess(userGuess) {
      const response = await fetch("/api/guess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ guess: userGuess, correctGuess: emojiDisplay.id }),
      });
      const { correct, score } = await response.json();
      updateScore(score);
      return correct;
    }
  
    function displayFeedback(correct) {
      feedback.textContent = correct ? "Correct!" : "Incorrect. Try again!";
    }
  
    function updateOptions(options) {
      const select = document.createElement("select");
      select.name = "guess";
      
      options.forEach((option) => {
        const optionElement = document.createElement("option");
        optionElement.value = option;
        optionElement.text = option;
        select.appendChild(optionElement);
      });
      
      guessForm.innerHTML = "";
      guessForm.appendChild(select);
      guessForm.innerHTML += '<button type="submit">Submit</button>';
    }
  
    function updateScore(score) {
      scoreDisplay.textContent = `Score: ${score}`;
    }
});
  