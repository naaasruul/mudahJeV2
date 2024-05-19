# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class Quiz(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
#     text = models.CharField(max_length=300)

#     def __str__(self):
#         return self.text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
#     text = models.CharField(max_length=200)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text

# class Result(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     score = models.IntegerField()

#     def __str__(self):
#         return f'{self.user.username} - {self.quiz.title}'
