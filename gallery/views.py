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

    if 'searchcat' in request.GET and request.GET["searchcat"]:
        search_term = request.GET.get("searchcat")
        searched_images = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html',{"message":message,"all_images": searched_images})

    else:
        message = "You haven't searched for any term."
        return render(request, 'index.html',{"message":message})
