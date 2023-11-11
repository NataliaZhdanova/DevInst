// Create another file named shop.js.

// In shop.js, require the product objects from the products.js module.

// Create a function that takes a product name as a parameter and searches for the corresponding product object.

// Call this function with different product names and print the details of the products.

// Run shop.js and verify that the correct product details are displayed.

import products from "./product.js";

function findProduct(name) {
    const product = products.find(product => product.name === name);
    return product;
}

console.log(findProduct("Coffee"));
console.log(findProduct("Chess"));
