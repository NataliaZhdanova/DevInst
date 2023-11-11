// The program should take the currency which the user currently has and the currency in which they would like to receive, as well as the amount of money. 
// Afterwards, the program will output the correct exchange rate based on the data from the APIs.

// First, you need to fetch all the supported currencies, in order to add the currencies options (ie FROM - To) in the currency converter. 
// Check out this page on Supported Codes Endpoint from the ExchangeRate API documentation.

// To convert from a currency, to another one, you need to fetch conversion rate from the Pair Conversion API endpoint. Check out this page on Pair conversion requests from the ExchangeRate API documentation.
// Hint: You could also supply an optional AMOUNT variable in the query of the request.

// Bonus: Add this “switch” button on the page, when clicked on it will switch the currencies and display the new amount converted.
// Example : if the conversion was from EUR to GBP, as soon as the button is clicked on, the conversion should be from GBP to EUR.

const fromCurr = document.getElementById("fromCurrency");
const toCurr = document.getElementById("toCurrency");
const amount = document.getElementById("amount");
const convertCurr = document.getElementById("convertBtn");
const switchCurr = document.getElementById("switchBtn");
const resultDisplay = document.getElementById("result");

const apiKey = "f4c85fedf933ae628bd36ebd";

async function fetchCurrencies() {
  const response = await fetch(`https://open.er-api.com/v6/latest`);
  const data = await response.json();
  const currencies = Object.keys(data.rates);

  currencies.forEach(currency => {
    const ddListCurr1 = document.createElement("option");
    const ddListCurr2 = document.createElement("option");
    ddListCurr1.value = ddListCurr2.value = currency;
    ddListCurr1.textContent = ddListCurr2.textContent = currency;
    fromCurr.appendChild(ddListCurr1);
    toCurr.appendChild(ddListCurr2);
  });
}

fetchCurrencies();

async function convertCurrency() {

  const fromCurrency = fromCurr.value;
  const toCurrency = toCurr.value;
  const money = Number(amount.value);
 
  const response = await fetch(`https://v6.exchangerate-api.com/v6/${apiKey}/pair/${fromCurrency}/${toCurrency}/${money}`);
  const data = await response.json();
  const result = data.conversion_result.toFixed(2);

  resultDisplay.innerHTML = `<p>Converted Amount: ${result} ${toCurrency}</p>`;
}


convertCurr.addEventListener("click", convertCurrency);
switchCurr.addEventListener("click", () => {
  const temp = fromCurr.value;
  fromCurr.value = toCurr.value;
  toCurr.value = temp;
});


