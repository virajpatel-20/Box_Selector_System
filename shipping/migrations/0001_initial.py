from django.db import migrations


def create_default_boxes(apps, schema_editor):
    Box = apps.get_model("shipping", "Box")

    default_boxes = [
        {
            "name": "Small Box",
            "length_cm": 20,
            "width_cm": 20,
            "height_cm": 10,
            "max_weight_kg": 2,
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
            "name": "Extra Large Box",
            "length_cm": 80,
            "width_cm": 60,
            "height_cm": 40,
            "max_weight_kg": 20,
            "cost": 140,
        },
        {
            "name": "TV Box",
            "length_cm": 120,
            "width_cm": 80,
            "height_cm": 20,
            "max_weight_kg": 25,
            "cost": 180,
        },
    ]

    for box in default_boxes:
        Box.objects.get_or_create(
            name=box["name"],
            defaults=box
        )


def remove_default_boxes(apps, schema_editor):
    Box = apps.get_model("shipping", "Box")

    Box.objects.filter(
        name__in=[
            "Small Box",
            "Medium Box",
            "Large Box",
            "Extra Large Box",
            "TV Box",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(
            create_default_boxes,
            remove_default_boxes,
        ),
    ]