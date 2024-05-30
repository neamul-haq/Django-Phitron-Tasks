from django.db import models
from task_categories.models import Category
# Create your models here.
class Tasks(models.Model):
    taskTitle = models.CharField(max_length=100)
    assign_date = models.DateField()
    taskDescription = models.TextField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.taskTitle