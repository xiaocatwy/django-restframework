from django.shortcuts import render

# Create your views here.


def settingindex(request):
    """设置二级菜单"""

    return render(request, 'settingindex.html')