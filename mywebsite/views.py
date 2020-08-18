from django.http import HttpResponse
from django.shortcuts import render

# Method view
def index(request):
    context = {
        'judul': 'Framework Django',
        'heading':'Selamat Datang',
	    'subheading':'Framework Django',
        'nav': [
			['/','Home'],
			['/about','About'],
			['/blog','Blog'],
        ]
    }
    return render(request,'index.html', context)

def about(request):
    context = {
        'judul': 'Framework Django',
        'heading':'About',
        'nav': [
			['/','Home'],
			['/about','About'],
			['/blog','Blog'],
        ]
    }
    return render(request,'about.html', context)