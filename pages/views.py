from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Homepage")


def about_page_view(request):
    context = {"name": "Ahlam",
               "age": 26,
               }

    return render(request, "pages/about.html", context)  # new
