from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listings = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listings
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')
