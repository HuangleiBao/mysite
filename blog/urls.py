from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/blog/1
    path('<int:blog_id>',views.blog_detail,name="blog_detail"),
    path('type/<int:blog_type_id>',views.blogs_with_type,name="blog_with_type"),
]