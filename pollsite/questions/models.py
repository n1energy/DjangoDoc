from django.db import models

class Question(models.Model):
    qestion_text = models.CharField(max_lenght = 200)
    pub_date = models.DateTimeField()

class Choice(moldels.Model):
    qestion = models.ForeighnKey(Qestion, on_delete.models.CASCADE)
    choice_text = models.CharField(max_lenght = 200)
    votes = models.IntegerField(default = 0)
