from django.db import models

class Twice(models.Model):
    CHOICES = (
        ('KR', 'Korea'),
        ('JP','Japan'),
        ('TW', 'Tiwan'),
    )
    name= models.CharField(max_length = 30)
    age = models.IntegerField(default=3000)
    birth = models.DateTimeField()
    nationality = models.CharField(max_length = 30 , choices=CHOICES)
    position = models.TextField(max_length = 30)


    def __str__(self):
        return self.name