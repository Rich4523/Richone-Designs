from django.shortcuts import render, redirect
from .models import Product, Category, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.

def category(request, foo):
	# Replace hyphens with spaces
	foo = foo.replace('-', ' ')
	# Grab the category from the url
	try:
		# Look up the Category
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'category.html', {'products':products, 'category':category})

	except:
		messages.success(request, ("That category doesn't exist..."))
		return redirect('home')



def product(request, pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product': product})


def home(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products': products})


def comment(request):
	submitted = False
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/comment?submitted=True')

	else:
		form = CommentForm
		if 'submitted' in request.GET:
			submitted = True


	return render(request, 'add_comment.html', {'form':form, 'submitted':submitted})


def about(request):
	return render(request, 'about.html', {})


def privacy(request):
	return render(request, 'privacy.html', {})




