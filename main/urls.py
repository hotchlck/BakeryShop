from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-item/<int:id_item>/', add_item, name='add_item'),
    path('minus-item/<int:id_item>/', minus_item,name='minus_item'),
    path('remove-item<int:id_item>/', remove_item, name='remove_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('decrement_ajax/', decrement_ajax, name="decrement_ajax"),
    path('increment_ajax/', increment_ajax, name="increment_ajax"),
    path('delete_ajax/', delete_ajax, name='delete_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]