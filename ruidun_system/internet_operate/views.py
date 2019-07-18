from django.shortcuts import render

# Create your views here.


def internetindex(request):
    """物联网硬件管理系统二级菜单"""

    return render(request, 'internetindex.html')