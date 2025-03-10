from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.shortcuts import render
from app.forms import CarrosForm
from app.models import Carros


# Create your views here.
def home(request):
    return render(request, 'index.html')


def form(request):
    data = {'form': CarrosForm()}
    return render(request, 'form.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def edit(request, pk):
    data = {'db': Carros.objects.get(pk=pk)}
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {'db': Carros.objects.get(pk=pk)}
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {'db': Carros.objects.get(pk=pk)}
    return render(request, 'view.html', data)


def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def home(request):
    data = {}
    all = Carros.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)


