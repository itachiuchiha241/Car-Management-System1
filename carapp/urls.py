# This Is From and Improt ----------------

from django.urls import path
from carapp import views
from django.conf.urls.static import static
from Car_management_system import settings


# This is Urlpatterns For Page------------

urlpatterns = [
    path('home',views.home),
    path('about',views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sliderchange/', views.sliderchange, name='sliderchange'),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('myview',views.SimpleViews.as_view()),
    path('pdetails/<pid>',views.product_details),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('catfilter/<int:category_id>/', views.catfilternav, name='catfilternav'),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('remove/<int:cid>', views.remove, name='remove'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('pay/', views.no_orders, name='no_orders'),
    path('sendmail/<uname>',views.send_mail),
]




# This Is Debug Settings-----------------------

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)