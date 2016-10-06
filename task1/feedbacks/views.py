from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from myauth.views import need_authentication

from .models import Feedback
from .forms import FeedbackForm


def feedback_main(request):
    feedbacks = Feedback.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'feedback_main.html', {"feedbacks": feedbacks, 'title': 'Гадости'})


def trying_to_delete_or_edit_not_your_feedback(request):
    feedbacks = Feedback.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'feedback_main.html', {"feedbacks": feedbacks, 'title': 'Гадости'})

@need_authentication
def feedback_new(request):
    if not Feedback.objects.filter(author=request.user):
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.create(request.user)
                feedback.publish()
                return redirect("feedback_main")
        else:
            form = FeedbackForm()
        return render(request, 'feedback_new.html', {'form': form, 'title': 'Написать гадости'})
    else:
        return cheater(request, 'В одни руки один фидбек')


@need_authentication
def feedback_edit(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.user == feedback.author:
        if request.method == "POST":
            form = FeedbackForm(request.POST, instance=feedback)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.save()
                return redirect("feedback_main")
        else:
            form = FeedbackForm(instance=feedback)
        return render(request, 'feedback_new.html', {'form': form, 'title': 'Приукрасить гадости'})
    else:
        return cheater(request, 'Пытались редактировать жужой фидбек?')


@need_authentication
def feedback_delete(request, pk):
    feedback = Feedback.objects.filter(pk=pk)[0]
    if request.user == feedback.author or request.user.is_superuser:
        feedback.delete()
        return redirect("feedback_main")
    else:
        return cheater(request, 'Пытались удалить чужой фидбек?')


def cheater(request, message):
    return render(request, 'cheater.html', {'title': 'Читерок', 'cheater_message': message})
