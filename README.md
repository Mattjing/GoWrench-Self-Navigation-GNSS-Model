# GoWrench Self-Navigation GNSS Model

This repository consolidates the development artifacts for a GNSS-driven self-navigation workflow.  
It includes ROS launch/configuration files, simulation publishers, GNSS path conversion tools, KML outputs, text datasets, and a lightweight visualization app.

The project was built to support testing and demonstration of an autonomous navigation stack that can:

- consume GNSS data (real or simulated),
- fuse localization inputs through EKF,
- run move_base-based navigation,
- export and review trajectories in text/KML formats,
- visualize collected GNSS tracks for analysis.

## What This Project Achieved

The current repository demonstrates the following outcomes:

1. End-to-end GNSS navigation pipeline assembly using ROS launch orchestration.
2. Localization integration through `robot_localization` EKF configuration.
3. Testable GNSS simulation via fake publishers and dynamic GNSS generators.
4. Path and coordinate transformation utilities for TXT <-> KML workflows.
5. Practical result inspection through both KML files and browser-based GNSS visualization.
6. Repeatable experimentation setup with separated config, launch, script, and dataset assets.

## Repository Structure (Detailed)

### `GNSS_visualization/`

Purpose: browser-based viewing of GNSS data/paths.

- `GNSS_rtv.py`
	- Main Python script for serving or preparing GNSS data visualization.
	- Used to quickly inspect how trajectory points evolve over time.
- `templates/index.html`
	- Frontend template used by the visualization script.
	- Provides the map/UI layer for displaying GNSS tracks.

Use this folder when you want immediate visual feedback for generated or recorded GNSS traces.

#### Google Maps API Integration (JavaScript)

The web map is rendered using the Google Maps JavaScript API loaded in:

- `GNSS_visualization/templates/index.html`
	- `<script src="https://maps.googleapis.com/maps/api/js?key={{ api_key }}"></script>`
	- `google.maps.Map(...)` is used to initialize the map.
	- `google.maps.Marker(...)` is used to place the GNSS position marker.

The API key value is injected by the backend from:

- `GNSS_visualization/GNSS_rtv.py`

Related Google Maps Directions API usage also appears in:

- `pythonProject/google_path.py`
- `matt_self_navigation/scripts/fake_gnss_path.py`

### `matt_self_navigation/`

Purpose: core ROS package content for localization and navigation experiments.

#### `matt_self_navigation/config/`

Navigation and localization parameterization:

- `ekf.yaml`
	- EKF settings used by `robot_localization`.
	- Defines sensor fusion behavior and noise/covariance assumptions.
- `global_costmap.yaml`
	- Global planner map behavior and inflation/obstacle configuration.
- `local_costmap.yaml`
	- Local planner map behavior for short-horizon obstacle handling.
- `move_base.yaml`
	- Shared `move_base` planner/controller tuning.

#### `matt_self_navigation/launch/`

Composable ROS launch entry points:

- `self_navigation.launch`
	- High-level launcher for GNSS input, EKF localization, and `move_base`.
- `self_navigation_test.launch`
	- Testing-oriented launch composition.
- `ekf_localization.launch`
	- Starts localization nodes with EKF config.
- `move_base.launch`
	- Starts navigation stack (`move_base`) with costmaps/planners.
- `fake_gnss.launch`
	- Launch path for simulated GNSS testing.
- `robot_state_publisher.launch`
	- Robot state publishing setup for TF and model state flow.
- `static_transform.launch`
	- Static TF transform definitions used by the stack.

#### `matt_self_navigation/scripts/`

Simulation and testing helper nodes:

- `fake_gnss_publisher.py`
	- Publishes static/synthetic GNSS data on ROS topics for baseline testing.
- `fake_gnss_dynamic_generator.py`
	- Publishes dynamic GNSS trajectories by perturbing lat/lon/alt values.
- `fake_gnss_path.py`
	- Path-oriented GNSS generation logic for route simulation.
- `fake_gnss_publisher_tester.py`
	- Script for validating fake GNSS publisher behavior.
- `fake_imu_publisher.py`
	- Simulated IMU data source for localization fusion tests.

Use this package when running full navigation experiments in ROS.

### `pythonProject/`

Purpose: data preparation and conversion utilities outside the ROS runtime.

- `gnss_recorder.py`
	- Records GNSS streams into file-based datasets.
- `google_path.py`
	- Handles path processing for Google mapping workflow compatibility.
- `path_txt2KML.py`
	- Converts route/path text points into KML path output.
- `txt2KML.py`
	- General text-coordinate to KML conversion.

Use these scripts to transform raw logs into map-viewable artifacts and to prepare data for analysis.

### `KML/`

Purpose: geospatial artifacts for inspection in Google Earth or other KML viewers.

- `coordinates.kml`
- `example.kml`
- `gnss_data.kml`
- `gnss_path_google.kml`
- `output_path.kml`
- `output.kml`

These files represent sample inputs, processed outputs, and intermediate/final route visualizations.

### `text files/`

Purpose: plain-text GNSS datasets used by conversion and visualization scripts.

- `gnss_data.txt`
	- GNSS point records for general processing.
- `gnss_path.txt`
	- Path sequence for route-centric conversion/plotting.

### Root Files

- `README.md`
	- Project-level documentation and folder guide.
- `.gitignore`
	- Excludes temporary artifacts and large runtime outputs from version control.

## Typical Workflow

1. Collect or simulate GNSS/IMU data (`matt_self_navigation/scripts/`).
2. Launch localization and navigation (`matt_self_navigation/launch/`).
3. Tune navigation/localization parameters (`matt_self_navigation/config/`).
4. Export path data into TXT/KML (`pythonProject/`).
5. Inspect trajectories in map tools (`KML/`) or web view (`GNSS_visualization/`).

## Reproduction Notes

- ROS environment and dependencies must match your local setup.
- Required third-party ROS packages (for GNSS drivers/localization) should be installed in your workspace.
- Large ROS bag files are intentionally excluded from this repository.

Example visualization run:

```powershell
python GNSS_visualization/GNSS_rtv.py
```

Example navigation launch (after sourcing ROS workspace):

```bash
roslaunch self_navigation self_navigation.launch
```
