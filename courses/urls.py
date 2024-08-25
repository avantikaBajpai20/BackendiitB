from django.urls import path
from .views import (
    CourseListCreateView, CourseDetailView,
    CourseInstanceListCreateView, CourseInstanceDetailView, 
    AllInstancesView, AddInstanceAPIView
)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('add-instance/', AddInstanceAPIView.as_view(), name='add_instance'),
    path('instances/all/', AllInstancesView.as_view(), name='get_all_instances'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateView.as_view(), name='course-instance-list'),
    path('instances/<int:year>/<int:semester>/<int:pk>/', CourseInstanceDetailView.as_view(), name='course-instance-detail'),
]
