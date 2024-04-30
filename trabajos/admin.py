from django.contrib import admin
from .models import PorfolioItem, Employee, Experience, NewProject, Cliente

# Register your models here.
admin.site.register(PorfolioItem)
admin.site.register(Employee)
admin.site.register(Experience)
admin.site.register(NewProject)
admin.site.register(Cliente)
