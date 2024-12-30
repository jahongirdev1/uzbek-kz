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


class Contact(models.Model):
    address = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    instagram = models.CharField(max_length=200, blank=True)
    telegram = models.CharField(max_length=200, blank=True)
    youtube = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.address


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
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to="media", null=True, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, blank=True)
    mini_desc = RichTextField(blank=True)
    full_desc = RichTextField(blank=True)
    journalist = models.CharField(max_length=200, blank=True)




class EtnoCenterRegion(models.Model):
    title = models.CharField(max_length=200, blank=True)
    titli_ru = models.CharField(max_length=200, blank=True)
    titli_en = models.CharField(max_length=200, blank=True)
    titli_kk = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title




class EtnoCenter(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    etno_center_region = models.ForeignKey(EtnoCenterRegion, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    info = RichTextField(blank=True)
    address = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200, blank=True)
    telegram = models.CharField(max_length=200, blank=True)
    youtube = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)
    longitude = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)




class EtnoCenterManager(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    etno_center = models.ForeignKey(EtnoCenter, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='upload', blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True)
    mini_desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.first_name

class Association(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    desc = RichTextField(blank=True)
    mini_desc = RichTextField(blank=True)
    image1 = models.ImageField(upload_to='upload', blank=True)
    image2 = models.ImageField(upload_to='upload', blank=True)
    image3 = models.ImageField(upload_to='upload', blank=True)
    image4 = models.ImageField(upload_to='upload', blank=True)
    status = models.IntegerField(default=0)

    def __sizeof__(self):
        return self.title

















