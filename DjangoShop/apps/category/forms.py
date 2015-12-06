from django import form
from category.models import Category


class CategoryForm(form.ModelForm):

	class Meta:
		model=Category