from django.shortcuts import render, HttpResponse

# Create your views here.

def tambah(request, num1, num2) :
    context = {
        'title': 'Kalkulator Tambah',
        'operator': '+',
        'num1' : num1,
        'num2' : num2,
        'result' : num1+num2

    }
    return render (request, 'calculator/index.html', context)

def kurang(request, num1, num2) :
    context = {
        'title': 'Kalkulator Kurang',
        'operator': '-',
        'num1': num1,
        'num2': num2,
        'result': num1-num2
    }
    return render(request, 'calculator/index.html', context)

def kali(request, num1, num2) :
    context = {
        'title': 'Kalkulator Kali',
        'operator': 'x',
        'num1': num1,
        'num2': num2,
        'result': num1*num2
    }
    return render(request, 'calculator/index.html', context)

def bagi(request, num1, num2) :
    context = {
        'title': 'Kalkulator Bagi',
        'operator': ':',
        'num1': num1,
        'num2': num2,
        'result': num1/num2
    }
    return render(request, 'calculator/index.html', context)