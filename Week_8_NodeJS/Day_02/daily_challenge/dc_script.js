import express from "express";
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static("public"));

app.listen(PORT, () => {
  console.log(`The server is running on http://localhost:${PORT}`);
});

const emojis = [
    { emoji: '😀', name: 'Smile' },
    { emoji: '🐶', name: 'Dog' },
    { emoji: '🌮', name: 'Taco' },
  ];
  
  let score = 0;
  
  app.get("/api/emoji", (req, res) => {
    const randomEmoji = getRandomEmoji();
    const distractors = getDistractors(randomEmoji.name);
    res.json({ emoji: randomEmoji.emoji, name: randomEmoji.name, options: shuffleOptions([...distractors, randomEmoji.name]) });
  });
  
  app.post("/api/guess", express.json(), (req, res) => {
    const userGuess = req.body.guess;
    const correctGuess = req.body.correctGuess;
          
    if (userGuess === correctGuess) {
      score += 1;
      res.json({ correct: true, score });
    } else {
      res.json({ correct: false, score });
    }
  });
  
  function getRandomEmoji() {
    return emojis[Math.floor(Math.random() * emojis.length)];
  }
  
  function getDistractors(correctAnswer) {
    const allEmojiNames = emojis.map(e => e.name);
    const distractors = allEmojiNames.filter(name => name !== correctAnswer);
    return distractors.slice(0, 2);
  }
  
  function shuffleOptions(options) {
    for (let index = options.length - 1; index > 0; index--) {
      const j = Math.floor(Math.random() * (index + 1));
      [options[index], options[j]] = [options[j], options[index]];
    }
    return options;
  }