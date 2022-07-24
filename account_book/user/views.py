from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password


# Create your views here.


class Register(APIView):
    def get(self, request):
        return render(request, "user/register.html")

    def post(self, request):
        name = request.data.get('name', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        User.objects.create(name=name, email=email, password=make_password(password))

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=404)

        if user.check_password(password):
            request.session['email'] = email
            return Response(status="200")
        else:
            return Response(status=404)


class Logout(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")
