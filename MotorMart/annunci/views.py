from django.shortcuts import render

# Create your views here.
def annunci_list(request):
    return render(request, template_name="annunci/cars.html")
