# GoWrench Final Report Repository

This repository contains the files curated to support the final report:

- `GoWrench Final Report.pdf`
- GNSS visualization app files
- Navigation scripts, launch files, and configuration files
- KML outputs and GNSS text datasets
- Utility Python scripts used for data conversion and path processing

## Folder Structure

- `GNSS_visualization/`: Visualization script and web template
- `matt_self_navigation/`: Scripts, launch files, and ROS config used in tests
- `KML/`: KML inputs/outputs used in mapping and path visualization
- `text files/`: GNSS text datasets used for processing
- `pythonProject/`: Supporting Python processing scripts

## Notes

- Large ROS bag files are intentionally excluded.
- Temporary and backup files are ignored through `.gitignore`.

## Reproduction

Install Python dependencies as needed and run scripts from their folders, for example:

```powershell
python GNSS_visualization/GNSS_rtv.py
```

Adjust paths depending on your local environment and ROS setup.
