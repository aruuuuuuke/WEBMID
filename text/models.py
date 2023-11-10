from django.db import models


class Country(models.Model):
    name = models.TextField() 

    def __str__(self):
        return self.name    

class Text(models.Model):
    full_text=models.TextField()
    text= models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)

    def __str__(self):
        return self.text