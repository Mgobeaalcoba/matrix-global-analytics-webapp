from django.contrib import admin
from .models import PorfolioItem, Employee, Experience, NewProject

# Register your models here.
admin.site.register(PorfolioItem)
admin.site.register(Employee)
admin.site.register(Experience)
admin.site.register(NewProject)
