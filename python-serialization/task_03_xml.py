#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    """Serialize a Python dictionary to an XML file."""
    try:
        root = ET.Element("data")
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except OSError:
        return False


def deserialize_from_xml(filename):
    """Deserialize an XML file and return a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        for child in root:
            data[child.tag] = child.text
        return data
    except OSError:
        return None
