from django.contrib import admin
from . models import Customer, Product, Feature, Review, Order, OrderItem, UpdateOrder,Contact, CheckoutDetail

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CheckoutDetail)
admin.site.register(UpdateOrder)
admin.site.register(Contact)
#admin.site.register(Category)