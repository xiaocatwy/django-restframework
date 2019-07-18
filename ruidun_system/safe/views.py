from django.shortcuts import render

# Create your views here.


def safeindex(request):
    """安全管理二级菜单"""

    return render(request, 'safeindex.html')