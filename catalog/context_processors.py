from .models import Announcement, BusinessInfo, Category, Menu, FooterSection, FooterLink

def business(request):
    return {
        "announcement": Announcement.objects.all()[:1].get().announcement,
        "phone": BusinessInfo.objects.all()[:1].get().phone,
        "categories": Category.objects.filter(parent_category__name="home"),
        "info": BusinessInfo.objects.all()[:1].get(),
        "menu": Menu.objects.all().order_by("order"),
        "footerSections": FooterSection.objects.all(),
        "footerLinks": FooterLink.objects.all(),
    }