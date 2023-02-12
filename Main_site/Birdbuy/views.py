from django.shortcuts import render
from Birdbuy.models import Birds, Content


def index(request):
    Birds_item = Birds.objects.all()
    products = []
    for product in Birds_item:
        products.append({
            "image": product.image,
            "product_name": product.breed,
            "price": product.price
        })
    Content_item = Content.objects.all()[0]
    content = {
        "table_of_contents": {
            "number_phone": Content_item.number_phone,
            "cart_sum_enable": Content_item.cart_sum_enable,
            "cart_sum": Content_item.cart_sum,
        },
        'products': products
    }
    return render(request, 'main/Birdbuy.html', content)
