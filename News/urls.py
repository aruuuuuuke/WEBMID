from django.contrib import admin
from django.urls import path
from text import views as text 
from user import views as user 
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', text.all_news),
    path('', text.empty),
    path('news/<int:id>/', text.detail),
    path('country/<str:country>/',text.filterCountry),
    path('user/login/', user.auth_view ),
    path('user/registration/', user.registration_view),
    path('user/logout/', user.logout_view)
]   
