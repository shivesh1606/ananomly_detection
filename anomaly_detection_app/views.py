from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            num_points = int(request.POST.get('num_points'))
            contamination = float(request.POST.get('contamination'))
            seasonal_strength = float(request.POST.get('seasonal_strength'))
            random_strength = float(request.POST.get('random_strength'))
            
            # Validate contamination parameter
            if 0.0 < contamination <= 0.5:
                np.random.seed(42)
                time = np.arange(0, num_points)
                
                # Generate seasonal element
                seasonal_element = seasonal_strength * np.sin(0.1 * time)

                # Generate random noise
                random_noise = random_strength * np.random.normal(size=num_points)

                # Generate data stream
                data_stream = seasonal_element + random_noise

                # Initialize IsolationForest
                iso_forest = IsolationForest(contamination=contamination, random_state=42)
                X_train = data_stream.reshape(-1, 1)
                iso_forest.fit(X_train)

                # Predict anomalies
                preds_iso_forest = iso_forest.predict(X_train)

                # Get indices of anomalies
                anomalies_indices = np.where(preds_iso_forest == -1)[0]

                # Convert NumPy array to standard Python types
                anomalies_with_index = [(int(index), float(data_stream[index])) for index in anomalies_indices]
                data_stream_list = data_stream.tolist()

                # Return the JSON response
                return JsonResponse({
                    'anomalies_with_index': anomalies_with_index,
                    'data_stream': data_stream_list,
                    'num_points': int(num_points),
                    'contamination': float(contamination),
                    'seasonal_strength': float(seasonal_strength),
                    'random_strength': float(random_strength)
                })
            else:
                # Invalid contamination parameter
                return JsonResponse({'error': "Invalid contamination parameter. Please enter a value between 0.0 and 0.5."})
        except ValueError:
            # Invalid input for num_points, contamination, seasonal_strength, or random_strength
            return JsonResponse({'error': "Invalid input. Please enter valid values for num_points, contamination, seasonal_strength, and random_strength."})
    else:
        # Handle GET request (render the form)
        return render(request, 'anomaly_detection_app/home.html')
