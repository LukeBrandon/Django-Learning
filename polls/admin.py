from django.contrib import admin
from.models.choice import Choice
from.models.question import Question

# Register your models here.
admin.site.register([Question, Choice])