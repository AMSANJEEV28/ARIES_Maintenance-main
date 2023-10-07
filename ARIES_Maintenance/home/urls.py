from django.urls import path
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name='index'),
    path("compressor/", views.compressor_view, name='compressor'),
    path("part1/", views.part1_view, name='part1'),
    path('aries_login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("part2/", views.part2_view, name='part2'),
    path("part3/", views.part3_view, name='part3'),
    path("part4/", views.part4_view, name='part4'),
    path("part5/", views.part5_view, name='part5'),
    path("chiller/", views.chiller_view, name='chiller'),
    path("hydraulicpump/", views.hydraulicpump_view, name='hydraulicpump'),
    path("notification/", views.notification_view, name='notification'),
    path("part6/", views.part6_view, name='part6'),
    path("part7/", views.part7_view, name='part7'),
    path("part8/", views.part8_view, name='part8'),
    path("contact/", views.contact_view, name='contact'),
]
