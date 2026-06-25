from django.core.management.base import BaseCommand
from shipping.models import Box


class Command(BaseCommand):
    help = "Insert default shipping boxes"

    def handle(self, *args, **kwargs):

        boxes = [

            {
                "name": "XS Box",
                "length_cm": 15,
                "width_cm": 15,
                "height_cm": 10,
                "max_weight_kg": 1,
                "cost": 25,
            },

            {
                "name": "Small Box",
                "length_cm": 25,
                "width_cm": 20,
                "height_cm": 15,
                "max_weight_kg": 3,
                "cost": 40,
            },

            {
                "name": "Medium Box",
                "length_cm": 40,
                "width_cm": 30,
                "height_cm": 20,
                "max_weight_kg": 5,
                "cost": 60,
            },

            {
                "name": "Large Box",
                "length_cm": 60,
                "width_cm": 40,
                "height_cm": 30,
                "max_weight_kg": 10,
                "cost": 90,
            },

            {
                "name": "XL Box",
                "length_cm": 80,
                "width_cm": 60,
                "height_cm": 40,
                "max_weight_kg": 20,
                "cost": 140,
            },

            {
                "name": "XXL Box",
                "length_cm": 100,
                "width_cm": 80,
                "height_cm": 50,
                "max_weight_kg": 35,
                "cost": 200,
            },

            {
                "name": "TV Box",
                "length_cm": 120,
                "width_cm": 80,
                "height_cm": 20,
                "max_weight_kg": 25,
                "cost": 180,
            },

            {
                "name": "Furniture Box",
                "length_cm": 150,
                "width_cm": 90,
                "height_cm": 70,
                "max_weight_kg": 50,
                "cost": 300,
            },

        ]

        created = 0

        for box in boxes:
            obj, was_created = Box.objects.get_or_create(
                name=box["name"],
                defaults=box
            )

            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{created} boxes added successfully."
            )
        )