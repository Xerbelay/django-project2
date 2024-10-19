from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden


def product_detail(request, product_id): 
    products = ['cucumber', 'tomato', 'carrot', 'lettuce', 'potato', 'onion', 'garlic', 'pepper', 'broccoli']
    if product_id in range(0, len(products)):
        return HttpResponse(products[product_id], status=200)
    else:
        return HttpResponseNotFound("Product not found", status=404)
def check_availability(request, quantity):
    if (quantity > 0):
        return HttpResponse("Product is available", status=200)
    if(quantity == 0):
        return HttpResponse("The product is missing", status=204)
    else:
        return HttpResponseBadRequest("quantity must be positive", status=400)

