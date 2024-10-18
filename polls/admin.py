from urllib import request
from django.contrib import admin
from polls.models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question)

