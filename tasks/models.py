from django.db import models

# Create your models here.

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )

created_at = models.DateTimeField(auto_now=True)
update_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title