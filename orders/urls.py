from django.conf.urls import url, include
from django.contrib import admin

from orders import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^checkout/$', views.checkout, name= 'checkout'),
]
