#!/usr/bin/env python3
"""Basic serialization"""


def serialize_and_save_to_file(data, filename):
    """Serializes an object to a JSON file

    Args:
        data: The object to serialize
        filename: The name of the file to save the JSON string to
    """
    import json

    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Deserializes a JSON file to an object

    Args:
        filename: The name of the file to load the JSON string from

    Returns:
        The deserialized object
    """
    import json

    with open(filename, 'r') as f:
        return json.load(f)
