from .models import Language, Navbar, Category, Information, Contact, News, Donate, JoinToGroup, Region, FamousPersonalities
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from googletrans import Translator
from django.db.models import Prefetch
import json
# change
translator = Translator()
def language_list(request):
    languages = Language.objects.all().filter(status=0).values()
    return JsonResponse(list(languages), safe=False)
    
@csrf_exempt
def navbar_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'ru')
        navbars = Navbar.objects.filter(status=0).values()
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
        lang_code = request.GET.get('lang_code', 'ru')
        print('test1')
        categories = Category.objects.all().filter(status=0).values()
        print('test2')

        translated_categories = [
            {
                'id': category['id'],
                'title': translator.translate(category['title'], dest=lang_code).text,
                'status': category['status'],
            }
            for category in categories
        ]
        print('test3')
        return JsonResponse(translated_categories, safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def information_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'ru')

        informations = Information.objects.filter(status=0).prefetch_related('category')
        translated_informations = []

        for info in informations:
            translated_info = {
                'id': info.id,
                'status': info.status,
                'image': info.image.url if info.image else "",
                'pdf': info.pdf.url if info.pdf else "",
                'qr': info.qr.url if info.qr else "",
                'category_id': info.category_id,
                'category_title': info.category.title if info.category else ""
            }

            for key in ['title', 'full_desc', 'mini_desc', 'job', 'buttons_title']:
                if getattr(info, key):
                    try:
                        translated_info[key] = translator.translate(getattr(info, key), dest=lang_code).text
                    except Exception as e:
                        translated_info[key] = getattr(info, key)
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
        news_items = News.objects.filter(status=0).values()

        def safe_translate(text, lang_code):
            return translator.translate(text, dest=lang_code).text if text else ""

        translated_news = [
            {
                'id': news['id'],
                'title': safe_translate(news.get('title'), lang_code),
                'full_desc': safe_translate(news.get('full_desc'), lang_code),
                'mini_desc': safe_translate(news.get('mini_desc'), lang_code),
                'video': news.get('video'),
                'image': news.get('image'),
                'posted_date': news.get('posted_date'),
                'name': news.get('name')
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
def famous_personalities_list(request):
    if request.method == 'GET':
        lang_code = request.GET.get('lang_code', 'ru')

        personalities = FamousPersonalities.objects.filter(status=0).prefetch_related('information')
        translated_personalities = []

        for personality in personalities:
            translated_personality = {
                'id': personality.id,
                'title': personality.title,
                'desc': personality.desc,
                'information_title': personality.information.title if personality.information else "",
                'buttons_title': personality.buttons_title
            }

            for key in ['title', 'desc', 'buttons_title']:
                if getattr(personality, key):
                    try:
                        translated_personality[key] = translator.translate(getattr(personality, key), dest=lang_code).text
                    except Exception as e:
                        translated_personality[key] = getattr(personality, key)
                        print(f"Translation error: {e}")
                else:
                    translated_personality[key] = ""

            if translated_personality['information_title']:
                try:
                    translated_personality['information_title'] = translator.translate(translated_personality['information_title'], dest=lang_code).text
                except Exception as e:
                    translated_personality['information_title'] = personality.information.title
                    print(f"Translation error: {e}")

            translated_personalities.append(translated_personality)

        return JsonResponse(translated_personalities, safe=False)
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


#
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from googletrans import Translator
#
# translator = Translator()
#
# @csrf_exempt
# def information_id(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             id = data.get('id')
#             lang_code = data.get('lang_code')
#
#             info = FamousPersonalities.objects.get(id=id)
#             print(info.to_string())
#             if not info:
#                 return JsonResponse({"error": "Information not found"}, status=400)
#
#             result = {
#                 'id': id,
#                 # 'image': info.information.image.url if info.information and info.information.image else "",
#                 'name': info.information.title if info.information.title else "",
#                 'job': translator.translate(info.information.job, dest=lang_code).text if info.information and info.information.job else "",
#                 'title': translator.translate(info.title, dest=lang_code).text if info.title else "",
#                 'desc': translator.translate(info.desc, dest=lang_code).text if info.desc else "",
#             }
#
#             return JsonResponse({"data": result}, status=200)
#
#         except FamousPersonalities.DoesNotExist:
#             return JsonResponse({"error": "Information does not exist"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     else:
#         return JsonResponse({"error": "Method not allowed"}, status=405)
#
#
#
#
#
#
#
#




