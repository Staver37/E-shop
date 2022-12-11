from django.urls import path
from .views import *

import django.views.static import serve
import django.conf.urls import url
# list of app routes
urlpatterns = [
    path('',homePage),
    path('products',catalogPage),
    path('products/seed',seedData),
    path('buy', buyProduct),
    path('decreasesProd', decreasesProductInBag),
    path('deleteBag', deleteBag),
    path('product/details',viewProduct),
    path('cart',viewBag),  
    path('checkout',checkOut),      
    path('order-confirm',confirmOrdedr),   
    path('create-payment-intent',CreatePaymentIntent),   
    path('payment-completed',completePayment), 
    path('contact', coontact_view),
    path('sent-message', sendMessage),



    
    # admin routes
    path('admin/product/add/form', addProductForm),
    path('admin/product/add/submit', saveProduct),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
