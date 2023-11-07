from django.shortcuts import render
import random

def home(request):
  return render(request, "adivinanumero/home.html")

def guess(request):
  random_number = random.randint(0, 10)
  user_guess = int(request.POST["number"])

  if user_guess == random_number:
    message = "¡Has acertado!"
  elif user_guess > random_number:
    message = "Demasiado alto"
  else:
    message = "Demasiado bajo"
  return render(request, "adivinanumero/guess.html", {'message': message , 'random_number': random_number})