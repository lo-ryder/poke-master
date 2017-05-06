from __future__ import unicode_literals

from django.db import models
from ..logregapp .models import User


class PokeManager(models.Manager):
    print '_____in poke manager________'

    def PokeButton(self, postData):
        print ' person getting poked', postData['personpoked_id']
        print ' user poking user_id', postData['user_id']
        new_poke = Poke.objects.create(
            personpoked_id = User.objects.get(id=postData['personpoked_id']),
            user_poking = User.objects.get(id=postData['user_id']),
        )
        print 'added A POKE to ', postData['user_id']
        return new_poke

class Poke(models.Model):
    personpoked_id = models.ForeignKey(User, related_name="poked")
    user_poking = models.ForeignKey(User, related_name="poking")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PokeManager()
