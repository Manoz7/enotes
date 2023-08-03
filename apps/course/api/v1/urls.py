from django.urls import path
from rest_framework import routers

# from .views.demo import DemoView, DemoViewSet
from .views.course import (
    CourseListCreateView, CourseDetailView,
    SubjectListCreateView, SubjectDetailView,
    NoteListCreateView, NoteDetailView,
    QuestionPaperListCreateView, QuestionPaperDetailView,
    SyllabusListCreateView, SyllabusDetailView,
)

ROUTER = routers.DefaultRouter()

# ROUTER.register('demo', DemoViewSet, basename='demo-viewset')

urlpatterns = ROUTER.urls


urlpatterns = [
    # Course URLs
    path('courses/create', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # Subject URLs
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),

    # Note URLs
    path('notes/', NoteListCreateView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),

    # Question Paper URLs
    path('questionpapers/', QuestionPaperListCreateView.as_view(), name='questionpaper-list'),
    path('questionpapers/<int:pk>/', QuestionPaperDetailView.as_view(), name='questionpaper-detail'),

    # Syllabus URLs
    path('syllabus/', SyllabusListCreateView.as_view(), name='syllabus-list'),
    path('syllabus/<int:pk>/', SyllabusDetailView.as_view(), name='syllabus-detail'),
]
