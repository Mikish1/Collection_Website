from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class RulingState(models.Model):
    state = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.state


class Authority(models.Model):
    authorityName = models.CharField(max_length=100, default=None)
    startRule = models.IntegerField(blank=True, null=True)
    endRule = models.IntegerField(blank=True, null=True)
    rulingState = models.ForeignKey(RulingState, on_delete=models.CASCADE, blank=True, null=True, related_name="ruling_state")

    class Meta:
        verbose_name_plural = "Authorities"

    def __str__(self):
        return self.authorityName


class Region(models.Model):
    regionName = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f"{self.regionName}"


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="city_region")

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.region.regionName}, {self.name}"


class Coin(models.Model):
    MATERIAL_CHOICES = (
        ("bronze", "Bronze"),
        ("silver", "Silver"),
        ("gold", "Gold"),
        ("lead", "Lead"),
        ("billon", "Billon"),
        ("iron", "Iron"),
    )

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="coins_city")
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE, related_name="mint_authority", blank=True, null=True)
    magistrate = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="coin_category")
    obverse_image = models.ImageField(upload_to='coin_images', blank=True, null=True)
    reverse_image = models.ImageField(upload_to='coin_images', blank=True, null=True)
    size = models.FloatField()
    weight = models.FloatField()
    material = models.CharField(max_length=100, choices=MATERIAL_CHOICES)
    denomination = models.CharField(max_length=100, blank=True)
    date_range = models.CharField(max_length=10, blank=True)
    date_exact = models.CharField(max_length=10, blank=True)
    obverse = models.TextField(default='')
    reverse = models.TextField(default='')
    reference = models.CharField(default='', max_length=50, blank=True)
    notes = models.TextField(blank=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        if self.authority is not None:
            return f"{self.category.category}, {self.authority.authorityName}: {self.city.region.regionName}, {self.city.name}"

        else:
            return f"{self.category.category}, {self.city.region.regionName}, {self.city.name}"
