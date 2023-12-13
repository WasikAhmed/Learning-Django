from django.urls import path
from .views import DepartmentListCreateView, DepartDetailView, StudentListCreateView, StudentDetailView

urlpatterns = [
    path("departments/", DepartmentListCreateView.as_view(), name="department_list_create"),
    path("departments/<int:pk>", DepartDetailView.as_view(), name="department_detail"),
    path("students/", StudentListCreateView.as_view(), name="student_list_create"),
    path("students/<int:pk>", StudentDetailView.as_view(), name="student_detail"),
]
