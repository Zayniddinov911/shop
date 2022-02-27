from django import template

register = template.Library()


@register.simple_tag()
def get_current_price(request, x):
    t = request.GET.get('price')
    if t:
        return t.split(';')[x]
    else:
        return 'null'
