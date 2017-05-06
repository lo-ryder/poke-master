from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Poke, PokeManager
from ..logregapp .models import User
from django.db.models import Count

# Create your views here.
def pokes(request):


    context = {
        'activeUser': User.objects.get(id=request.session['id']),
        'distinctPokeList': Poke.objects.values('user_poking_id','personpoked_id').filter(personpoked_id=request.session['id']).annotate(Count('user_poking', distinct=False)).order_by('-user_poking__count'),
        'whoPokedMe': Poke.objects.values('personpoked_id','user_poking').filter(personpoked_id=request.session['id']).distinct(),
        'userList': User.objects.all().exclude(id=request.session['id']),
    }
    print '\n\nactiveUser->', context['activeUser']
    print '\n\ndistinctPokeList->', context['distinctPokeList']
    for poke in context['distinctPokeList']:
        print "personpoked_id", poke.values()

    print '\n\nwhoPokedMe->', context['whoPokedMe']
    for poke in context['whoPokedMe']:
        print "personpoked_id", poke.values()
    print '\n\nuserList->', context['userList'], '\n\n'

    print 'request.session id->', request.session['id']
    return render(request, 'pokeapp/pokes.html', context)


def pokebutton(request):
    print 'in pokebutton!!!!'
    Poke.objects.PokeButton(request.POST)
    print 'added a poke to +++++>', request.POST['personpoked_id']
    return redirect('pokeapp:pokes')
