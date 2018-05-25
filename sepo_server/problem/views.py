# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from problem.models import ProblemModel
from problem.forms import PostForm
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import redirect
from ranking.models import Score, SolvedList

# Create your views here.

def post_problem(req,pk):
    post = get_object_or_404(ProblemModel, pk = pk)
    
    return render(req, 'Problem.html', {'post' : post})

def prob_validate(req,pk):
    answer = PostForm(req.POST)
    post = get_object_or_404(ProblemModel,pk=pk)

    if answer.is_valid():
        if answer.fl is post.flag:
            row = Score.objects.get(username=req.user)
            if SolvedList.objects.filter(username = req.user, pnum=pk) is None :
                row.score = row.score + 5
                row.save()
                SolvedList.objects.create(username = req.user, pnum = pk)
            return redirect('')
        else:
            return HttpResponse('Answer is wrong!')
    else:
        return HttpResponse('Abnormal Form!')



