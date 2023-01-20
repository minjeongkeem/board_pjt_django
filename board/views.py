from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.http import (require_http_methods, require_safe, require_POST)

from django.contrib.auth.decorators import login_required
from . models import Article, Comment
from . forms import Articleform, CommentForm


# Create your views here.



@login_required
@require_http_methods(['GET', 'POST'])
def board_create(request):
    if request.method == "POST":
        form = Articleform(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save
            return redirect('board:board_detail', article.pk)
    else:
        form = Articleform()
    context = {'form':form}
    return render('board/board_create.html', context)

@require_safe
def board_index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'board/board_index.html', context)

@login_required
@require_safe
def board_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    is_like = article.like_users.exists()

    context = {'article':article, 'form':form, 'is_like':is_like}
    return render(request, 'board/board_detail.html', context)
    
@login_required
@require_POST
def board_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
        return redirect('board:board_index')
    else:
        return redirect('board:board_detail', article.pk)

def comment_create(request, article_pk):
    pass

def comment_delete(request, article_pk, comment_pk):
    pass


def likes(request):
    pass