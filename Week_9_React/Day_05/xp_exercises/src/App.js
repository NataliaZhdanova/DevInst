import { useState, useEffect } from "react";
import quotes from "./QuotesDatabase";

function getRandomColor() {
// Generate a random hex color code
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let index = 0; index < 6; index++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
};

let newColor = getRandomColor();

function App() {
  const [quote, setQuote] = useState({});
  const [backgroundColor, setBackgroundColor] = useState(newColor);
  const [quoteColor, setQuoteColor] = useState(newColor);
  const [buttonColor, setButtonColor] = useState(newColor);

  function generateRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    setQuote(quotes[randomIndex]);

    newColor = getRandomColor();

    setBackgroundColor(newColor);
    setQuoteColor(newColor);
    setButtonColor(newColor);
  };

   useEffect(() => {
    generateRandomQuote();
  }, []);

  return (
    <div style={{ backgroundColor: backgroundColor, padding: "20px" }}>
        <div style={{ backgroundColor: "white", padding: "20px", borderRadius: "20px" }}>
          <h1 style={{ color: quoteColor }}>{quote.quote}</h1>
          <p style={{ color: quoteColor }}>-{quote.author}-</p>
          <button style={{ backgroundColor: buttonColor, color: "white", borderRadius: "5px", border: "none", padding: "10px" }} onClick={generateRandomQuote}>
            New quote
          </button>
        </div>
    </div>
  );
};

export default App;

