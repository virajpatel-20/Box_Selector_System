from django.shortcuts import render
from .forms import ProductForm
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Box, Order, OrderItem
from .serializers import ProductSerializer
from .serializers import BoxSerializer
from .serializers import OrderSerializer

from .models import Order
from .services.box_selector import recommend_box


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BoxListCreateView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class =BoxSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

from .services.box_selector import recommend_box

class RecommendBoxView(APIView):

    def post(self, request):

        order_id = request.data.get("order_id")

        try:
            order = Order.objects.get(id=order_id)

        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"},
                status=404
            )

        box = recommend_box(order)

        if not box:
            return Response(
                {"error": "No suitable box found"},
                status=404
            )

        return Response({
            "recommended_box": box.name,
            "cost": box.cost
        })

def home(request):

    recommendation = None
    order = None

    if request.method == "POST":

        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            product = product_form.save()
            order = Order.objects.create()
            quantity = product_form.cleaned_data["quantity"]

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

            # Get recommendation
            recommendation = recommend_box(order)

    else:

        product_form = ProductForm()

    context = {
        "product_form": product_form,
        "recommendation": recommendation,
        "order": order,
    }
    

    return render(
        request,
        "shipping/home.html",
        context
    )