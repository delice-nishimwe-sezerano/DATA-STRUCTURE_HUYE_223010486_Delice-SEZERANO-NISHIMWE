# Q.68

class VolunteerManagementSystem:
    def __init__(stud):
        stud.signup_stack = []   
        stud.pending_queue = []   
        stud.available_projects = []  

    # Stack operations
    def sign_up(stud, volunteer, project):
        stud.signup_stack.append((volunteer, project))

    def undo_sign_up(stud):
        if stud.signup_stack:
            return stud.signup_stack.pop()
        return None

    # Queue operations
    def apply(stud, volunteer):
        stud.pending_queue.append(volunteer)

    def process_application(stud):
        if stud.pending_queue:
            return stud.pending_queue.pop(0)
        return None

    # List operations
    def add_project(stud, project):
        stud.available_projects.append(project)

    def remove_project(stud, project):
        if project in stud.available_projects:
            stud.available_projects.remove(project)

    def list_projects(stud):
        return stud.available_projects
    
    
vms = VolunteerManagementSystem()

# Add available projects
vms.add_project("Beach Cleanup")
vms.add_project("Food Bank Volunteer")
vms.add_project("Community Garden")
print("Available Projects:", vms.list_projects())

# Volunteer signs up for a project
vms.sign_up("David", "Beach Cleanup")
vms.sign_up("Delice", "Food Bank Volunteer")
print("Sign-up Stack after sign-ups:", vms.signup_stack)

# Undo the last sign-up
undone_signup = vms.undo_sign_up()
print("Undone Sign-up:", undone_signup)
print("Sign-up Stack after undoing:", vms.signup_stack)

# Apply for a volunteer position
vms.apply("Hana")
vms.apply("Danny")
print("Pending Applications:", vms.pending_queue)

# Process the first application
processed_application = vms.process_application()
print("Processed Application:", processed_application)
print("Pending Applications after processing:", vms.pending_queue)

# Remove a project
vms.remove_project("Food Bank Volunteer")
print("Available Projects after removal:", vms.list_projects())

