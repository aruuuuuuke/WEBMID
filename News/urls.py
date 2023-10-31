from django.contrib import admin
from django.urls import path
from text import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', views.all_news),
    path('', views.empty),
    path('news/<int:id>/', views.detail)

]
