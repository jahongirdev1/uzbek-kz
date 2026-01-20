from django.contrib import admin
from main.models import *


class BaseAdmin(admin.ModelAdmin):
    pass


class GalleryImagesInline(admin.TabularInline):
    model = GalleryImages
    extra = 1
    max_num = 20


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImagesInline]
    list_display = ('title', 'language', 'status', 'posted_date')


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
    PayLink,
]

for model in models:
    admin.site.register(model, BaseAdmin)


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    pass


@admin.register(Traditions)
class TraditionsAdmin(admin.ModelAdmin):
    pass