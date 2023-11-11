// 🌟 Exercise 1 : Comparison
// Instructions
// Create a function called compareToTen(num) that takes a number as an argument.
// The function should return a Promise:
// the promise resolves if the argument is less than or equal to 10
// the promise rejects if argument is greater than 10.

function compareToTen(num) {
    let prom = new Promise((resolve, reject) => {
        if (num <= 10) {
            resolve(`${num} is less than or equal to 10`);
        } else {
            reject(`${num} is greater than 10`);
        }
    });
    prom.then(value => {
        console.log("OK: " + value );
    })
    .catch(error => console.error("Error: " + error));
}

compareToTen(9);
compareToTen(20);


// 🌟 Exercise 2 : Promises
// Instructions
// Create a promise that resolves itself in 4 seconds and returns a “success” string.

let prom1 = new Promise((resolve, reject) => {
    setTimeout(resolve => console.log("Success..."), 4000);
})

// 🌟 Exercise 3 : Resolve & Reject
// Instructions
// Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.
// Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”

const promise1 = Promise.resolve(3);
const promise2 = Promise.reject("Boo!");

// promise1.then(value => {
//   console.log("Promise resolved with value:", value);
// }).catch(error => {
//   console.error("Error occurred:", error);
// });

// promise2.then(value => {
//   console.log("Promise resolved with value:", value);
// }).catch(error => {
//   console.error("Error occurred:", error);
// });

