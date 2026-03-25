from simplekml import Kml
import simplekml

input_file = r'C:\Users\mattj\Documents\McMaster\MEST\GoWrench Project\text files\gnss_path.txt'
output_kml = r'C:\Users\mattj\Documents\McMaster\MEST\GoWrench Project\KML\gnss_path_google.kml'

kml = Kml()

# Open the input file and process the data
coordinates = []  # List to store coordinates (longitude, latitude, altitude)
with open(input_file, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        # Extract latitude, longitude, and altitude from the file
        if line.startswith("latitude:"):
            latitude = float(line.split(":")[1].strip())
        elif line.startswith("longitude:"):
            longitude = float(line.split(":")[1].strip())
        elif line.startswith("altitude:"):
            altitude = float(line.split(":")[1].strip())
            # Add the coordinates as a tuple (longitude, latitude, altitude)
            coordinates.append((longitude, latitude, altitude))

# Add a LineString to the KML for the path
linestring = kml.newlinestring(name="GNSS Path")
linestring.coords = coordinates
linestring.altitudemode = simplekml.AltitudeMode.absolute
linestring.extrude = 1
linestring.style.linestyle.color = simplekml.Color.red
linestring.style.linestyle.width = 3

# Save the KML file
kml.save(output_kml)
print(f"KML file generated successfully: {output_kml}")