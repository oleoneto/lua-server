from django.contrib import admin

admin.site.site_header = "Lua Learning Platform"
admin.site.site_title = "Lua Learning Platform"

# Admin configuration coming from `admin` package
from .admin import *
