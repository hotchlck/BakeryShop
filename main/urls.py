from django.urls import path
from main.views import show_main, create_product, show_xml, show_json,  show_xml_by_id, show_json_by_id 
from main.views import register, login_user, logout_user, add_item, minus_item, remove_item


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
]