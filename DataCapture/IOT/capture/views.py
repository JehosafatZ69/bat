# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'capture/index.html')

def capture_code(request):
   if request.method == 'POST':
      code = request.POST.get('barcode')
      if code is not '':
         print('+++++++++++++++++++++++++++++', code)
         barcode = open('barCodeScanner.txt', 'w')
         barcode.write(code)
         barcode.close()
   return render(request, 'capture/index.html', {'barcode':''})