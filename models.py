from django.db import models
from sanitizer.models import SanitizedTextField

class Pixel(models.Model):
	"""
	Model to hold tracking pixel objects. Stores sanitized html that is rendered as a django template.
	"""
	allowed_tags = ['img', 'iframe', 'script', 'noscript']
	allowed_attributes = ['style', 'class', 'id', 'src', 'width', 'height', 'frameborder', 'type']

	affiliate_id = models.CharField(max_length=30, unique=True)
	pixel = SanitizedTextField(max_length=255, allowed_tags=allowed_tags, allowed_attributes=allowed_attributes, strip=True)