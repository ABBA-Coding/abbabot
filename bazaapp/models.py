from django.db import models


class HeadCategory(models.Model):
    title = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Departament")
    owner = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Ism Familya")
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Departament"
        verbose_name_plural = "Departamentlar"


class TelegramGroups(models.Model):
    name = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name="Telegram Guruh")
    group_id = models.CharField(max_length=120, null=True, blank=True, verbose_name='Telegram Guruh IDsi')
    headgroups = models.ForeignKey(HeadCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Telegram Guruh"
        verbose_name_plural = "Telegram Guruhlar"


class Category(models.Model):
    title = models.CharField(max_length=80, unique=True, null=True, blank=True, verbose_name="Xizmat turlari")
    headcategory = models.ForeignKey(HeadCategory, on_delete=models.CASCADE, default=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def get_photo(self):
        try:
            return self.image.url
        except:
            pass

    class Meta:
        verbose_name = "Xizmat turi"
        verbose_name_plural = "Xizmat turlari"


class Projects(models.Model):
    title = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='Proyekt')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group = models.ForeignKey(TelegramGroups, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Proyekt"
        verbose_name_plural = "Proyektlar"


class Status(models.Model):
    title = models.CharField(max_length=90, unique=True, null=True, verbose_name="Proyekt Statusi")
    headcategory = models.ForeignKey(HeadCategory, models.CASCADE, default=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    def get_photo(self):
        try:
            return self.image.url
        except:
            return "#"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Jarayon'
        verbose_name_plural = 'Jarayonlar'
