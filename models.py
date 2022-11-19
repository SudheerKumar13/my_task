from django.db import models
class Tasks(models.Model):
    task_id=models.IntegerField()
    category=models.CharField(max_length=255)
    status=models.CharField(max_length=30)
    
    class Meta:
        db_table="Tasks"