def generate_invitations(template, attendees):
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee and Generate Output Files
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name")
        name = "N/A" if name is None else str(name)

        event_title = attendee.get("event_title")
        event_title = "N/A" if event_title is None else str(event_title)

        event_date = attendee.get("event_date")
        event_date = "N/A" if event_date is None else str(event_date)

        event_location = attendee.get("event_location")
        event_location = "N/A" if event_location is None else str(event_location)

        content = template
        content = content.replace("{name}", name)
        content = content.replace("{event_title}", event_title)
        content = content.replace("{event_date}", event_date)
        content = content.replace("{event_location}", event_location)

        output_filename = f"output_{index}.txt"
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(content)