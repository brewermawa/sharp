from .models import Category, ProductImages, ProductPrice


def getBreadCrumbs(category_id, breadCrumbs=[]):
    category = Category.objects.get(pk=category_id)
    
    breadCrumbs.append(category)

    if category.parent_category:
        getBreadCrumbs(category.parent_category.id, breadCrumbs)

    return breadCrumbs


def getProducts(products):
    productList = []

    for product in products:
        try:
            productImage = f"images/{ProductImages.objects.get(product=product, main=True).image}"
        except:
            productImage = ""

        try:
            price = ProductPrice.objects.get(product=product, active=True).final_price
            notPrice = product.price
            discount = ((notPrice - price) / notPrice)*100
        except:
            price = product.price
            notPrice = False
            discount = False

        product = {
            "name": product.name,
            "brand": product.brand,
            "image": productImage,
            "price": price,
            "notPrice": notPrice,
            "discount": discount
        }
        productList.append(product)

    return productList