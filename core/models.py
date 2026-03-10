from django.db import models

class AwarenessTopic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='topics/')

    def __str__(self):
        return self.title
from django.contrib.auth.models import User


class ToolUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool_name = models.CharField(max_length=200)
    input_data = models.TextField()
    result = models.TextField()
    used_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tool_name}"

from django.contrib.auth.models import User

class SecretNote(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    note = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Note"

from django.contrib.auth.models import User
from django.db import models


# Quiz Topic
class QuizTopic(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



# Question
class Question(models.Model):

    topic = models.ForeignKey(QuizTopic,
                              on_delete=models.CASCADE)

    question = models.TextField()

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_option = models.IntegerField()


    def __str__(self):
        return self.question



# Result save
class QuizResult(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    topic = models.CharField(max_length=200)

    score = models.IntegerField()

    total = models.IntegerField()

    percentage = models.FloatField()

    security_level = models.CharField(max_length=50)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} - {self.topic}"





class ToolUsage(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    tool_name = models.CharField(max_length=200)

    input_data = models.TextField(blank=True, null=True)

    result = models.TextField(blank=True, null=True)

    used_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} - {self.tool_name}"







