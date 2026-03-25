from xml.dom.minidom import Document

def text_to_kml(input_file, output_file):
    # Create a new KML document
    doc = Document()

    # Create the KML root element
    kml = doc.createElement("kml")
    kml.setAttribute("xmlns", "http://www.opengis.net/kml/2.2")
    doc.appendChild(kml)

    # Create Document and Placemark
    document = doc.createElement("Document")
    kml.appendChild(document)

    placemark = doc.createElement("Placemark")
    document.appendChild(placemark)

    name = doc.createElement("name")
    name.appendChild(doc.createTextNode("GNSS Path"))
    placemark.appendChild(name)

    # Description
    description = doc.createElement("description")
    description.appendChild(doc.createTextNode("Path generated from GNSS data"))
    placemark.appendChild(description)

    # Create LineString element for a continuous path
    line_string = doc.createElement("LineString")
    placemark.appendChild(line_string)

    extrude = doc.createElement("extrude")
    extrude.appendChild(doc.createTextNode("1"))
    line_string.appendChild(extrude)

    alt_mode = doc.createElement("altitudeMode")
    alt_mode.appendChild(doc.createTextNode("absolute"))
    line_string.appendChild(alt_mode)

    coordinates = doc.createElement("coordinates")

    # Read coordinates from the text file and add them to the KML as a continuous path
    with open(input_file, "r", encoding="latin-1") as file:
        recording = False
        for line in file:
            if "position:" in line:
                recording = True  # Start recording position data
            elif recording and "x:" in line:
                lon = line.split(":")[1].strip()
            elif recording and "y:" in line:
                lat = line.split(":")[1].strip()
            elif recording and "z:" in line:
                alt = line.split(":")[1].strip()
                coordinates.appendChild(doc.createTextNode(f"{lon},{lat},{alt} "))
                recording = False  # Stop recording after capturing x, y, z

    line_string.appendChild(coordinates)

    # Write the KML to the output file
    with open(output_file, "w") as f:
        f.write(doc.toprettyxml(indent="  "))

# Usage
input_file = "C:\\Users\\mattj\\Documents\\McMaster\\MEST\\GoWrench Project\\text files\\gnss_path.txt"
kml_file = "C:\\Users\\mattj\\Documents\\McMaster\\MEST\\GoWrench Project\\KML\\output_path.kml"
text_to_kml(input_file, kml_file)
print(f"KML file saved to {kml_file}")

