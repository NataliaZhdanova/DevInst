// 1. Create 2 HTML files: one for the Login form and the other for the Register form 
//(when the inputs are empty the submit button should be disabled).
// 2. Set up a new Express.js application.
// 3. Implement the following routes using express.Router:

// POST /register: Allow users to register by providing a username and password. Hash the password using bcrypt before storing it in the JSON file.
// POST /login: Allow users to login by providing their username and password. Compare the hashed password from the JSON file with the provided password.
// GET /users: Retrieve a list of all registered users from a JSON file (only for demonstration purposes; no authentication required).
// GET /users/:id: Retrieve a specific user by ID from the JSON file (only for demonstration purposes; no authentication required).
// PUT /users/:id: Update a user’s information by ID in the JSON file (only for demonstration purposes; no authentication required).

// 5. Use bcrypt to hash user passwords before storing them in the JSON file and for verifying passwords during login.
// 6. Implement error handling for file read/write operations, route validation, and incorrect login credentials.

const registerForm = document.getElementById("register");
const usernameReg = document.getElementById("usernameReg");
const passwordReg = document.getElementById("passwordReg");
const submitReg = document.getElementById("submitReg");
const feedback = document.getElementById("feedback");


const checkInputs = () => {
    const anyInputEmpty = !usernameReg.value || !passwordReg.value;
    submitReg.disabled = anyInputEmpty;
};

usernameReg.addEventListener("input", checkInputs);
passwordReg.addEventListener("input", checkInputs);

registerForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    const username = usernameReg.value;
    const password = passwordReg.value;
    let json = { username, password };
    try {
        const response = await fetch("/register", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(json),
        });

        if (response.ok) {
            feedback.innerHTML = "<p>Registration successful!</p>";
        } else {
            feedback.innerHTML = "<p>Registration failed. Please try again.</p>";
        }
    } catch (error) {
        console.error("Error during registration:", error.message);
        feedback.innerHTML = "<p>Registration failed. Please try again.</p>";
    }
});