from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length= 100)
    RegNo = models.CharField(max_length= 10)
    CourseUnit = models.CharField (max_length= 200)
    Mark = models.IntegerField ()

    def __str__(self):
        return self.Name