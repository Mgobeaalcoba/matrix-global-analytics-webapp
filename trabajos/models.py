from django.db import models

# Create your models here.
class PorfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='../static/i')
    github_link = models.URLField(default='https://github.com/Mgobeaalcoba')
    github_link_img = models.ImageField(upload_to='../static/i')

    def __str__(self):
        return self.title
