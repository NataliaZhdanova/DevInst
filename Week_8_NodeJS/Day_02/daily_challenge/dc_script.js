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
  
  app.get('/api/emoji', (req, res) => {
    const randomEmoji = getRandomEmoji();
    const distractors = getDistractors(randomEmoji.name);
    res.json({ emoji: randomEmoji.emoji, options: shuffleOptions([...distractors, randomEmoji.name]) });
  });
  
  app.post('/api/guess', express.json(), (req, res) => {
    const userGuess = req.body.guess;
    const correctGuess = req.body.correctGuess;
    
    if (userGuess === correctGuess) {
      score += 1;
      res.json({ correct: true, score });
    } else {
      res.json({ correct: false, score });
    }
  });
  
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
  
  function getRandomEmoji() {
    return emojis[Math.floor(Math.random() * emojis.length)];
  }
  
  function getDistractors(correctAnswer) {
    const allEmojiNames = emojis.map(e => e.name);
    const distractors = allEmojiNames.filter(name => name !== correctAnswer);
    return distractors.slice(0, 2); // Select 2 distractors
  }
  
  function shuffleOptions(options) {
    for (let i = options.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [options[i], options[j]] = [options[j], options[i]];
    }
    return options;
  }