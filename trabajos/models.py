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

class NewProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='../static/i')
    github_link = models.URLField(default='https://github.com/Mgobeaalcoba')
    github_link_img = models.ImageField(upload_to='../static/i')

    def __str__(self):
        return self.title
    
class Employee(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='../static/i')
    description = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    years = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey(Employee, related_name="experiences", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.position} at {self.company}"
