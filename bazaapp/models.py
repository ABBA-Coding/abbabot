from django.db import models



class HeadCategory(models.Model):
    title = models.CharField(max_length=50, unique=True, null=True,blank=True,verbose_name="Xizmat Turi")
    owner = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Ism Familya")
    image = models.ImageField(null=True,blank=True,upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xizmat Turi"
        verbose_name_plural = "Xizmat Turlari"





class Category(models.Model):
    title = models.CharField(max_length=80, unique=True, null=True, blank=True, verbose_name="Bo'lim Turlari")
    headcategory = models.ForeignKey(HeadCategory,on_delete=models.CASCADE,default=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def get_photo(self):
        try:
            return self.image.url
        except:
            pass

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Projects(models.Model):
    title = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='Proyekt')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Proyekt"
        verbose_name_plural = "Proyektlar"


class Status(models.Model):
    title = models.CharField(max_length=90, unique=True, null=True, verbose_name="Proyekt Statusi")
    headcategory = models.ForeignKey(HeadCategory, models.CASCADE,default=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def get_photo(self):
        try:
            return self.image.url
        except:
            return 


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Jarayon'
        verbose_name_plural = 'Jarayonlar'