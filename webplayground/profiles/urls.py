from django.urls import path
from .views import ProfileListView, ProfileDetailView

profile_patterns = ([
    path('', ProfileListView.as_view(), name="profiles"),
    path('<slug:username>/', ProfileDetailView.as_view(), name="profile"),
], 'profiles')