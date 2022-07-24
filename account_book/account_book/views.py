from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User


class Main(APIView):
    def get(self, request):
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        return render(request, 'account_book/main.html', context=dict(user=user))
