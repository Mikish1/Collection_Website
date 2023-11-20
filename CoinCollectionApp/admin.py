from django.contrib import admin
from .models import Coin, City, Authority, RulingState, Region, Category

# Register your models here.
admin.site.register(Coin)
admin.site.register(City)
admin.site.register(Authority)
admin.site.register(Region)
admin.site.register(RulingState)
admin.site.register(Category)