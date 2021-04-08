from django.http.response import HttpResponse, JsonResponse
from datetime import datetime, timedelta
from api.models import Product
from api.models import Category

# def hello(request):
#     return HttpResponse('<h1>hello view function</h1>')


# def show_time(request, hours):
    
#     current_time = datetime.now() + timedelta(hours=hours)
#     return HttpResponse(f'<h1>TIME: {current_time}</h1>')

# products =[
#    {
#     'id': 1,
#     'url': "https://www.amazon.com/dp/031653708X/ref=s9_acsd_ri_bw_c2_x_2_i?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-10&pf_rd_r=FNBS39QDRJGF08VFV62H&pf_rd_t=101&pf_rd_p=d2e01c79-7462-4300-8d41-3633536344dc&pf_rd_i=283155",
#     'name': 'The Pegan Diet',
#     'price': 14.99,
#     'description': '21 Practical Principles for Reclaiming Your Health in a Nutritionally Confusing World',
#     'image': "https://images-na.ssl-images-amazon.com/images/I/51P89RJVqzL._SX320_BO1,204,203,200_.jpg",
#     'rating': "5/5",
#     'likes': 0,
#     'id_uniq': 0
#   },
#   {
#     'id': 1,
#     'url': "https://www.amazon.com/dp/031653708X/ref=s9_acsd_ri_bw_c2_x_2_i?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-10&pf_rd_r=FNBS39QDRJGF08VFV62H&pf_rd_t=101&pf_rd_p=d2e01c79-7462-4300-8d41-3633536344dc&pf_rd_i=283155",
#     'name': 'The Pegan Diet',
#     'price': 14.99,
#     'description': '21 Practical Principles for Reclaiming Your Health in a Nutritionally Confusing World',
#     'image': "https://images-na.ssl-images-amazon.com/images/I/51P89RJVqzL._SX320_BO1,204,203,200_.jpg",
#     'rating': "5/5",
#     'likes': 0,
#     'id_uniq': 1
#   },
#   {
#     'id': 1,
#     'url': "https://www.amazon.com/dp/031653708X/ref=s9_acsd_ri_bw_c2_x_2_i?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-10&pf_rd_r=FNBS39QDRJGF08VFV62H&pf_rd_t=101&pf_rd_p=d2e01c79-7462-4300-8d41-3633536344dc&pf_rd_i=283155",
#     'name': 'The Pegan Diet',
#     'price': 14.99,
#     'description': '21 Practical Principles for Reclaiming Your Health in a Nutritionally Confusing World',
#     'image': "https://images-na.ssl-images-amazon.com/images/I/51P89RJVqzL._SX320_BO1,204,203,200_.jpg",
#     'rating': "5/5",
#     'likes': 0,
#     'id_uniq': 3
#   }
  
    
# ]
#def product_list(request):
  #  return HttpResponse('<h1>This is product list </h1>')

#def product_detail(request, product_id):
    #return HttpResponse(f'<h1>This is product detail page : {product_id} </h1>')

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return  JsonResponse({'message': str(e)}, status =400)
    return JsonResponse(product.to_json())

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as p:
        return  JsonResponse({'message': str(p)}, status =400)
    return JsonResponse(category.to_json())
