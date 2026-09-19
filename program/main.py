print("======================================")
print(" ONLINE ID PRODUCTION APPOINTMENT")
print("======================================")

name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
date = input("Enter appointment date: ")
time = input("Enter appointment time: ")

appointment = {
    "Name": name,
    "Student ID": student_id,
    "Date": date,
    "Time": time,
    "Status": "Confirmed"
}

print("\n======================================")
print("        APPOINTMENT CONFIRMED")
print("======================================")

for key, value in appointment.items():
    print(f"{key}: {value}")

print("\nPlease arrive 10 minutes before your appointment.")
