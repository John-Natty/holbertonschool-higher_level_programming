#!/usr/bin/env python3
"""Module for generating personalized invitation files."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendee data."""

    # Check that template is a string.
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check that attendees is a list.
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return

    # Check that every attendee is a dictionary.
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Each attendee must be a dictionary.")
            return

    # Check if the template is empty.
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check if there is no data.
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # List of placeholders to replace in the template.
    template_placeholders = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    # Generate one output file for each attendee.
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        # Replace each placeholder with the attendee's value.
        for placeholder in template_placeholders:
            value = attendee.get(placeholder, "N/A")

            # If the value is missing or None, replace it with "N/A".
            if value is None:
                value = "N/A"

            # Convert the value to string before using replace().
            value = str(value)

            # Replace {name}, {event_title}, etc.
            invitation = invitation.replace(f"{{{placeholder}}}", value)

        # Write the personalized invitation into the output file.
        try:
            with open(
                f"output_{index}.txt", "w", encoding="utf-8"
            ) as output_file:
                output_file.write(invitation)
        except OSError as error:
            print(f"Error writing output_{index}.txt: {error}")
