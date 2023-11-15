// Inside the crud-api directory, create a new directory named data.

// Inside the data directory, create a new file named dataService.js.
// In dataService.js, import the axios module and create a function named fetchPosts that makes a GET 
// request to the JSONPlaceholder API to fetch data for all posts.
// Export the fetchPosts function.

import axios from "axios";

const fetchPosts = async () => {
  try {
    const response = await axios.get("https://jsonplaceholder.typicode.com/posts");
    return response.data;
  } catch (error) {
    console.error("Cannot fetch posts:", error.message);
    throw error;
  }
};


module.exports.fetchPosts = fetchPosts;