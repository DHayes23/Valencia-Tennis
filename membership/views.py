from django.shortcuts import render, redirect, reverse, get_object_or_404,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Membership, MembershipType
from .forms import MembershipForm


@login_required
def application(request):
    """ Submits a membership application """

    if request.method == 'POST':
        form = MembershipForm(request.POST)
        try:
            if form.is_valid():
                application_form = form.save(commit=False)
                application_form.user = request.user
                form.save()
                messages.success(request, 'Membership application sent! You will be contacted regarding your membership within 5 working days.')
                return redirect(reverse('profile'))

            else:
                messages.error(request, 'Failed to submit membership application. Please check the form for missing fields.')
        except Exception as e:
            messages.error(request, 'You have already submitted a membership application!')
            print(e)
            return redirect(reverse('profile'))
    else:
        form = MembershipForm()
        
    template = 'membership/application.html'
    context = {
        'form': form,
    }

    return render(request, template, context)