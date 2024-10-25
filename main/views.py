from django.views.decorators.csrf import csrf_exempt
from .models import Language, Navbar, Category, Information, Contact, News, Donate, JoinToGroup, Region
from django.http import JsonResponse
from googletrans import Translator
import json

translator = Translator()
def language_list(request):
    languages = Language.objects.all().filter(status=0).values()
    return JsonResponse(list(languages), safe=False)
@csrf_exempt
def navbar_list(request):
    if request.method == 'GET':
        body = json.loads(request.body)
        lang_code = body.get('lang_code', 'ru')

        navbars = Navbar.objects.all().filter(status=0).values()

        translated_navbars = [
            {
                'id': navbar['id'],
                'title': translator.translate(navbar['title'], dest=lang_code).text,
                'status': navbar['status']
            }
            for navbar in navbars
        ]
        return JsonResponse(translated_navbars, safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'en')
        categories = Category.objects.all().filter(status=0).values()
        translated_categories = [
            {
                'id': category['id'],
                'title': translator.translate(category['title'], dest=lang_code).text,
                'status': category['status']
            }
            for category in categories
        ]
        return JsonResponse(translated_categories, safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
@csrf_exempt
def information_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'en')
        informations = Information.objects.all().filter(status=0).values()
        translated_informations = []
        for info in informations:
            translated_info = {
                'id': info['id'],
                'status': info['status'],
                'image': info['image'],
                'pdf': info['pdf'],
                'qr': info['qr'],
            }
            for key in ['title', 'full_desc', 'mini_desc', 'job']:
                if info[key]:
                    try:
                        translated_info[key] = translator.translate(info[key], dest=lang_code).text
                    except Exception as e:
                        translated_info[key] = info[key]
                        print(f"Translation error: {e}")
                else:
                    translated_info[key] = ""
            translated_informations.append(translated_info)
        return JsonResponse(translated_informations, safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
@csrf_exempt
def contact_list(request):
    lang_code = request.GET.get('lang_code', 'ru')

    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

    contacts = Contact.objects.all().filter(status=0).values()

    if not contacts:
        return JsonResponse({'message': 'No contacts found.'}, status=404)

    translated_contacts = []
    for contact in contacts:
        translated_contact = {
            'id': contact['id'],
            'address': translator.translate(contact['address'], dest=lang_code).text,
            'phone1': contact['phone1'],
            'phone2': contact['phone2'],
            'email': contact['email'],
            'status': contact['status'],
            'instagram': contact['instagram'],
            'telegram': contact['telegram'],
            'youtube': contact['youtube'],
            'whatsapp': contact['whatsapp']
        }
        translated_contacts.append(translated_contact)

    return JsonResponse(translated_contacts, safe=False)

@csrf_exempt
def news_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'ru')

        news_items = News.objects.all().filter(status=0).values()
        translated_news = [
            {
                'id': news['id'],
                'title': translator.translate(news['title'], dest=lang_code).text,
                'full_desc': translator.translate(news['full_desc'], dest=lang_code).text,
                'mini_desc': translator.translate(news['mini_desc'], dest=lang_code).text,
                'video': news['video'],
                'image': news['image'],
                'posted_date': news['posted_date'],
                'name': news['name']
            }
            for news in news_items
        ]

        return JsonResponse(translated_news, safe=False)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def region_list(request):
    lang_code = request.GET.get('lang_code', 'ru')

    if request.method == 'GET':
        regions = Region.objects.all().filter(status=0).values()
        translated_regions = [
            {
                'id': region['id'],
                'kod': region['kod'],
                'title': translator.translate(region['title'], dest=lang_code).text,
                'mini_desc': translator.translate(region['mini_desc'], dest=lang_code).text,
                'full_desc': translator.translate(region['full_desc'], dest=lang_code).text,
                'image': region['image'],
                'longitude': region['longitude'],
                'latitude': region['latitude']
            }
            for region in regions
        ]

        return JsonResponse(translated_regions, safe=False)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def jointogroup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_jointogroup = JoinToGroup.objects.create(
                name=data.get('name'),
                iin=data.get('iin'),
                date_birth=data.get('date_birth'),
                phone_number=data.get('phone_number'),
                status=0
            )
            return JsonResponse({"message": "JoinToGroup successfully created!", "id": new_jointogroup.id}, status=200)
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















