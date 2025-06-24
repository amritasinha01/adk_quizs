from django.urls import path
from .views import quiz_view, home_view, upload_question_view

urlpatterns = [
    path('', home_view, name='home'),
    path('quiz/', quiz_view, name='quiz'),
    path('upload-question/', upload_question_view, name='upload-question'),
]