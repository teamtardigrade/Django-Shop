from __future__ import unicode_literals

from django.db import models

class Category(models.Model):

	name = models.CharField(max_length=30, unique=True)
	active = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = "categories"


	def __unicode__(self):

		return self.name 