from shipping.models import Box

def recommend_box(order):

    total_weight_kg = 0
    for item in order.orderitem_set.all():
        total_weight_kg += ( item.product.weight_kg * item.quantity )

    required_volume = 0

    for item in order.orderitem_set.all():
        product_volume = (item.product.length_cm * item.product.width_cm * item.product.height_cm)
        required_volume += ( product_volume * item.quantity )

    boxes = Box.objects.all()

    eligible_boxes = []

    for box in boxes:
        box_volume = (box.length_cm * box.width_cm * box.height_cm)
        if (total_weight_kg <= box.max_weight_kg and required_volume <= box_volume ):
            eligible_boxes.append(box)

    if not eligible_boxes:
        return None

    best_box = min(eligible_boxes,key=lambda box: 
                   (box.cost,(box.length_cm * box.width_cm * box.height_cm))
)
    return best_box