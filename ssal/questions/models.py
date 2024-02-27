from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()
class Question(models.Model):

    name = models.CharField(max_length=20)
    proposition1 = models.CharField(max_length=100)  # First proposition for the question
    proposition2 = models.CharField(max_length=100)  # Second proposition for the question
    proposition3 = models.CharField(max_length=100)  # Third proposition for the question
    correct_answer = models.CharField(max_length=100)  # Right answer for the question
    prof = models.ForeignKey(user, on_delete=models.CASCADE,related_name='questions')

    def __str__(self) -> str:
        return self.name

    # def clean(self):
    #     super().clean()
    #     propositions = [self.proposition1, self.proposition2, self.proposition3]
    #     if self.correct_answer not in propositions:
    #         raise ValidationError("The correct answer must be one of the three propositions.")
