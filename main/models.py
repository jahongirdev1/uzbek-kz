from django.db import models
from datetime import date
from ckeditor.fields import RichTextField





class Language(models.Model):
    kod = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title




class Navbar(models.Model):
    title = models.CharField(max_length=200)
    child_navbars = models.ForeignKey("Navbar", on_delete=models.CASCADE, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title





class Category(models.Model):
    title = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Information(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    full_desc = models.TextField(blank=True)
    mini_desc = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    job = models.CharField(max_length=200, blank=True)
    pdf = models.FileField(upload_to='upload', blank=True)
    qr = models.CharField(max_length=400,  blank=True)
    buttons_title = models.CharField(max_length=400,  blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title if self.title else "Без заголовка"





class News(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    full_desc = models.TextField(blank=True)
    mini_desc = models.CharField(max_length=200, blank=True)
    video = models.FileField(upload_to="media", null=True, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title





class Region(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    kod = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    mini_desc = models.CharField(max_length=200, blank=True)
    full_desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    longitude = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.kod


class FamousPersonalities(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    information = models.ForeignKey(Information, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    desc = models.TextField(blank=True)
    buttons_title = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def to_string(self):
        return f'{self.title} ---> {self.desc} --> {self.buttons_title} --> {self.status} -->{self.information}'



class Donate(models.Model):
    number_card = models.CharField(max_length=200)
    name_card = models.CharField(max_length=200)
    cvv = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    accept = models.BooleanField(default=False)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.price)



class JoinToGroup(models.Model):
    name = models.CharField(max_length=200)
    iin = models.CharField(max_length=200)
    date_birth = models.DateField(default=date.today, blank=True)
    phone_number = models.CharField(max_length=200)
    region_code = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.name















class Translate(models.Model):
    code = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    value = models.CharField(max_length=200,  default='default_value')


    def __str__(self):
        return f'{self.code} ----> {self.language}'

class Test(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload', blank=True)
    title2 = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    content = RichTextField(blank=True)

    def __str__(self):
        return self.title


class Traditions(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title2 = models.CharField(max_length=200, blank=True)
    desc = models.TextField(blank=True)
    content = RichTextField(blank=True)
    mini_desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class AboutUs(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class FamousPersons(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    sur_name = models.CharField(max_length=200,  blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    position = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200,  blank=True)
    desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)



    def __str__(self):
        return self.sur_name

class OurPartners(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return  self.title


class WhoAreWe(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    desc =  RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class OurHistory(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class YouthOrganizations(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Education(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    mini_desc = RichTextField(blank=True)
    full_desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class Sport(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    mini_desc = RichTextField(blank=True)
    full_desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class HelpThoseInNeed(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    mini_desc = RichTextField(blank=True)
    full_desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class ImportantDoc(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Statutes(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='upload', blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class PlansFor2025(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='upload', blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ProjectsFor2025(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)



    def __str__(self):
        return self.title


class LastNews(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class VideoMaterials(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to="media", null=True, blank=True)
    title = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class PhotoGallery(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Interview(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Язык")
    video = models.FileField(upload_to="media", null=True, blank=True, verbose_name="Видео")
    image = models.ImageField(upload_to='upload', blank=True, verbose_name="Изображение")
    title = models.CharField(max_length=200, blank=True, verbose_name="Заголовок")
    mini_desc = RichTextField(blank=True, verbose_name="Мини описание")
    full_desc = RichTextField(blank=True, verbose_name="Польная описание")
    journalist = models.CharField(max_length=200, blank=True, verbose_name="Журналист")


    class Meta:
        verbose_name = 'Интервью'
        verbose_name_plural = "Интервью"



    def __str__(self):
        return self.title


class EtnoCenterRegion(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Заголовок")
    titli_ru = models.CharField(max_length=200, blank=True, verbose_name="Заголовок русский")
    titli_en = models.CharField(max_length=200, blank=True, verbose_name="Заголовок английский")
    titli_kk = models.CharField(max_length=200, blank=True , verbose_name="Заголовок казахский")
    mini_desc = RichTextField(blank=True, verbose_name="Мини-описание")
    code = models.CharField(max_length=200, blank=True, verbose_name="Код")
    status = models.IntegerField(default=0 , verbose_name="Статус")
    
    class Meta:
        verbose_name = 'Этно центр регион'
        verbose_name_plural = "Этно центр регионы"

    def __str__(self):
        return self.title




class EtnoCenter(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Язык")
    etno_center_region = models.ForeignKey(EtnoCenterRegion, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Этно-центр-регион")
    title = models.CharField(max_length=200, blank=True , verbose_name="Заголовок")
    mini_desc = RichTextField(blank=True, verbose_name="Мини-описание")
    image = models.ImageField(upload_to='upload', blank=True, verbose_name="ИзображеИзображениение")
    info = RichTextField(blank=True , verbose_name="Информация")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone1 = models.CharField(max_length=200, verbose_name="Номер 1")
    phone2 = models.CharField(max_length=200, verbose_name="Номер 2")
    email = models.CharField(max_length=200, verbose_name="Почта")
    instagram = models.CharField(max_length=200, blank=True, verbose_name="Инстаграм")
    telegram = models.CharField(max_length=200, blank=True, verbose_name="Телеграм")
    youtube = models.CharField(max_length=200, blank=True, verbose_name="Ютуб")
    whatsapp = models.CharField(max_length=200, blank=True, verbose_name="Ватсап")
    longitude = models.CharField(max_length=200, blank=True, verbose_name="Долгота")
    latitude = models.CharField(max_length=200, blank=True, verbose_name="Широта")
    status = models.IntegerField(default=0, verbose_name="Статус")
    
    class Meta:
        verbose_name = 'Этно центр '
        verbose_name_plural = "Этно центр"

    def __str__(self):
        return self.title



class EtnoCenterManager(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Язык")
    etno_center = models.ForeignKey(EtnoCenter, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Этно-центр")
    image = models.ImageField(upload_to='upload', blank=True, verbose_name="Изображение")
    first_name = models.CharField(max_length=200, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=200, blank=True, verbose_name="Фамилия")
    position = models.CharField(max_length=200, blank=True, verbose_name="Позиция")
    desc = RichTextField(blank=True, verbose_name="Описание")
    mini_desc = RichTextField(blank=True, verbose_name="Мини-описание")
    status = models.IntegerField(default=0, verbose_name="Статус")

    class Meta:
        verbose_name = 'Этно центр менежер'
        verbose_name_plural = "Этно центр менежеры"

    def __str__(self):
        return self.first_name

class Association(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Язык")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    desc = RichTextField(blank=True, verbose_name="Описание")
    mini_desc = RichTextField(blank=True, verbose_name="Мини-описание")
    image1 = models.ImageField(upload_to='upload', blank=True, verbose_name="Изображение1")
    image2 = models.ImageField(upload_to='upload', blank=True, verbose_name="Изображение2")
    image3 = models.ImageField(upload_to='upload', blank=True, verbose_name="Изображение3")
    image4 = models.ImageField(upload_to='upload', blank=True, verbose_name="Изображение4")
    status = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Ассоциация'
        verbose_name_plural = "Ассоциации"

    def __sizeof__(self):
        return self.title

class Contact(models.Model):
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone1 = models.CharField(max_length=200, verbose_name='Номер 1')
    phone2 = models.CharField(max_length=200, verbose_name='Номер 2')
    email = models.CharField(max_length=200, verbose_name='Почта')
    status = models.IntegerField(default=0, verbose_name='Статус')
    instagram = models.CharField(max_length=200, blank=True, verbose_name='Инстаграм')
    telegram = models.CharField(max_length=200, blank=True, verbose_name='Телеграм')
    youtube = models.CharField(max_length=200, blank=True, verbose_name='Ютуб')
    whatsapp = models.CharField(max_length=200, blank=True, verbose_name='Ватсап')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.address



class PayLink(models.Model):
    link = models.CharField(max_length=500, blank=True, verbose_name='Ссылка')
    card_number = models.CharField(max_length=200, blank=True, verbose_name='Номер карты' )


    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return self.link












