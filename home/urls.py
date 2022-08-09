
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('signup',views.signup),
    path('login',views.login),
    path('logout',views.logout),
    path('addstudent', views.addstudent),
    path('showstudent', views.showstudent),
    path('updatestudent', views.updatestudent),
    path('searchstudent', views.searchstudent),
    path('joinstudent', views.joinstudent),
    path('showjoinedstudents', views.showjoinedstudents),
    path('updatejoined', views.updatejoined),
    path('searchjoinedstudents', views.searchjoinedstudents)


]
