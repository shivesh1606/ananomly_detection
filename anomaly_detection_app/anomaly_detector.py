import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination)

    def train(self, data):
        data = np.array(data).reshape(-1, 1)
        self.model.fit(data)

    def detect_anomalies(self, data):
        data = np.array(data).reshape(-1, 1)
        anomaly_scores = self.model.decision_function(data)
        labels = self.model.predict(data)
        return labels, anomaly_scores

def simulate_data_stream(num_points=1000):
    np.random.seed(42)
    time = np.arange(0, num_points)
    regular_pattern = np.sin(0.02 * time)
    seasonal_element = 0.5 * np.sin(0.1 * time)
    random_noise = 0.1 * np.random.normal(size=num_points)
    data_stream = regular_pattern + seasonal_element + random_noise
    return data_stream

def visualize_data_stream(data_stream, anomaly_labels):
    plt.plot(data_stream, label='Data Stream')
    anomalies = np.where(anomaly_labels == -1)[0]
    plt.scatter(anomalies, data_stream[anomalies], color='red', label='Anomalies')
    plt.title('Data Stream with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
