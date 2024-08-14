from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import ItemForm  # Import your form
from .models import Item

# Create your views here.
@login_required(login_url='/accounts/signin/')
def home(request):
    latest_item_list = Item.objects.order_by("-pub_date")
    context = {"latest_item_list": latest_item_list}
    return render(request, "app/home.html", context)

def new_task(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'app/new_task.html', {'form': form})

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item
    }
    # Render the template with the context data
    return render(request, 'app/detail.html', context)

def delete_task(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
    return redirect('home')

def edit_task(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            try:
                form.save()
                return redirect('detail', item_id=item.id)
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print(form.errors)  # Print form errors to debug
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'app/edit.html', {'form': form, 'item': item})
    
