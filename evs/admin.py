from django.contrib import admin

from .models import VotingEvent, Question

admin.site.register(VotingEvent)
admin.site.register(Question)
# Register your models here.
