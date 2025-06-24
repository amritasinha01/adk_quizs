from django.contrib import admin
from .models import QuizQuestion

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_option')
    search_fields = ('question_text',)

