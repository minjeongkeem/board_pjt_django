from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views.decorators.http import (require_http_methods, require_safe, require_POST)

from django.contrib.auth.decorators import login_required
from .models import Content


# Create your views here.


@require_safe
def board_index(request):
    contents = Content.objects.all()
    context = {'contents': contents}
    return render(request, 'board/board_index.html', context)


def board_detail(request):
    content = Content.objects.all()
    pass

def board_create(request):
    
    pass

def board_edit(request):
    pass

def board_delete(request):
    pass

