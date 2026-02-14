from datetime import datetime

def send_appointment_confirmation(appointment_data):
    """Simulate appointment confirmation"""
    print("\n" + "="*60)
    print("🔔 AUTOMATION TRIGGERED: Appointment Confirmation")
    print("="*60)
    print(f"📧 To: {appointment_data['email']}")
    print(f"👤 Patient: {appointment_data['patient_name']}")
    print(f"📅 Appointment: {appointment_data['appointment_type']}")
    print(f"🕐 Date & Time: {appointment_data['date']} at {appointment_data['time']}")
    print(f"👨‍⚕️ Doctor: {appointment_data['doctor']}")
    print(f"✉️ Message: 'Your appointment has been confirmed. See you soon!'")
    print("="*60 + "\n")
    return True

def send_welcome_message(patient_data):
    """Simulate welcome message to new patient"""
    print("\n" + "="*60)
    print("🔔 AUTOMATION TRIGGERED: Welcome Message")
    print("="*60)
    print(f"📧 To: {patient_data['email']}")
    print(f"👤 Name: {patient_data['name']}")
    print(f"✉️ Message: 'Thank you for contacting MedFlow Clinic!'")
    print(f"📱 We'll respond to your inquiry within 24 hours.")
    print("="*60 + "\n")
    return True

def send_appointment_reminder(appointment_data):
    """Simulate appointment reminder"""
    print("\n" + "="*60)
    print("🔔 AUTOMATION TRIGGERED: Appointment Reminder")
    print("="*60)
    print(f"📧 To: {appointment_data['email']}")
    print(f"👤 Patient: {appointment_data['patient_name']}")
    print(f"📅 Reminder: Your appointment is on {appointment_data['date']} at {appointment_data['time']}")
    print(f"✉️ Message: 'Please arrive 15 minutes early.'")
    print("="*60 + "\n")
    return True

def check_inventory_alert(item_name, quantity, threshold):
    """Check and alert for low inventory"""
    if quantity < threshold:
        print("\n" + "="*60)
        print("🚨 AUTOMATION TRIGGERED: Low Inventory Alert")
        print("="*60)
        print(f"📦 Item: {item_name}")
        print(f"📊 Current Stock: {quantity}")
        print(f"⚠️ Minimum Required: {threshold}")
        print(f"🔴 Status: REORDER NEEDED")
        print("="*60 + "\n")
        return True
    return False

def notify_staff_new_appointment(appointment_data):
    """Notify staff about new appointment"""
    print("\n" + "="*60)
    print("🔔 AUTOMATION TRIGGERED: Staff Notification")
    print("="*60)
    print(f"👨‍⚕️ To: Dr. {appointment_data['doctor']}")
    print(f"📋 New Appointment: {appointment_data['patient_name']}")
    print(f"🕐 Scheduled: {appointment_data['date']} at {appointment_data['time']}")
    print(f"📝 Type: {appointment_data['appointment_type']}")
    print("="*60 + "\n")
    return True