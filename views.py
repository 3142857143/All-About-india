from django.shortcuts import render
from django.template.context import RequestContext
# Create your views here.
def home(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")
def page1(request):

    return render(request, "page1.html")
def demo(request):

    return render(request, "demograph.html")
def state_wise_literacy(request):

    return render(request, "state.html")
def sports(request):

    return render(request, "achievements_in_sports.html")
def science(request):
    return render(request, "science.html")
def georgraphy(request):
    return render(request, "geography.html")
def politics(request):
    return render(request, "politics.html")

def ap(request):
    return render(request, "ap.html")
def ap2(request):
    return render(request, "ap2.html")
def assam(request):
    return render(request, "assam.html")

def bihar(request):
    return render(request, "bihar.html")

def chhattisgarh(request):
    return render(request, "chhattisgarh.html")

def goa(request):
    return render(request, "goa.html")

def gujarat(request):
    return render(request, "gujarat.html")


def haryana(request):
    return render(request, "haryana.html")


def hp(request):
    return render(request, "hp.html")


def jharkhand(request):
    return render(request, "jharkhand.html")


def karnataka(request):
    return render(request, "karnataka.html")


def kerala(request):
    return render(request, "kerala.html")


def maharastra(request):
    return render(request, "maharastra.html")


def manipur(request):
    return render(request, "manipur.html")


def meghalaya(request):
    return render(request, "meghalaya.html")


def mizoram(request):
    return render(request, "mizoram.html")


def mp(request):
    return render(request, "mp.html")


def nagaland(request):
    return render(request, "nagaland.html")


def odisha(request):
    return render(request, "odisha.html")


def punjab(request):
    return render(request, "punjab.html")


def rajasthan(request):
    return render(request, "rajasthan.html")


def sikkim(request):
    return render(request, "sikkim.html")


def telangana(request):
    return render(request, "telangana.html")

def tn(request):
    return render(request, "tn.html")


def tripura(request):
    return render(request, "tripura.html")


def uk(request):
    return render(request, "uk.html")

def up(request):
    return render(request, "up.html")

def wb(request):
    return render(request, "wb.html")
