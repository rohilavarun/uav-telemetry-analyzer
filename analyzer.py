import pandas as pd
from sklearn.ensemble import IsolationForest
import warnings

# Suppress warnings for cleaner terminal output
warnings.filterwarnings('ignore')

def train_and_detect_anomalies(csv_file):
    """
    Uses an Unsupervised Machine Learning model (Isolation Forest) 
    to detect abnormal behavior in UAV flight data.
    """
    print(f"Loading flight data from {csv_file}...\n")
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("Error: Could not find telemetry.csv")
        return

    # Select the physical metrics the ML model should look at
    features = ['Altitude_m', 'Voltage_V', 'Pitch_deg', 'Wind_ms']
    X = df[features]

    print("Training pure Machine Learning Model on flight data...")
    
    # Initialize the Machine Learning Model
    model = IsolationForest(contamination=0.25, random_state=42)

    # Train the model and make predictions 
    df['Anomaly_Score'] = model.fit_predict(X)

    # Filter out only the anomalous rows (-1 means anomaly)
    anomalies = df[df['Anomaly_Score'] == -1]

    # Output the Results
    print("-" * 50)
    print("🚁 POST-FLIGHT ML DEBRIEF: ANOMALIES DETECTED")
    print("-" * 50)
    
    if anomalies.empty:
        print("Flight Status: NORMAL. No anomalies detected.")
    else:
        print(f"CRITICAL WARNING: {len(anomalies)} anomalies detected by ML algorithm!\n")
        for index, row in anomalies.iterrows():
            print(f"Timestamp: [{row['Time']}]")
            print(f"  -> Data Signature: Alt: {row['Altitude_m']}m | Volts: {row['Voltage_V']}V | Pitch: {row['Pitch_deg']}° | Wind: {row['Wind_ms']}m/s")
            print("  -> ML Assessment: Data point deviates significantly from normal flight parameters.\n")

if __name__ == "__main__":
    # Run the purely local ML pipeline
    train_and_detect_anomalies("telemetry.csv")