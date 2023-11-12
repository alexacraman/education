from django.urls import path
from .views import StudentRegistrationView, StudentEnrollCourseView, StudentCourseListView, StudentCourseDetailView, StudentDashboard, contact_view

urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<slug:slug>/', StudentCourseDetailView.as_view(), name='student_course_detail'),
    path('course/<slug:slug>/<module_id>', StudentCourseDetailView.as_view(), name='student_course_detail_module'),
    path('dashboard/', StudentDashboard.as_view(), name='dashboard'),
    path('contact/', contact_view, name='contact'),
    
   
]