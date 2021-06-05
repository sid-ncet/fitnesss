from django.db import models
class Data(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(default=0)
    age=models.IntegerField(default=0)
    adress=models.CharField(max_length=100)

    def register(self):
        self.save()

