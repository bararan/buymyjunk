from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Item, Image
from .forms import PostItem, ImageFormSet
from profiles.models import Profile
from django.db.utils import IntegrityError

# Create your views here.

class ItemsListView(ListView):
    model = Item
    template_name = 'items/main.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/detail.html'

def item_detail_view(req, pk):
    item = get_object_or_404(Item, id=pk)
    item_form = PostItem(
        req.POST or None,
        req.FILES or None,
        instance = item,
    )
    image_form = ImageFormSet(
        req.POST or None,
        req.FILES or None,
        queryset = item.get_images(),
        
    )
    if req.method == 'POST':
        redir = False
        if item_form.is_valid():
            redir = True
            item_form.save()
        if image_form.is_valid():
            redir = True
            imgs = image_form.save(commit=False)
            for img in imgs:
                try:
                    img.save()
                except IntegrityError:
                    img.item = item
                    img.save()
        if redir:
            item_form = PostItem()
            image_form = ImageFormSet()
            return HttpResponseRedirect(str(pk))
    context = {
        'object': item,
        'item_form': item_form,
        'image_form': image_form,
    }
    return render(req, 'items/detail.html', context)

def all_items_view(req):
    object_list = Item.objects.all()
    seller = None
    item_form = PostItem(
        req.POST or None,
        req.FILES or None
    )
    image_form = ImageFormSet(
        req.POST or None,
        req.FILES or None,
        queryset=Image.objects.none()
    )
    context = {
        'object_list': object_list,
        'item_form': item_form,
        'image_form': image_form
    }
    if req.method == 'POST':
        seller = get_object_or_404(Profile, user=req.user)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.seller = seller
            item.save()
            if image_form.is_valid():
                imgs = image_form.save(commit=False)
                for img in imgs:
                    img.item = item
                    img.save()
            message = f"You have successfully posted {item.title}"
            messages.add_message(req, messages.SUCCESS, message)
            return HttpResponseRedirect('.')
    return render(req, 'items/main.html', context)

def delete_item_view(req, pk):
    if req.method=='POST':
        itm = Item.objects.filter(id=pk)
        title = itm[0].title
        itm.delete()
    else:
        print('Not deleting on a GET')
    message = f"You have deleted {title}"
    messages.add_message(req, messages.INFO, message)
    return HttpResponseRedirect('/')
