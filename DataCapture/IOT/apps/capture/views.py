from django.shortcuts import render
from django.forms import ModelForm
import sys
from django.http import HttpResponse

# Create your views here.

class CaptureCodeForm(ModelForm):
   class Meta:
      fields = [
         'code',
      ]
      labels = {
         'code': 'BarCode',
      }

def index(request):
   return render(request, 'capture/index.html')
   # return HttpResponse(
   # '<form action="/your-name/" method="post">'+
   #  '<label for="your_name">Your name: </label>'+
   #  '<input id="barcode" type="text" name="your_name" value="{{ current_name }}">'+
   #  '<input type="submit" value="OK">'+
   # '</form>')

def capture_code(request):
   if request.method == 'POST':
      code = request.POST.get('barcode')
      if code is not '':
         print('+++++++++++++++++++++++++++++', code)
         barcode = open('barCodeScanner.txt', 'w')
         barcode.write(code)
         barcode.close()
         code = ''
   # return HttpResponse('EL valor del formulario es:' + code)
   return render(request, 'capture/index.html', {'barcode':''})
   # return render(request, 'capture/index.html')
   # #return redirect('capture:index')