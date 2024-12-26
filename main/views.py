from .models import Language, Navbar, Category, Information, Contact, News, Donate, JoinToGroup, Region, FamousPersonalities
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Prefetch
import json

def language_list(request):
    languages = Language.objects.filter(status=0).values()
    return JsonResponse(list(languages), safe=False)

@csrf_exempt
def navbar_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        navbars = Navbar.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(navbars), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        categories = Category.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(categories), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def information_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        informations = Information.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(informations), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def contact_list(request):
    if request.method == 'GET':
        contacts = Contact.objects.filter(status=0).values()
        return JsonResponse(list(contacts), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def news_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        news_items = News.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(news_items), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def region_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        regions = Region.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(regions), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def famous_personalities_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'kk')
        personalities = FamousPersonalities.objects.filter(status=0, language__kod=lang_code).values()
        return JsonResponse(list(personalities), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

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
