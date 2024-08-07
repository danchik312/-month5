from django.contrib import admin
from . import models

admin.site.register(models.movie)
admin.site.register(models.review)
admin.site.register(models.director)

