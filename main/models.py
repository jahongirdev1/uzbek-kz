from django.db import models
from datetime import date

# class Language(models.Model):
#     kod = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
#
#
# class Navbar(models.Model):
#     title = models.CharField(max_length=200)
#     child_navbars = models.ForeignKey("Navbar", on_delete=models.CASCADE, blank=True, null=True)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
#
#
#
# class NavbarThings(models.Model):
#     navbar = models.ForeignKey("Navbar", on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=200)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
#
#
#
#
# class Category(models.Model):
#     title = models.CharField(max_length=200)
#     catgorys_button = models.CharField(max_length=200)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
#
#
#
#
# class JoinToGroup(models.Model):
#     name = models.CharField(max_length=200)
#     iin = models.CharField(max_length=200)
#     date_birth = models.DateField(default=date.today, blank=True)
#     phone_number = models.CharField(max_length=200)
#     status = models.IntegerField(default=0)
#
#
#     def __str__(self):
#         return self.name
#
#
#
# class Donate(models.Model):
#     number_card = models.CharField(max_length=200)
#     name_card = models.CharField(max_length=200)
#     cvv = models.IntegerField(default=0)
#     price = models.IntegerField(default=0)
#     accept = models.BooleanField(default=False)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return str(self.price)
#
#
#
# class Region(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     kod = models.CharField(max_length=200, blank=True)
#     title = models.CharField(max_length=200, blank=True)
#     regions_navbars = models.CharField(max_length=200, blank=True)
#     longitude = models.CharField(max_length=200, blank=True)
#     latitude = models.CharField(max_length=200, blank=True)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.kod
#
#
# class RegionInformation(models.Model):
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
#     region_navbars = models.ForeignKey(Region.regions_navbars, on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=200, blank=True)
#     mini_desc = models.CharField(max_length=200, blank=True)
#     full_desc = models.TextField(blank=True)
#     image = models.ImageField(upload_to='upload', blank=True)
#     status = models.IntegerField(default=0)
#
#
#     def __str__(self):
#         return self.title
#
#
# class Contact(models.Model):
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
#     region = models.ForeignKey(Region.regions_navbars, on_delete=models.CASCADE, blank=True, null=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     address = models.CharField(max_length=200)
#     phone1 = models.CharField(max_length=200)
#     phone2 = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     status = models.IntegerField(default=0)
#     instagram = models.CharField(max_length=200, blank=True)
#     telegram = models.CharField(max_length=200, blank=True)
#     youtube = models.CharField(max_length=200, blank=True)
#     whatsapp = models.CharField(max_length=200, blank=True)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.address
#
#
#
# class Information(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     image = models.ImageField(upload_to='upload', blank=True)
#     title = models.CharField(max_length=200, blank=True)
#     full_desc = models.TextField(blank=True)
#     mini_desc = models.CharField(max_length=1000, blank=True)
#     any_file = models.FileField(upload_to='upload', blank=True)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
#
#
# class FamousPersonalities(models.Model):
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
#     region_navbars = models.ForeignKey(Region.regions_navbars, on_delete=models.CASCADE, blank=True, null=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     image = models.ImageField(upload_to='upload', blank=True)
#     fio = models.CharField(max_length=200, blank=True)
#     job = models.CharField(max_length=200, blank=True)
#     title = models.CharField(max_length=200, blank=True)
#     desc = models.TextField(blank=True)
#     buttons_title = models.CharField(max_length=200, blank=True)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
#
#
# class News(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=200, blank=True)
#     mini_desc = models.CharField(max_length=1000, blank=True)
#     full_desc = models.TextField(blank=True)
#     image = models.ImageField(upload_to='upload', blank=True)
#     video = models.FileField(upload_to='upload', blank=True)
#     posted_date = models.DateField(default=date.today, blank=True)
#     jurnalists_name = models.CharField(max_length=200, blank=True)
#     buttons_title = models.CharField(max_length=200, blank=True)
#     status = models.IntegerField(default=0)
#
#     def  __str__(self):
#         return self.title













class Language(models.Model):
    kod = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Navbar(models.Model):
    title = models.CharField(max_length=200)
    child_navbars = models.ForeignKey("Navbar", on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# class NavbarThings(models.Model):
#     navbar = models.ForeignKey("Navbar", on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=200)
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Information(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
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