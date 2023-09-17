
browser.runtime.onMessage.addListener(message => {
    console.log("Received message from cheetah.js:", message);
    
    // Sending messages remotely
    fetch('http://localhost:5000/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(message)
    })
    .then(response => response.json())
    .then(data => console.log("Remote server response:", data))
    .catch(error => console.error("Error sending data:", error));
});
