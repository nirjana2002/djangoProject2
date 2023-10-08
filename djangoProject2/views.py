from django.shortcuts import render

from banks.models import Bank


def home(request):
   banks = Bank.objects.all()
   return render(request, 'home.html', context={"banks": banks})
