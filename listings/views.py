from django.shortcuts import render


def indexPage(request):
    return render(request, 'listings/listings.html')


def listingPage(request):
    return render(request, 'listings/listing.html')


def searchPage(request):
    return render(request, 'listings/search.html')
