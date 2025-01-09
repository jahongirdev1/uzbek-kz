from .models import Language, PlansFor2025, LastNews, WhoAreWe, EtnoCenterRegion, EtnoCenterManager, Donate, JoinToGroup, EtnoCenter, FamousPersons, Translate, Traditions, ProjectsFor2025, PhotoGallery, OurPartners, ImportantDoc, Sport, HelpThoseInNeed, AboutUs, Education, Statutes, YouthOrganizations, Interview, VideoMaterials, OurHistory, Association, Contact
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Prefetch
import json
from django.shortcuts import get_object_or_404






@csrf_exempt
def traditions(request):
    if request.method == 'GET':
        traditions_list = Traditions.objects.all().values()
        return JsonResponse(list(traditions_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def translations_list(request):
    if request.method == 'GET':
        trs = Translate.objects.all()
        translations = {}
        for tr in trs:
            if tr.language:
                if not tr.language.kod in translations:
                    translations[tr.language.kod] = {}
                translations[tr.language.kod][tr.code] = tr.value


        return JsonResponse(dict(translations), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)



def language_list(request):
    languages = Language.objects.filter(status=0).values()
    return JsonResponse(list(languages), safe=False)


@csrf_exempt
def join_to_group(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_join_to_group = JoinToGroup.objects.create(
                name=data.get('name'),
                iin=data.get('iin'),
                date_birth=data.get('date_birth'),
                phone_number=data.get('phone_number'),
                region_code=data.get('region_code'),
                status=0
            )
            return JsonResponse({"message": "JoinToGroup successfully created!", "id": new_join_to_group.id}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def donate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_donate = Donate.objects.create(
                number_card=data.get('number_card'),
                name_card=data.get('name_card'),
                cvv=data.get('cvv'),
                price=data.get('price'),
                accept=data.get('accept', False),
                status=data.get('status', 0),
            )
            return JsonResponse({"message": "Donate successfully created!", "id": new_donate.id}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
def about_us(request):
    print(request.method)
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        about_us_list = AboutUs.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(about_us_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def famous_persons(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        famous_persons_list = FamousPersons.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(famous_persons_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def our_partners(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        our_partners_list = OurPartners.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(our_partners_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def who_are_we(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        who_are_we_list = WhoAreWe.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(who_are_we_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def our_history(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        our_history_list = OurHistory.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(our_history_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def youth_organizations(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        youth_organizations_list = YouthOrganizations.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(youth_organizations_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def education(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        education_list = Education.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(education_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def sport(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        sport_list = Sport.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(sport_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def help_those_in_need(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        help_those_in_need_list = HelpThoseInNeed.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(help_those_in_need_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def important_doc(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        important_doc_list = ImportantDoc.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(important_doc_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def statutes(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        statutes_list = Statutes.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(statutes_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def plans_for2025(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        plans_for2025_list = PlansFor2025.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(plans_for2025_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)



@csrf_exempt
def projects_for2025(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        projects_for2025_list = ProjectsFor2025.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(projects_for2025_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)



@csrf_exempt
def last_news(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        last_news_list = LastNews.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(last_news_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def video_materials(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        video_materials_list = VideoMaterials.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(video_materials_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def photo_gallery(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        photo_gallery_list = PhotoGallery.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(photo_gallery_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def interview(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        interview_list = Interview.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(interview_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def etno_center(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        etno_center_list = EtnoCenter.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(etno_center_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def etno_center_manager(request):
    if request.method == 'GET':
        etno_center_regions_id = request.GET.get('etno_center_regions_id', 0)
        lang_code = request.GET.get('lang_code', 'kk')
        if not etno_center_regions_id:
            etno_center_manager_list = EtnoCenterManager.objects.filter(status=0, language__kod=lang_code).values()
            return JsonResponse(list(etno_center_manager_list), safe=False)

        managers_id = []
        if etno_center_regions_id:
            etno_center_manager_list = EtnoCenterManager.objects.filter(etno_center_regions_id=EtnoCenter.etno_center_region.id).values()
            for manger_id in etno_center_manager_list:
                managers_id.append(manger_id)
        return JsonResponse(list(etno_center_manager_list, managers_id), safe=False)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def etno_center_region(request):
    if request.method == 'GET':
        etno_center_region_list = EtnoCenterRegion.objects.filter(status=0).values()
        return JsonResponse(list(etno_center_region_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def association(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        association_list = Association.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(association_list), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def contact_list(request):
    if request.method == 'GET':
        contacts = Contact.objects.filter(status=0).values()
        return JsonResponse(list(contacts), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)



#exsample

@csrf_exempt
def managers_by_region(request, etno_center_region_id):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        get_object_or_404(EtnoCenter, etno_center_region_id=etno_center_region_id, status=0)

        managers = EtnoCenterManager.objects.filter(etno_center__etno_center_region_id=etno_center_region_id, status=0, language__kod=lang_code).values()

        managers_dict = {
            manager.id: {
                "id": manager.id,
                "language": manager.language,
                "image": manager.image,
                "first_name": manager.first_name,
                "last_name": manager.last_name,
                "position": manager.position,
                "desc": manager.desc,
                "mini_desc": manager.mini_desc,
                "status": manager.status,
            } for manager in managers
        }

        return JsonResponse(managers_dict, safe=False)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)



#
# @csrf_exempt
# def navbar_list(request):
#     if request.method == 'GET':
#         lang_code = request.GET.get('lang_code', 'kk')
#         navbars = Navbar.objects.filter(status=0, language__kod=lang_code).values()
#         return JsonResponse(list(navbars), safe=False)
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)
#
# @csrf_exempt
# def category_list(request):
#     if request.method == 'GET':
#         lang_code = request.GET.get('lang_code', 'kk')
#         categories = Category.objects.filter(status=0, language__kod=lang_code).values()
#         return JsonResponse(list(categories), safe=False)
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)
#
# @csrf_exempt
# def information_list(request):
#     if request.method == 'GET':
#         lang_code = request.GET.get('lang_code', 'kk')
#         informations = Information.objects.filter(status=0, language__kod=lang_code).values()
#         return JsonResponse(list(informations), safe=False)
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)
#

#
# @csrf_exempt
# def news_list(request):
#     if request.method == 'GET':
#         lang_code = request.GET.get('lang_code', 'kk')
#         news_items = News.objects.filter(status=0, language__kod=lang_code).values()
#         return JsonResponse(list(news_items), safe=False)
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)
#
# @csrf_exempt
# def region_list(request):
#     if request.method == 'GET':
#         lang_code = request.GET.get('lang_code', 'kk')
#         regions = Region.objects.filter(status=0, language__kod=lang_code).values()
#         return JsonResponse(list(regions), safe=False)
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)
#
# @csrf_exempt
# def famous_personalities_list(request):
#     if request.method == 'GET':
#         lang_code = request.GET.get('lang_code', 'kk')
#         personalities = FamousPersonalities.objects.filter(status=0, language__kod=lang_code).values()
#         return JsonResponse(list(personalities), safe=False)
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)