import datetime

from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.shortcuts import render, redirect

from story.models import Story


def index(request):
    today = datetime.date.today()
    stories = Story.objects.filter(created_at__gte=today).order_by('-number_of_votes')[0:50]

    if request.user.is_authenticated:
        for story in stories:
            story.has_voted = False

            if story.votes.filter(created_by=request.user):
                story.has_voted = True

    return render(request, 'core/index.html', {
        'stories': stories
    })


def new(request):
    today = datetime.date.today()
    stories = Story.objects.filter(created_at__gte=today).order_by('-created_at')

    if request.user.is_authenticated:
        for story in stories:
            story.has_voted = False

            if story.votes.filter(created_by=request.user):
                story.has_voted = True

    return render(request, 'core/new.html', {
        'stories': stories
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {
        'form': form
    })