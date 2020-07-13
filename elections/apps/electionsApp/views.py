from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Vote, Person

def index(request):
    all_votes_list = Vote.objects.all()[:15]
    #output = ', '.join([q.vote_title for q in all_votes_list])
    #return HttpResponse(output)
    return render(request, 'electionsApp/list.html', {'all_votes_list': all_votes_list})


def detail(request, vote_id):
    try:
        a = Vote.objects.get(id=vote_id)
    except:
        raise Http404('Голосование не найдено')
    return render(request, 'electionsApp/detail.html', {'vote': a})
    #return HttpResponse("Голосование %s." % vote_id)


def results(request, vote_id):
    response = "Результат %s."
    return HttpResponse(response % vote_id)


def vote_for_person(request, vote_id):
    pass


