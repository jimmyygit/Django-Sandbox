from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    context = {
        "text": "this is tezxt!!!",
        "list": [1,2,2,"last ITem1"],
        "html": "<h1>HTML header</h1>",
    }
    return render(request, "about.html", context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})