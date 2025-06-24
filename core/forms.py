from django import forms
from .models import QuizQuestion

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = '__all__'