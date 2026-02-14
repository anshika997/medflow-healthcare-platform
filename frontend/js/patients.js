const API_URL = 'http://localhost:8000/api';

async function loadPatients() {
    try {
        const response = await fetch(`${API_URL}/patients`);
        const data = await response.json();
        
        const tbody = document.querySelector('#patientsTable tbody');
        tbody.innerHTML = '';
        
        if (data.patients.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="text-align: center; color: #6b7280;">No patient inquiries yet</td></tr>';
            return;
        }
        
        data.patients.forEach(patient => {
            const date = patient.created_at ? new Date(patient.created_at).toLocaleDateString() : 'N/A';
            
            const row = `
                <tr>
                    <td>${patient.name}</td>
                    <td>${patient.phone}</td>
                    <td>${patient.email}</td>
                    <td>${patient.message.substring(0, 50)}...</td>
                    <td><span class="status-badge status-${patient.status}">${patient.status}</span></td>
                    <td>${date}</td>
                </tr>
            `;
            tbody.innerHTML += row;
        });
        
    } catch (error) {
        console.error('Error loading patients:', error);
    }
}

loadPatients();
setInterval(loadPatients, 10000);