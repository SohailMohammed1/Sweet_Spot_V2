from django.shortcuts import render, redirect
from .models import Dessert
from .forms import DessertForm

def list_desserts(request):
    desserts = Dessert.objects.all()
    return render(request, 'desserts/dessert_list.html', {'desserts': desserts})

def add_dessert(request):
    if request.method == 'POST':
        form = DessertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_desserts')  
    else:
        form = DessertForm()

    return render(request, 'desserts/add_dessert.html', {'form': form})

def edit_dessert(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)
    if request.method == "POST":
        form = DessertForm(request.POST, instance=dessert)
        if form.is_valid():
            form.save()
            return redirect('list_desserts')
    else:
        form = DessertForm(instance=dessert)

    return render(request, 'desserts/edit_dessert.html', {'form': form})

def delete_dessert(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)
    dessert.delete()
    return redirect('list_desserts')

