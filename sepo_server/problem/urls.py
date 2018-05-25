from django.conf.urls import include, url
from problem.views import post_problem, prob_validate

urlpatterns = [
    url(r'^(?P<pk>\d+)/',post_problem,name = 'problem_no'),
    url(r'^(?P<pk>\d+)/validate/', prob_validate, name = 'problem_no'),
  ]
