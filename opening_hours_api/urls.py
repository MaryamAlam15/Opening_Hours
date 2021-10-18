from django.urls import path

from opening_hours_api.views import OpeningHoursAPIView

urlpatterns = [
    path('opening-hours/', OpeningHoursAPIView.as_view(), name='opening_hours_api_view'),
]
