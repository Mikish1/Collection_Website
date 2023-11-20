from django import template

register = template.Library()


@register.filter
def in_category(region, category):
    print(region.filter(category__category=category), category)
    return region.filter(category__category=category)


@register.filter
def city_in_region(cities, region):
    return cities.filter(region__regionName=region)


@register.filter
def ruler_in_state(authorities, state):
    return authorities.filter(rulingState__state=state)


@register.filter
def coin_in_category_obverse(coins, category):
    return coins[category].obverse_image.url


@register.filter
def coin_in_category_reverse(coins, category):
    return coins[category].reverse_image.url

