from django.db import models

# Create your models here.



class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.TextField()
    last_name=models.TextField()
    Cereal=[
        ("S","small"),
        ("M","medium"),
        ("L","large"),
        ("J","jumbo"),
    ]
    cereal= models.CharField(max_length=1, choices=Cereal)

    def __str__(self):
        return  str(self.id) + "-" +  self.name
    