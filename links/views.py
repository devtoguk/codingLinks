from django.shortcuts import render

# Create your views here.
def show_links(request):
    return render(request, 'links/show.html')
