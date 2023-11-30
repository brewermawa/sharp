from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
import math

register = template.Library()

def currency(money):
    return f"${intcomma(math.floor(money))+(('%0.2f' % money)[-3:])}"

register.filter('format_currency', currency)