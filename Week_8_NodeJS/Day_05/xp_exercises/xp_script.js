// Instructions
// You should use this API: https://www.swapi.tech/ to get the data and update it “randomly” in your website by clicking a button.
// Note: The API contains 83 different characters

// Create your HTML file, and add the relevant elements.

// In your JS file, create your functions :
// to retrieve the elements from the DOM.
// to get the data from the API (star wars characters).
// to display the info on the DOM: the name, height, gender, birth year, and home world of the character.

// Display the data using AJAX. Make sure to display a loading message as follows:
// You can use any of these animation icons for the loading message.
// Fontawesome link :
// https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css

// 4. If there is an error getting the data, display a message as follows:
// 5. You can use your own css to style the website as you see fit

const text = document.getElementById("text");
const btn = document.getElementById("find");

async function fetchData() {
  try {
      let randNum = Math.floor(Math.random() * 83)    
      const response = await fetch(`https://www.swapi.tech/api/people/${randNum}/`);
      const data = await response.json();
      const message = data.message;
      if (message != "ok") {
        text.innerHTML = `<p>Oh, no! That hero is not available!</p>`
      }
      return data;
  } catch (error) {
    console.error("Error fetching char data:", error);
  }
}

async function fetchPlanet(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    const homeworld = data.result.properties.name;
    return homeworld;
  } catch (error) {
    console.error("Error fetching planetr data:", error);
  }
}

async function displayDetails(data) {
  const properties = data.result.properties
  const { name, height, gender, birth_year, homeworld, skin_color, eye_color} = properties;
  let homePlanet = await fetchPlanet(homeworld);
  text.innerHTML = `
      <h2>${name}</h2><br>
      <p>Birth Year: ${birth_year}</p>
      <p>Gender: ${gender}</p>
      <p>Height: ${height}</p>    
      <p>Homeworld: ${homePlanet}</p>
      <p>Skin color: ${skin_color }</p>
      <p>Eye color: ${eye_color }</p>
    `;
   }

btn.addEventListener("click", async (event) => {
  event.preventDefault();
  try {
    const data = await fetchData();
    displayDetails(data);
  } catch (error) {
    console.error('Error:', error);    
  }
})
