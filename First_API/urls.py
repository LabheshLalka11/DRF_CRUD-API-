from django.urls import path 
from . import views


urlpatterns = [
    path('Homepage/', views.Homepage),
    path('all-detail/',views.AllStudentDetail),
    path('student-detail/<int:pk>/',views.SingleStudentDetail),
]
