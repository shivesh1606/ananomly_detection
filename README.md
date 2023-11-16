# Anomaly Detection Project

## Overview

This project implements an anomaly detection system using Isolation Forest, a machine learning algorithm. The system takes input parameters such as the number of data points, contamination level, seasonal strength, and random strength to generate a synthetic data stream and detect anomalies within it.

## Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Input Parameters](#input-parameters)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Use Case](#use-case)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following installed on your machine:

- Python (version X.X)
- Django (version X.X)
- Other dependencies (list them here)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/anomaly-detection-project.git ```
1. Navigate to the project directory:

   ```bash
cd anomaly-detection-project ```

2. Install dependencies:

  ```bash
pip install -r requirements.txt ```

## Usage
Run the Django development server:

  ```bash
python manage.py runserver ```

Open your web browser and go to http://localhost:8000/ to access the anomaly detection interface.

## Input Parameters
Num Points: Number of data points in the synthetic data stream.
Contamination: Proportion of anomalies in the data stream.
Seasonal Strength: Strength of the seasonal component in the data generation.
Random Strength: Strength of the random noise component in the data generation.
Results
The system will display the data stream, detected anomalies, and a graph illustrating the anomalies over the data stream.

## Technologies Used
- Django
- Plotly
- NumPy
- Scikit-learn
- Use Case
## Scenario:

Imagine you have a sensor network collecting data over time, and you want to identify anomalies or irregular patterns in the collected data. This anomaly detection system can be applied to analyze the sensor data, detect unusual patterns, and provide insights into potential issues or abnormalities within the monitored environment.
