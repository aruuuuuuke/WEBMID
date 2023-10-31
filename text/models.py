from django.db import models

class Text(models.Model):
    full_text=models.TextField()
    text= models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
