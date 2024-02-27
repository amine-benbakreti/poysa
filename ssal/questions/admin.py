from django.contrib import admin
from .models import Question
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=["name","proposition1","proposition2","proposition3","correct_answer"]
