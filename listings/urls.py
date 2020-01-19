from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='listings'),
    path('<int:listing_id>', views.listingPage, name='listing'),
    path('search', views.searchPage, name='search')
]
