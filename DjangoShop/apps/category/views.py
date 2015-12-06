from django.shortcuts import render
from category.models import Category

def singleCategory(request, id):

	try:
		category = Category.objects.get(pk=id)
	except Category.DoesNotExist:
		message = "Requested category does not exist"
	else:
		context = {'category':category}
		return render(request,'category/singleCategory.html',context)

	context = {'message':message}
	return render(request,'category/singleCategory.html',context)


def categoryCollection(request):

	categories = Category.objects.all()
	return render(request,'category/categoryCollection.html',context)


