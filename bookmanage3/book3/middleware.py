# 导入中间件的父类
from django.utils.deprecation import MiddlewareMixin
class TestMiddleware1(MiddlewareMixin):
    # 自定义中间件
    def process_request(self, request):
        # 处理请求前的自动调用
        print('每次请求前调用111')

    def process_response(self, request, response):
        print('每次响应前 调用 222')
        return response

class TestMiddleware2(MiddlewareMixin):
    # 定义中间键
    def process_request(self, request):
        print('请求前执行 333333')

    def process_response(self,quest, response):
        print('每次响应前会执行  4444444')
        return response