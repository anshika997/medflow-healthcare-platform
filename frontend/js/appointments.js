const API_URL = 'http://localhost:8000/api';

// Set minimum date to today
document.querySelector('input[name="date"]').min = new Date().toISOString().split('T')[0];

document.getElementById('appointmentForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    
    try {
        const response = await fetch(`${API_URL}/appointments`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        document.getElementById('message').innerHTML = `
            <div class="message-box alert-success">
                ✅ ${result.message}<br>
                📧 ${result.automation}<br>
                🔔 You will receive a reminder before your appointment
            </div>
        `;
        
        e.target.reset();
        
        // Scroll to message
        document.getElementById('message').scrollIntoView({ behavior: 'smooth' });
        
    } catch (error) {
        document.getElementById('message').innerHTML = `
            <div class="message-box alert-danger">
                ❌ Error booking appointment. Please try again.
            </div>
        `;
    }
});