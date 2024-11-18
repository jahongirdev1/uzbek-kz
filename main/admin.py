from django.contrib import admin
from main.models import *
class BaseAdmin(admin.ModelAdmin):
    pass

models = [
    Language,
    News,
    Contact,
    Navbar,
    Donate,
    JoinToGroup,
    Category,
    Region,
    FamousPersonalities
]


for model in models:
    admin.site.register(model, BaseAdmin)







class InformationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Information, InformationAdmin)