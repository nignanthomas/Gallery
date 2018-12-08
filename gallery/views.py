from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Image


# Create your views here.


def landing(request):
    all_images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Home'

    return render(request,'index.html', {'all_images':all_images,'locations':locations,'categories':categories, 'title':title})


def search_results(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Search'

    if 'searchcat' in request.GET and request.GET["searchcat"]:
        search_term = request.GET.get("searchcat")
        searched_images = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html',{"message":message,"all_images": searched_images,'locations':locations,'categories':categories, 'title':title})

    else:
        message = "You haven't searched for any term."
        return render(request, 'index.html',{"message":message, 'locations':locations,'categories':categories, 'title':title})


def page_category(request,category):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = f"{category}"
    category_results = Image.search_category(category)
    return render(request,'index.html',{'all_images':category_results,'locations':locations,'categories':categories, 'title':title})

def page_location(request,location):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = f"{location}"
    location_results = Image.filter_location(location)
    return render(request,'index.html',{'all_images':location_results,'locations':locations,'categories':categories, 'title':title})
