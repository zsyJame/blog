from django.urls import path
from views import RegisterView
urlpatterns = [
    # path的第一个参数：路由
    # 第二个参数： 视图参数名
    path('register/',RegisterView.as_view()),
]