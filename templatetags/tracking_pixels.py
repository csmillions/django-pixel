from django import template
from django_pixel.models import Pixel
register = template.Library()

@register.simple_tag(takes_context=True)
def get_pixel(context, affiliate_id__name):
	"""
	This template tag lets you add tracking pixels to pages.
	Pixels are retrieved by affiliate id, and are rendered as django templates.
	{% if  request.GET.cbaffi %}
		{% get_pixel 'cbaffi' %}
	{% endif %}
	"""
	try:
		pixel = Pixel.objects.get(affiliate_id=context['request'].REQUEST[affiliate_id__name])
		return template.Template(pixel.pixel).render(context)
	except Pixel.DoesNotExist:
		return ''

