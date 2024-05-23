from django import template
import main.views as views
from main.utils import menu

register = template.Library()

@register.simple_tag
def get_menu():
    return menu