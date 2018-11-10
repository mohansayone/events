from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from.forms import EntryForm

from.models import entry
#from django.http import HttpResponse
def index(request):
    entries = entry.objects.all()
    return render(request,'app/index.html',{'entries':entries})


def details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)

    if entry.author != request.user:
        raise Http404()

    return render(request, 'mapp/details.html', {'entry': entry})

def add(request):
    if request.method =='POST':
        pass
    else:
        form = EntryForm

        return render(request,'app/form.html',{'form':form})


# Create your views here.
