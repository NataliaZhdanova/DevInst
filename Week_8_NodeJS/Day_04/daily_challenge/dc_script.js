// Use this Giphy API Random documentation. Use this API Key : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
// In the HTML file, add a form, containing an input and a button. This input is used to fetch gif depending on a specific category.
// In the JS file, create a program to fetch one random gif depending on the search of the user (ie. If the search is “sun”, append on the page one gif with a category of “sun”).
// The gif should be appended with a DELETE button next to it. Hint : to find the URL of the gif, look for the sub-object named “images” inside the data you receive from the API.
// Allow the user to delete a specific gif by clicking the DELETE button.
// Allow the user to remove all of the GIFs by clicking a DELETE ALL button.

const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const gifForm = document.getElementById("gifForm");
const searchInput = document.getElementById("searchInput");
const gifContainer = document.getElementById("gifContainer");
const deleteAllButton = document.getElementById("deleteAllButton");

gifForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const searchTerm = searchInput.value;
  const url = `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&tag=${searchTerm}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    const gifUrl = data.data.images.original.url;

    const gifDiv = document.createElement("div");
    const gifImg = document.createElement("img");
    const deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    gifImg.src = gifUrl;

    deleteButton.addEventListener("click", () => {
      gifContainer.removeChild(gifDiv);
    });

    gifDiv.appendChild(gifImg);
    gifDiv.appendChild(deleteButton);
    gifContainer.appendChild(gifDiv);
  } catch (error) {
    console.error("We could't fetch a gif...", error);
  }
});


deleteAllButton.addEventListener("click", () => {
  gifContainer.innerHTML = '';
});