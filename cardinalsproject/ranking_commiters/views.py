from django.shortcuts import render
from operator import attrgetter

from api_request.models import *

from ranking_commiters.models import Weight


def ranking_commiters(request, organization, repository):

    repository = RepositoryAPI(organization, repository)

    if request.method == 'GET':
        repository.update_score()
    elif request.method == 'POST':
        weight = Weight(request)
        repository.update_score(weight)
        
    commiters = repository.contributors

    ranking_commiters = sorted(commiters,
                               key=attrgetter('score'),
                               reverse=True)

    context = {"repo_id": 0, "ranking_commiters": ranking_commiters}

    return render(request, 'rankingCommiters.html', context)