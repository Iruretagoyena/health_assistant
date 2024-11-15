import xml.etree.ElementTree as ET
import pandas as pd

def parse_apple_health_data(xml_file):
    # Load and parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)

    # Extract relevant health data
    health_data = []
    for record in root.findall('Record'):
        record_data = {
            'type': record.get('type'),
            'sourceName': record.get('sourceName'),
            'unit': record.get('unit'),
            'value': record.get('value'),
            'startDate': record.get('startDate'),
            'endDate': record.get('endDate')
        }
        health_data.append(record_data)

    # Convert to DataFrame
    health_df = pd.DataFrame(health_data)
    return health_df

# Example usage
xml_file = '../preprocessing/data/export.xml'
health_df = parse_apple_health_data(xml_file)

# Display the first few rows
print(health_df.head())
print(health_df.head(10))