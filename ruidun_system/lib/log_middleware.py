import datetime
from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(type(request))

    def process_response(self, request, response):
        # print(request)
        # print(response)
        # 记录增删改的操作
        print(type(request))
        # if request.method == "POST":
        #     category = "增加数据"
        # elif request.method == "PUT":
        #     category = "修改数据"
        # elif request.method == "DELETE":
        #     category = "删除数据"
        # else:
        #     return response
        # # object = request.view.serializer_class.Meta.Model.Meta.verbose_name
        # user = request.user.username
        # time = datetime.datetime.now()
        # print(category, user, time)
        return response