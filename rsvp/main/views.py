from django.shortcuts import render
from .models import User, Guest
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
        invite_code = request.session.get('invite_code')
        pax = request.session.get('pax')
        try:
            user = User.objects.get(invite_code = invite_code)
        except:
            return render(request,"main.html", {"error_message": "Invitation code not found"})
        
        for guest in request.POST.getlist('attendee_names[]'):
            user.guests.create(name=guest)
        
        user.code_used = True
        user.save()

        return render(request, 'main.html', {'success_message': "Thank you for your RSVP! We look forward to celebrating with you."})

# Create your views here.
