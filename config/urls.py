# config > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls', namespace='posts'))
]

#put : 객체를 그냥 다 바꾼다.
#RSET API 

#CBV  : Class로 API를 정의하는 형태
#FBV : Function으로 API를 정의하는 형태
