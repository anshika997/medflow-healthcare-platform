const API_URL = 'http://localhost:8000/api';

async function loadDashboard() {
    try {
        // Load stats
        const statsResponse = await fetch(`${API_URL}/dashboard/stats`);
        const stats = await statsResponse.json();
        
        document.getElementById('todayAppointments').textContent = stats.today_appointments;
        document.getElementById('newPatients').textContent = stats.new_patients;
        document.getElementById('pendingAppointments').textContent = stats.pending_appointments;
        document.getElementById('inventoryAlerts').textContent = stats.inventory_alerts;
        
        // Load inventory alerts
        if (stats.inventory_alerts > 0) {
            const alertsResponse = await fetch(`${API_URL}/inventory/alerts`);
            const alertsData = await alertsResponse.json();
            
            const alertsContainer = document.getElementById('alertsContainer');
            let alertsHTML = '<div class="table-container"><h3>⚠️ Inventory Alerts</h3>';
            
            alertsData.alerts.forEach(alert => {
                alertsHTML += `
                    <div class="alert alert-danger">
                        🚨 <strong>${alert.item}</strong> - Current: ${alert.current}, Required: ${alert.threshold}, Deficit: ${alert.deficit}
                    </div>
                `;
            });
            
            alertsHTML += '</div>';
            alertsContainer.innerHTML = alertsHTML;
        }
        
        // Load recent appointments
        const appointmentsResponse = await fetch(`${API_URL}/appointments`);
        const appointmentsData = await appointmentsResponse.json();
        
        const tbody = document.querySelector('#recentAppointments tbody');
        tbody.innerHTML = '';
        
        const recentAppointments = appointmentsData.appointments.slice(0, 5);
        
        if (recentAppointments.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="text-align: center; color: #6b7280;">No appointments yet</td></tr>';
        } else {
            recentAppointments.forEach(appt => {
                const row = `
                    <tr>
                        <td>${appt.patient_name}</td>
                        <td>${appt.appointment_type}</td>
                        <td>${appt.date}</td>
                        <td>${appt.time}</td>
                        <td>${appt.doctor}</td>
                        <td><span class="status-badge status-${appt.status}">${appt.status}</span></td>
                    </tr>
                `;
                tbody.innerHTML += row;
            });
        }
        
    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}

// Load dashboard on page load
loadDashboard();

// Refresh every 10 seconds
setInterval(loadDashboard, 10000);