from django.contrib import admin
from main.models import *
class BaseAdmin(admin.ModelAdmin):
    pass

models = [
    Language,
    News,
    Contact,
    Information,
    Navbar,
    Donate,
    JoinToGroup,
    Category,
    Region,
    FamousPersonalities
]

for model in models:
    admin.site.register(model, BaseAdmin)
