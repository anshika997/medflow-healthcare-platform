const API_URL = 'http://localhost:8000/api';

async function loadAppointments() {
    try {
        const response = await fetch(`${API_URL}/appointments`);
        const data = await response.json();
        
        const tbody = document.querySelector('#appointmentsTable tbody');
        tbody.innerHTML = '';
        
        if (data.appointments.length === 0) {
            tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; color: #6b7280;">No appointments found</td></tr>';
            return;
        }
        
        data.appointments.forEach(appt => {
            const row = `
                <tr>
                    <td>${appt.patient_name}</td>
                    <td>${appt.appointment_type}</td>
                    <td>${appt.date}</td>
                    <td>${appt.time}</td>
                    <td>${appt.doctor}</td>
                    <td><span class="status-badge status-${appt.status}">${appt.status}</span></td>
                    <td>
                        ${appt.status === 'scheduled' ? 
                            `<button onclick="completeAppointment('${appt._id}')" class="btn btn-success btn-small">Complete</button>
                             <button onclick="cancelAppointment('${appt._id}')" class="btn btn-danger btn-small">Cancel</button>` : 
                            '<span style="color: #6b7280;">No action</span>'}
                    </td>
                </tr>
            `;
            tbody.innerHTML += row;
        });
        
    } catch (error) {
        console.error('Error loading appointments:', error);
    }
}

async function completeAppointment(id) {
    try {
        await fetch(`${API_URL}/appointments/${id}/complete`, { method: 'PUT' });
        loadAppointments();
    } catch (error) {
        console.error('Error completing appointment:', error);
    }
}

async function cancelAppointment(id) {
    if (confirm('Are you sure you want to cancel this appointment?')) {
        try {
            await fetch(`${API_URL}/appointments/${id}/cancel`, { method: 'PUT' });
            loadAppointments();
        } catch (error) {
            console.error('Error cancelling appointment:', error);
        }
    }
}

loadAppointments();
setInterval(loadAppointments, 10000);