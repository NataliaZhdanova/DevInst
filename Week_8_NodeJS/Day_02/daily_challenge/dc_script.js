// Instructions
// Create a form with two fields (name, last name) and a submit button.
// When you click the Send button, retrieve the data from the inputs, and append it on the DOM as a JSON string.


const form = document.getElementById("myForm");
const resul = document.getElementById("result");

form.addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => data[key] = value);
    const jsonOutput = JSON.stringify(data);
    result.innerText = jsonOutput;
    });