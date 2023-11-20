from django.urls import path
from .views import HomeView, category_list_view, region_list_view, city_coin_list_view, roman_authority_list_view, \
    authority_list_view, authority_coin_list_view, emperor_coin_list_view, coin_detail_view

urlpatterns = [

    path('', category_list_view, name="home"),
    path('categories/', category_list_view, name="category"),
    path('categories/<str:category>/regions/', region_list_view, name="region_list"),
    path('categories/<str:category>/regions/<str:city>', city_coin_list_view, name="coin_list"),
    path('categories/<str:category>/emperors/', roman_authority_list_view, name="roman_emperor_list"),
    path('categories/<str:category>/authorities/', authority_list_view, name="authority_list"),
    path('categories/<str:category>/authorities/<str:authority>', authority_coin_list_view, name="authority_coin_list"),
    path('categories/<str:category>/emperors/<str:authority>', emperor_coin_list_view, name="emperor_coin_list"),
    path('categories/<str:category>/<int:pk>', coin_detail_view, name="coin_detail"),

]