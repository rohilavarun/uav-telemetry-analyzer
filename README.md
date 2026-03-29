# UAV Telemetry Anomaly Detector 🚁

## Overview
When building and testing drones or fixed-wing UAVs, flight controllers generate massive CSV files filled with raw telemetry data (voltage, pitch, altitude, wind resistance). Manually scanning these logs to find out why a drone became unstable is incredibly time-consuming. 

This project is a Python-based Machine Learning tool that automatically parses post-flight `telemetry.csv` logs, detects critical anomalies (like sudden voltage drops or dangerous pitch angles), and generates a human-readable post-flight debrief.

## Tech Stack
* **Language:** Python 3.9
* **Data Handling:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` 

## Setup & Installation

1. **Clone the repository:**
   Ensure you have downloaded all files into a single directory.

2. **Install the required dependencies:**
   Open your terminal and run:
   ```bash
   pip3 install pandas scikit-learn numpy