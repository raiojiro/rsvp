from django.shortcuts import render
from .models import Guest
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseForbidden

MAX_CAPACITY = 100

def home(request):
    if request.GET.get("invite_code") == "6yXtakjvRkQFiyqR":
        ontext = {'capacity_full': Guest.objects.count() >= MAX_CAPACITY}
        return render(request,'main.html')
    else:
        return HttpResponseForbidden("Invalid Invite Code")

@require_http_methods(["POST"])
def guests(request):
    pax = int(request.POST.get('pax', 0))
        
    request.session['pax'] = pax
    context = {"show_attendees_form": True,'attendee_range': range(pax)}
    return render(request,"guests.html", context)
        

@require_http_methods(["POST"])
def submit_attendee(request):
    if request.POST.getlist('attendee_names[]'):
        pax = request.session.get('pax')
        
        for guest in request.POST.getlist('attendee_names[]'):
            Guest.objects.create(name=guest)
        
        request.session['invite_code']="6yXtakjvRkQFiyqR"
        return render(request, 'main.html', {'success_message': "Thank you for your RSVP! We look forward to celebrating with you."})

# Create your views here.
