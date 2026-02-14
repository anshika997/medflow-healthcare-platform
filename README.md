# 🏥 MedFlow - Healthcare Operations Platform

A unified platform for managing clinic operations including appointments, patients, inventory, and staff with intelligent automation.

![MedFlow Dashboard](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)

## 🌟 Features

- 📅 **Smart Appointment Booking** - Patients can book appointments with automated confirmations
- 👥 **Patient Management** - Track patient inquiries and communications
- 📊 **Real-Time Dashboard** - Monitor clinic operations with live statistics
- 📦 **Inventory Tracking** - Automatic alerts for low medical supplies
- 🔔 **Smart Automation** - Auto-send confirmations, reminders, and notifications
- 👨‍⚕️ **Staff Management** - Coordinate team workflows efficiently

## 🚀 Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** MongoDB
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Automation:** Custom Python automation engine

## 📸 Screenshots

### Dashboard
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### Appointment Booking
![Booking](https://via.placeholder.com/800x400?text=Booking+Screenshot)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11+
- MongoDB (local or cloud)

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend runs on `http://localhost:8000`

### Frontend Setup
```bash
cd frontend
python -m http.server 3000
```

Frontend runs on `http://localhost:3000`

## 🎯 Key Automation Features

When actions occur, the system automatically:
- ✅ Sends appointment confirmations via email
- ✅ Sends welcome messages to new patients
- ✅ Sends appointment reminders
- ✅ Alerts staff about new appointments
- ✅ Notifies about low inventory levels

All automation triggers are logged in real-time in the backend console.

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/appointments` | Create new appointment |
| GET | `/api/appointments` | Get all appointments |
| POST | `/api/patients` | Create patient inquiry |
| GET | `/api/dashboard/stats` | Get dashboard statistics |
| POST | `/api/inventory` | Add inventory item |
| GET | `/api/inventory/alerts` | Get low stock alerts |

## 🎥 Demo Flow

1. **Setup** - Configure clinic settings
2. **Book Appointment** - Fill form → See automation in terminal
3. **Contact Form** - Send inquiry → See welcome message automation
4. **Dashboard** - View real-time statistics
5. **Staff Panel** - Manage appointments
6. **Inventory** - Add items → See low stock alerts

## 🏆 Built For

CareOps Healthcare Operations Hackathon 2025

## 👤 Author

**Anshika**
- GitHub: [Anshika Singh ](https://github.com/anshika997)

## 📄 License

MIT License - feel free to use this project for learning and development.

---

⭐ If you find this project useful, please consider giving it a star!