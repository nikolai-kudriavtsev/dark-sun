from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import RegistrationForm

# from .forms import RegistrationForm, CreateOrderForm
# from django.contrib.auth.decorators import login_required


def index(req):
    objects = Object.objects.all()
    return render(req, "index.html", context={"objects": objects})


#
def registration(req):
    return render(req, "registration/registration.html")


#
#
def reg_ajax(req):
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
    else:
        form = RegistrationForm()
    return render(req, "registration/reg_ajax.html", context={"form": form})


def catalog(req, categorys=None):
    # services = Service.objects.all().filter(amount__gte=0).order_by("-id")
    # for p in service:
    #     row = Cart.objects.all().filter(user=req.user, products=p.id)
    #     # p.cart = row[0].amount if len(row) else 0
    return render(
        req,
        "catalog.html",
        context={
            "services": services,
            "categorys": categorys,
            "order": order,
            "filtr": filtr,
        },
    )


def product_detail(req, id):
    product = service.objects.get(pk=id)
    row = Cart.objects.all().filter(user=req.user, product=id)
    # product.cart = row[0].amount if len(row) else 0
    return render(req, "product_detail.html", context={"service": service})


# @login_required
# def cart_add(reg, id):
#     row = Cart.objects.all().filter(user=reg.user, product=id)
#     product = Product.objects.get(pk=id)
#     if len(row):
#         row = row[0]
#         if row.amount >= product.amount:
#             return HttpResponse("<span class='error-count'>Больше добавить нельзя! в корзине %s шт</span>" % row.amount)
#         row.amount += 1
#     else:
#         row = Cart(user=reg.user, product=product, amount=1)
#         row.save()
#     return HttpResponse("в корзине %s шт" % row.amount)
#
# @login_required
# def cart_add(reg, id):
#     row = Cart.objects.all().filter(user=reg.user, product=id)
#     if len(row):
#         row = row[0]
#         if row.amount:
#             row.amount -= 1;
#             row.save() if row.amount else row.delete()
#             return HttpResponse("в корзине %s шт" % row.amount)
#         return HttpResponse("<span class='error-count'>Товар в корзине отсутствует!</span>")
