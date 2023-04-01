from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.urls import resolve, Resolver404
from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        current_url = resolve(request.path_info).url_name
    except Resolver404:
        current_url = None
    menu_items = MenuItem.objects.filter(name=menu_name)
    if menu_items:
        menu_item = menu_items[0]
        menu_html = generate_menu_html(menu_item, current_url)
        return menu_html
    else:
        return ''


def generate_menu_html(menu_item, current_url):
    sub_items = menu_item.menuitem_set.all()
    has_sub_items = sub_items.exists()
    active = current_url == menu_item.named_url
    css_classes = []
    if active:
        css_classes.append('active')
    if has_sub_items:
        css_classes.append('has-sub-items')
    css_classes_str = ' '.join(css_classes)
    html = f'<li class="{css_classes_str}">'
    if menu_item.named_url:
        url = menu_item.get_url()
        html += f'<a href="{url}">{menu_item.name}</a>'
    else:
        html += f'<span>{menu_item.name}</span>'
    if has_sub_items:
        html += '<ul>'
        for sub_item in sub_items:
            html += generate_menu_html(sub_item, current_url)
        html += '</ul>'
    html += '</li>'
    return html
