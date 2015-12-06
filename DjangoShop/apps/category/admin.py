from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):

	class Meta:
		model = Category