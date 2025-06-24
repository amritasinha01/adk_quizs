from django.shortcuts import render, redirect
from .models import QuizQuestion
from .forms import QuizQuestionForm
from agents.evaluator_agent import AnswerEvaluatorAgent

def home_view(request):
    return render(request, "core/index.html")

def upload_question_view(request):
    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quiz')
    else:
        form = QuizQuestionForm()
    return render(request, 'core/upload_question.html', {'form': form})

def quiz_view(request):
    questions = QuizQuestion.objects.all()
    results = []

    if request.method == 'POST':
        agent = AnswerEvaluatorAgent()

        for q in questions:
            selected = request.POST.get(f'q{q.id}')

            if not selected:
                selected = ""

            result = agent.run(user_answer=selected, correct_answer=q.correct_option)

            results.append({
                'question': q.question_text,
                'selected': selected,
                'correct': q.correct_option,
                'result': result
            })

        return render(request, 'core/quiz_result.html', {
            'results': results
        })

    return render(request, 'core/quiz.html', {'questions': questions})

