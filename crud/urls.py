from django.urls import path
from .views import (
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:id>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:id>/', StudentDeleteView.as_view(), name='student-delete'),
]
