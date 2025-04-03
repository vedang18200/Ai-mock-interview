from django.urls import path
from . import views

urlpatterns = [
    # Existing URLs
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('interview/', views.interview_view, name='interview_page'),
    path('result/', views.result_view, name='result'),
    
    # API endpoints
    path('api/start-interview/', views.start_interview_api, name='start_interview_api'),
    path('api/submit-answer/', views.submit_answer, name='submit_answer'),
    path('api/evaluate-interview/', views.evaluate_interview, name='evaluate_interview'),
    
    # New endpoints for interview management
    path('api/delete-interview/<str:interview_id>/', views.delete_interview, name='delete_interview'),
    path('api/delete_all_interviews/', views.delete_all_interviews, name='delete_all_interviews'),
]