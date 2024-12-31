document.addEventListener("DOMContentLoaded", () => {
    const statusElement = document.getElementById("status");

    async function sendCommand(command) {
        try {
            const response = await fetch("/send-command", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ command }),
            });

            const result = await response.json();
            statusElement.textContent = result.message;
            statusElement.style.color = result.status === "success" ? "green" : "red";
        } catch (error) {
            statusElement.textContent = "Error sending command!";
            statusElement.style.color = "red";
        }
    }

    document.getElementById("up").addEventListener("click", () => sendCommand("w"));
    document.getElementById("left").addEventListener("click", () => sendCommand("a"));
    document.getElementById("down").addEventListener("click", () => sendCommand("s"));
    document.getElementById("right").addEventListener("click", () => sendCommand("d"));
});
