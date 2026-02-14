const API_URL = 'http://localhost:8000/api';

document.getElementById('contactForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    
    try {
        const response = await fetch(`${API_URL}/patients`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        document.getElementById('message').innerHTML = `
            <div class="message-box alert-success">
                ✅ ${result.message}<br>
                📧 ${result.automation}<br>
                💬 We'll respond to your inquiry within 24 hours
            </div>
        `;
        
        e.target.reset();
        
    } catch (error) {
        document.getElementById('message').innerHTML = `
            <div class="message-box alert-danger">
                ❌ Error sending message. Please try again.
            </div>
        `;
    }
});