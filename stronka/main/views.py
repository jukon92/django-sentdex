from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm dla "standardowego formularza rejestracji"
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    #categories = tablica slugowCategory
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        #w matching_series jest obiekt(y?) (tutorialseries) ktory pokrywa sie z singleslug
        #inaczej, wszystkie obiekty (tutorialseries) sa zebrane w matchnig_series wzgledem wspolnych singleslug/category_slug
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            #w part_one sa obiekty(tutorial) ktore sa czescia m.tutorialseries
            #obiekty ktore maja takie samo tutorialseries i jest ono rowne m.tutorial_series
            series_urls[m] = part_one.tutorial_slug
            #series_urls to dict w ktorym sa zebrane

        return render(request, "main/category.html", {"part_ones": series_urls})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("tutorial_published")

        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        return render(request,
                      'main/tutorial.html',
                      {"tutorial": this_tutorial,
                       "side_bar": tutorials_from_series,
                       "this_tutorial_idx": this_tutorial_idx})

    return HttpResponse(f"{single_slug} does not correspond to anything.")

def homepage(request):
    return render(request = request,
                    template_name = 'main/categories.html',
                    context={"categories": TutorialCategory.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        #form = UserCreationForm(request.POST) standardowy formularz
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are logged in as: {username}")
            #main:homepage, poniewaz nazwy w urls moga sie zmieniac, natomiast nazwa appki raczej nie
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    #form = UserCreationForm standardowy formularz
    return render(request, "main/register.html", context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as: {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})