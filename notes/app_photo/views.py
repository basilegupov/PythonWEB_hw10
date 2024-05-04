from django.shortcuts import render, redirect
from .forms import PictureForm
from .models import Picture
# Create your views here.


def index(request):
    return render(request, "app_photo/index.html", context={"msg": "Hello"})
    

def pictures(request):
    pics = Picture.objects.all()
    return render(request, "app_photo/pictures.html", context={"pics": pics})


def uploads(request):
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            form.save()
            return redirect(to="app_photo:pictures")
    return render(request, "app_photo/uploads.html", context={"form": form})
