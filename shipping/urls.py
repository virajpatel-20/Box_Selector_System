from django.urls import path
from .views import home

from .views import ProductListCreateView, BoxListCreateView, OrderListCreateView, RecommendBoxView

urlpatterns = [
    path("products/", ProductListCreateView.as_view()),

    path("boxes/", BoxListCreateView.as_view()),

    path("orders/", OrderListCreateView.as_view()),

    path("recommend-box/", RecommendBoxView.as_view()),
    
    path("", home, name="home"),
]