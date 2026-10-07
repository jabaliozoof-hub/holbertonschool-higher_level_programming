#!/usr/bin/env python3
"""Module for basic JSON serialization and deserialization."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a JSON file.

    Args:

        data (dict): Python dictionary to serialize.
        filename (str): Name of the destination file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes JSON data into a Python dictionary.

    Args:

        filename (str): Name of the source JSON file.

    Returns:

        dict: Deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
