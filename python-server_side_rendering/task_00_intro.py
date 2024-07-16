import os

def generate_invitations(template, attendees):
    # Check input
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return
    
    # Handle template gives error msg for empty ones.
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    
    # error if attendee empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    #creates the attendee
    for idx, attendee in enumerate(attendees, start=1):
        output_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") if attendee.get(key) is not None else "N/A"
            output_content = output_content.replace(f"{{{key}}}", value)
        
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
        print(f"Generated {output_filename}")

# test file
if __name__ == "__main__":
    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
