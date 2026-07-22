def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    student_name = input("Student Name: ").strip()
    student_id = input("Student ID: ").strip()
    issue = input("Issue: ").strip()
    location = input("Location: ").strip()
    priority = input("Priority (High/Medium/Low): ").strip().capitalize()

    # Assign technician based on priority level
    if priority == "High":
        technician = "Mosleh"
    elif priority == "Medium":
        technician = "Siti"
    elif priority == "Low":
        technician = "Saleh"
    else:
        technician = "Unassigned"

    status = "Pending"

    return {
        "student_name": student_name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": status
    }