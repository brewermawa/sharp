from .models import Category, ProductImages, ProductPrice, CategoryFilter, ProductFeautureValue


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
            "id": product.id,
            "name": product.name,
            "brand": product.brand,
            "image": productImage,
            "price": price,
            "notPrice": notPrice,
            "discount": discount
        }
        productList.append(product)

    return productList


def getCategoryFilters(category, products):
    filters = CategoryFilter.objects.filter(category=category)
    filterList = []

    productIds = []
    for product in products:
        productIds.append(product["id"])

    for filter in filters:
        values = []
        for product in products:
            try:
                filterValue = ProductFeautureValue.objects.get(product=product["id"], feauture=filter.filter)
                if filterValue.value.value not in values:
                    values.append(filterValue.value.value)
            except:
                pass

        print(f"{filterValue.feauture} - {values}")
        pass

        f = {
            "name": filter.filter.name,
            "type": filter.filterType,
            "values": values,
        }

        if len(f["values"]) > 1:
            filterList.append(f)

    for x in filterList:
        print(x)

    return filterList