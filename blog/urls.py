from django.urls import path
from .views import *

app_name = 'blog' # определяем пространство имен для приложения blog

urlpatterns = [
    # re_path() - метод позволяющий использовать регулярные выражения
    path('', post_list, name='post_list'),
    # path('', PostListView.as_view(), name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    # теперь будем обращаться к шаблонам приложения name - через пространство имен blog:post_list, blog:post_detail

]