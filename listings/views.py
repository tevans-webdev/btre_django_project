from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def indexPage(request):
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listingPage(request):
    return render(request, 'listings/listing.html')


def searchPage(request):
    return render(request, 'listings/search.html')
