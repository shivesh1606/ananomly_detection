# from django.urls import path
# from .views import anomaly_detection_view

# urlpatterns = [
#     path('anomaly_detection/', anomaly_detection_view, name='anomaly_detection'),
# ]
from django.urls import path
from .views import detect_anomalies

urlpatterns = [
    path('', detect_anomalies, name='detect_anomalies'),
]
