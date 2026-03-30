UAV Telemetry Anomaly Detector 🚁
1. Project Overview

The UAV Telemetry Anomaly Detector is an automated diagnostic tool designed to enhance flight safety for Unmanned Aerial Vehicles. By processing high-frequency sensor logs (CSV), the system identifies critical flight risks—such as battery failures, aerodynamic instability, and hazardous weather conditions—using Unsupervised Machine Learning.

This project was developed as a solution to the time-consuming process of manually auditing telemetry data during drone prototyping and competition testing (e.g., SAE Aero Design).

2. Technical Stack

Language: Python 3.9

Data Handling: Pandas

Machine Learning: Scikit-Learn (Isolation Forest Algorithm)

Environment: macOS / Linux / Windows

3. Key Features

ML-Driven Detection: Uses the IsolationForest algorithm to detect outliers in flight data without needing pre-labeled "error" datasets.

Multi-Dimensional Analysis: Monitors Altitude, Voltage, Pitch, and Wind speed simultaneously to find correlations (e.g., wind gusts causing pitch instability).

Instant Post-Flight Debrief: Provides a human-readable summary of exactly when and why a flight reached unsafe parameters.

4. Installation & Setup

Step 1: Clone the Repository

Bash
git clone https://github.com/rohilavarun/uav-telemetry-analyzer.git
cd uav-telemetry-analyzer
Step 2: Install Dependencies

Bash
pip3 install pandas scikit-learn numpy
Step 3: Prepare Data
Place your telemetry log in the root folder named telemetry.csv. Ensure it contains the following columns:
Time, Altitude_m, Voltage_V, Pitch_deg, Wind_ms

5. Usage

To run the analysis, execute the main script:

Bash
python3 analyzer.py
Sample Output:

Plaintext
POST-FLIGHT ML DEBRIEF: ANOMALIES DETECTED
CRITICAL WARNING: 2 anomalies detected!
Timestamp: [00:05] -> Pitch: -25° | Wind: 22m/s
6. Safety Thresholds

The system flags data points based on both ML deviations and physical limits:

Voltage: Alerts if battery drops below 14.0V.

Pitch: Alerts if the drone tilts beyond ±20 degrees.

Wind: Alerts if gusts exceed 15 m/s.
