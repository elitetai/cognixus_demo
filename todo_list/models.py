from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)

    def __str___(self):
        return self.title