from django.shortcuts import render

# Create your views here.
def index_view(request):

    context = {
        "name" : "Rahwa",
        "tagline" : "Aspiring Django Developer"
    }

    return render(request, "index.html", context)



def education_view(request):
    
    context = {
        "school_name": "Refactory",
        "graduation_year": 2026
    }

    return render(request, "education.html", context)
