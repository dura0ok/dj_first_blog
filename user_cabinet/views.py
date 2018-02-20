from django.shortcuts import render, redirect
from .forms import CabForm
# Create your views here.
def cabinet(request):
    context = {
        'form': CabForm
    }
    if request.method == "POST":
        form = CabForm(request.POST, request.FILES, instance=request.user.client)
        if form.is_valid():
            form.author = request.user
            form.save()
            return redirect('/')
    else:
        form = CabForm()
    return render(request, 'cabinet.html', context=context)
