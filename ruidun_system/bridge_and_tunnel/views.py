from django.shortcuts import render

# Create your views here.

def bandtindex(request):
    """桥隧二级菜单"""

    return render(request, 'bandtindex.html')