from django.contrib import admin
from main.models import *
class BaseAdmin(admin.ModelAdmin):
    pass

models = [
    Language,
    Contact,
    Donate,
    JoinToGroup,
    FamousPersons,
    Sport,
    Education,
    LastNews,
    VideoMaterials,
    Interview,
    PhotoGallery,
    AboutUs,
    WhoAreWe,
    PlansFor2025,
    ProjectsFor2025,
    OurHistory,
    OurPartners,
    HelpThoseInNeed,
    Statutes,
    YouthOrganizations,
    EtnoCenter,
    EtnoCenterRegion,
    EtnoCenterManager,
    ImportantDoc,
    Association,

]


for model in models:
    admin.site.register(model, BaseAdmin)



class TranslateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Translate, TranslateAdmin)



class TraditionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Traditions, TraditionsAdmin)
