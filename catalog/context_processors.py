from .models import Announcement, BusinessInfo, Category, Menu

def business(request):
    return {
        "phone": BusinessInfo.objects.all()[:1].get().phone,
        "info": BusinessInfo.objects.all()[:1].get(),
        "announcement": Announcement.objects.all()[:1].get().announcement,
        "categories": Category.objects.filter(parent_category__name="home"),
        "menu": Menu.objects.all().order_by("order"),
    }