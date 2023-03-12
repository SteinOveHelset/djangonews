from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import StoryForm, CommentForm
from .models import Story, Comment, Vote


def detail(request, pk):
    story = Story.objects.get(pk=pk)
    story.has_voted = False

    if story.votes.filter(created_by=request.user):
        story.has_voted = True

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user
            comment.save()

            return redirect('story:detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'story/detail.html', {
        'story': story,
        'form': form
    })


@login_required
def vote(request, pk):
    story = Story.objects.get(pk=pk)

    already_voted = story.votes.filter(created_by=request.user)

    if not already_voted:
        Vote.objects.create(story=story, created_by=request.user)

        story.number_of_votes = story.number_of_votes + 1
        story.save()
    
    redirect_page = request.GET.get('redirect_page', '/')

    if redirect_page == 'detail':
        return redirect('story:detail', pk=pk)
    else:
        return redirect(redirect_page)


@login_required
def unvote(request, pk):
    story = Story.objects.get(pk=pk)

    vote = Vote.objects.get(story_id=pk, created_by=request.user)
    vote.delete()

    story.number_of_votes = story.number_of_votes - 1
    story.save()
    
    redirect_page = request.GET.get('redirect_page', '/')

    if redirect_page == 'detail':
        return redirect('story:detail', pk=pk)
    else:
        return redirect(redirect_page)


@login_required
def create(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()

            return redirect('/')
    else:
        form = StoryForm()

    return render(request, 'story/create.html', {
        'form': form
    })