// main.js

// 1. Auto-hide flash messages
document.addEventListener("DOMContentLoaded", () => {
    const flashMessages = document.querySelectorAll(".flash-message");
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = "0";
            setTimeout(() => msg.remove(), 600);  // Fully remove after fade-out
        }, 4000); // Display duration
    });
});

// 2. Confirm before deleting (used in delete buttons)
const deleteButtons = document.querySelectorAll(".delete-button");
deleteButtons.forEach(button => {
    button.addEventListener("click", function (e) {
        const confirmed = confirm("Are you sure you want to delete this item?");
        if (!confirmed) {
            e.preventDefault();
        }
    });
});

// 3. Show/hide password toggle (for login/register)
const togglePassword = document.querySelectorAll(".toggle-password");
togglePassword.forEach(icon => {
    icon.addEventListener("click", () => {
        const input = document.getElementById(icon.dataset.target);
        if (input.type === "password") {
            input.type = "text";
            icon.innerText = "🙈";
        } else {
            input.type = "password";
            icon.innerText = "👁️";
        }
    });
});
