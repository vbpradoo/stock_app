# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import *
from .models import *



# def lotes_user(request, username):
#     user = get_object_or_404(User, username=username)
#     if request.user == user:
#         lotes = user.lotes.all()
#     else:
#         lotes = Lotes.public.filter(owner__username=username)
#     context = {'lotes': lotes, 'owner': user}
#     return render(request, 'stock/lotes_user.html', context)

@login_required
def lotes_create(request):
    if request.method == 'POST':
        form = LotesForm(data=request.POST)
        if form.is_valid():
            lotes = form.save(commit=False)
            lotes.owner = request.user
            lotes.save()
            form.save_m2m()
            return redirect('stock_lotes_create',
                username=request.user.username)
    else:
        form = LotesForm()
    context = {'form': form, 'create': True}
    return render(request, 'stock/form.html', context)

@login_required
def lotes_edit(request, pk):
    lotes = get_object_or_404(Lotes, pk=pk)
    if lotes.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = LotesForm(instance=lotes, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_lotes_list',
                username=request.user.username)
    else:
        form = LotesForm(instance=lotes)
    context = {'form': form, 'create': False}
    return render(request, 'stock/form.html', context)


def lotes_list(request):
    
    lotes = Lotes.public.all()
    context = {'lotes': lotes}
    return render(request, 'stock/lotes_list.html', context)
