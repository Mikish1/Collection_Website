import random

from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from .models import Category, Region, City, Coin, Authority, RulingState


# Create your views here.
class HomeView(TemplateView):
    template_name = 'CoinCollectionApp/home.html'


def category_list_view(request):
    categories = Category.objects.all().order_by('category')
    coin_samples = {}
    for category in categories:
        coin = random.sample(list(Coin.objects.filter(category__category=category.category)), 1)[0]
        coin_samples[category.category] = coin
    context = {
        'categories': categories,
        'coin_samples': coin_samples,
    }

    return render(request, 'CoinCollectionApp/category_list.html', context)


def region_list_view(request, category):
    regions = Region.objects.all().filter(city_region__coins_city__category__category=category).order_by('regionName').distinct()
    cities = City.objects.all().filter(coins_city__category__category=category).order_by('name').distinct()

    context = {
        'regions': regions,
        'cities': cities,
        'category': category,
    }
    return render(request, 'CoinCollectionApp/region_list.html', context)


def city_coin_list_view(request, category, city):
    coins = Coin.objects.all().filter(category__category=category, city__name=city).order_by("city__name")
    city = coins.first().city
    paginator = Paginator(coins, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'city': city,
        'coin_images': coins,
        'page_obj': page_obj,
    }
    return render(request, 'CoinCollectionApp/city_coin_list.html', context)


def roman_authority_list_view(request, category):
    rulingState = RulingState.objects.get(state="Roman Empire")
    authorities = Authority.objects.all().filter(mint_authority__category__category=category)
    coins = Coin.objects.all().filter(category__category=category, authority__rulingState__state="Roman Empire").order_by("authority__endRule")

    context = {
        'authorities': authorities,
        'rulingstate': rulingState,
        'category': category,
        'coin_images': coins,
    }
    return render(request, 'CoinCollectionApp/roman_authority_list.html', context)


def authority_list_view(request, category):
    authorities = Authority.objects.all().filter(mint_authority__category__category=category).distinct().order_by('endRule')
    rulingState = RulingState.objects.all().filter(ruling_state__mint_authority__category__category=category).order_by('state').distinct()

    context = {
        'authorities': authorities,
        'category': category,
        'ruling_state': rulingState,
    }
    return render(request, 'CoinCollectionApp/authority_list.html', context)


def authority_coin_list_view(request, category, authority):
    coins = Coin.objects.all().filter(category__category=category, authority__authorityName=authority).order_by("city__name")
    authority = coins.first().authority
    paginator = Paginator(coins, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'authority': authority,
        'coin_images': coins,
        'page_obj': page_obj,
    }
    return render(request, 'CoinCollectionApp/authority_coin_list.html', context)


def emperor_coin_list_view(request, category, authority):
    coins = Coin.objects.all().filter(category__category=category, authority__authorityName=authority, display=True).order_by("city__name")
    authority = coins.first().authority
    paginator = Paginator(coins, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'authority': authority,
        'coin_images': coins,
        'page_obj': page_obj,
    }

    return render(request, 'CoinCollectionApp/emperor_coin_list.html', context)


def coin_detail_view(request, category, pk):
    coin = Coin.objects.get(pk=pk)

    context = {
        'coin': coin
    }

    return render(request, 'CoinCollectionApp/coin_detail.html', context)


