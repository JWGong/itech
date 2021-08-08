from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import Category, Dish, Review


# Create your views here.
class Home(View):
    def get(self, request):
        data = []
        categories = Category.objects.all()
        for category in categories:
            dishes = Dish.objects.filter(category=category)
            data.append({
                "category": category.name,
                "dishes": dishes
            })
        return render(request, "index.html", {"data": data, "type": "get"})


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse("home"))
        else:
            return render(request, "login.html", {"error": "Wrong account or password！"})


class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        email = request.POST.get("email")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username):
            return render(request, "register.html", {"error": "The username has been registered!"})
        else:
            User.objects.create_user(username=username, password=password, email=email, first_name=firstName,
                                     last_name=lastName)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse("home"))


class DishView(View):
    def get(self, request):
        dishId = request.GET.get("dId", 1)
        dish = Dish.objects.get(id=int(dishId))
        comments = Review.objects.filter(dish=dish).order_by('-addTime')
        return render(request, "dish.html", {"dish": dish, "comments": comments})

    def post(self, request):
        dishId = request.POST.get("dishId")
        comments = request.POST.get("comments")
        review = Review()
        review.user = request.user
        review.dish = Dish.objects.get(id=int(dishId))
        review.comments = comments
        review.save()
        return JsonResponse({"msg": "success",
                             "reviewData": {"username": request.user.username, "datetime": review.addTime,
                                            "content": review.comments}})


def handleLogout(request):
    logout(request)
    return redirect(reverse('login'))


def search(request):
    keyword = request.POST.get("keyword")
    context = {}
    if keyword:
        dishes = Dish.objects.filter(name__contains=keyword)
        context['dishes'] = dishes
        context['type'] = "search"
        return render(request, "index.html", context)
    else:
        return redirect(reverse("home"))
