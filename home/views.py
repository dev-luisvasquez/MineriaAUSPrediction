from turtle import end_fill
from django.shortcuts import render
from django.http import HttpResponse

from joblib import load


def predict(request):
      RanfomForest = load("RandomFC\model\RandomForest_joblib.pkl")
      if request.method == 'GET':
            
            (RanfomForest.predict([[0,12,12,12,12,12,1]]))
            return render(request, "home/index.html")
      elif request.method == 'POST':
      # mejor_modelo = load(Settings.RUTA_MODELO)
            Loc = (request.POST['Loc'])
            hum3 = (request.POST['hum3'])
            hum9 = (request.POST['hum9'])
            evap = (request.POST['evap'])
            temp9 = (request.POST['temp9'])
            temp3 = (request.POST['temp3'])
            rain = (request.POST['rain'])
            salida = {
          "predict": int(RanfomForest.predict(([[Loc, hum3, hum9, evap, temp9, temp3, rain]]))[0])
      }
            print(salida)
            return render(request, "home/index.html", context = salida)
      salida = salida.cleaned_data()
      salida = salida.save()

def home(request): return render (request, 'home/index.html')