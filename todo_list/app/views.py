from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import ItemForm
from .models import Item

LOGIN_URL = '/accounts/signin'

# Create your views here.
@login_required(login_url=LOGIN_URL)
def home(request):
    latest_item_list = Item.objects.filter(user=request.user).order_by("-pub_date")
    context = {"latest_item_list": latest_item_list}
    return render(request, "app/home.html", context)


@login_required(login_url=LOGIN_URL)
def new_task(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'app/new_task.html', {'form': form})

@login_required(login_url=LOGIN_URL)
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    context = {
        'item': item
    }
    # Render the template with the context data
    return render(request, 'app/detail.html', context)

@login_required(login_url=LOGIN_URL)
def delete_task(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id, user=request.user)
        item.delete()
    return redirect('home')

@login_required(login_url=LOGIN_URL)
def edit_task(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            try:
                form.save()
                return redirect('detail', item_id=item.id)
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print(form.errors)
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'app/edit.html', {'form': form, 'item': item})

@login_required(login_url=LOGIN_URL)
def completed_tasks(request):
    completed_tasks = Item.objects.filter(user=request.user, completed=True)
    return render(request, 'app/completed.html', context={"completed_jobs": completed_tasks})