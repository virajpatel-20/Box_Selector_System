from django.test import TestCase

from .models import Product, Box, Order, OrderItem

from .services.box_selector import recommend_box

class BoxRecommendationTest(TestCase):

    def test_cheapest_box_selected(self):

        product = Product.objects.create(
            name="Laptop",
            length_cm=20,
            width_cm=10,
            height_cm=5,
            weight_kg=2
        )

        Box.objects.create(
            name="Expensive Box",
            length_cm=50,
            width_cm=50,
            height_cm=50,
            max_weight_kg=10,
            cost=100
        )

        cheap_box = Box.objects.create(
            name="Cheap Box",
            length_cm=30,
            width_cm=20,
            height_cm=10,
            max_weight_kg=5,
            cost=50
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1
        )

        recommended_box = recommend_box(order)

        self.assertEqual(
            recommended_box.name,
            "Cheap Box"
        )

    def test_no_box_available(self):

        product = Product.objects.create(
            name="Large Product",
            length_cm=100,
            width_cm=100,
            height_cm=100,
            weight_kg=50
        )

        Box.objects.create(
            name="Tiny Box",
            length_cm=10,
            width_cm=10,
            height_cm=10,
            max_weight_kg=5,
            cost=20
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1
        )

        recommended_box = recommend_box(order)

        self.assertIsNone(recommended_box)

    def test_weight_limit_exceeded(self):

        product = Product.objects.create(
            name="Heavy Product",
            length_cm=10,
            width_cm=10,
            height_cm=10,
            weight_kg=20
        )

        Box.objects.create(
            name="Light Box",
            length_cm=50,
            width_cm=50,
            height_cm=50,
            max_weight_kg=5,
            cost=50
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1
        )

        recommended_box = recommend_box(order)

        self.assertIsNone(recommended_box)

    def test_same_cost_smaller_box_selected(self):

        product = Product.objects.create(
            name="Book",
            length_cm=10,
            width_cm=10,
            height_cm=10,
            weight_kg=1
        )

        smaller_box = Box.objects.create(
            name="Smaller Box",
            length_cm=20,
            width_cm=20,
            height_cm=20,
            max_weight_kg=5,
            cost=50
        )

        Box.objects.create(
            name="Larger Box",
            length_cm=40,
            width_cm=40,
            height_cm=40,
            max_weight_kg=5,
            cost=50
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1
        )

        recommended_box = recommend_box(order)

        self.assertEqual(
            recommended_box.name,
            "Smaller Box"
        )