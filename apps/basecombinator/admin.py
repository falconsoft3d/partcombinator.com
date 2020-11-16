from django.contrib import admin
from .models import (
    PyCompany,PyCron,PyCountry)

# Register your models here.
admin.site.register(PyCompany)
admin.site.register(PyCron)
admin.site.register(PyCountry)