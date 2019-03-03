from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class ListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class List(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_by': self.created_by.username
        }

    def get_absolute_url(self):
        return reverse_lazy('main:lists')


class Task(models.Model):
    name = models.CharField(max_length=255)
    cr_date = models.DateTimeField()
    due_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default=False)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cr_date': self.cr_date,
            'due_date': self.due_date,
            'user': self.created_by.username,
            'mark': self.mark,
            'list': self.list_id.name
        }

    def get_absolute_url(self):
        return reverse_lazy('main:todo_list')
