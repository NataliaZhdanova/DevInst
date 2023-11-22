const loginForm = document.getElementById("login");
const usernameLog = document.getElementById("usernameLog");
const passwordLog = document.getElementById("passwordLog");
const submitLog = document.getElementById("submitLog");
const feedback = document.getElementById("feedback");


const checkInputs = () => {
    const anyInputEmpty = !usernameLog.value || !passwordLog.value;
    submitLog.disabled = anyInputEmpty;
};

usernameLog.addEventListener("input", checkInputs);
passwordLog.addEventListener("input", checkInputs);

loginForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    const username = usernameLog.value;
    const password = passwordLog.value;
    let json = { username, password };
    try {
        const response = await fetch("/login", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(json),
        });

        if (response.ok) {
            feedback.innerHTML = "<p>Authentication successful!</p>";
        } else {
            feedback.innerHTML = "<p>Authentication failed. Please try again.</p>";
        }
    } catch (error) {
        console.error("Error during authentication:", error.message);
        feedback.innerHTML = "<p>Authentication failed. Please try again.</p>";
    }
});