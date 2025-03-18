from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Item, Image
from messaging.models import Thread
from .forms import PostItem, ImageFormSet
from messaging.forms import MessageForm
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
    from_user = req.user
    to_user = item.seller.user
    is_own_item = from_user == to_user 
    item_form, image_form, message_form = None, None, None
    if is_own_item:
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
                for img in item.get_images():
                    if str(img.id) in req.POST:
                        assert req.POST.get(str(img.id)) == 'on'
                        img.delete()
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
    else:
        message_form = MessageForm(
            data = req.POST or None,
            initial={
            "subject": f"Inquiry about {item.title}"
            })
        if req.method == 'POST':
            if message_form.is_valid():
                message = message_form.save(commit=False)
                # thread = Thread()
                # thread.subject  = message.subject
                # thread.users.add(req.user)
                # thread.users
                # thread.save()
                message.sender = req.user
                message.recipient = item.seller.user
                # message.thread = thread
                message.save()
                messages.add_message(req, messages.SUCCESS, 'Your message has been sent.')
            else:
                messages.add_message(req, messages.ERROR, "Your message could not be sent. Please try again.")               
    context = {
        'object': item,
        'item_form': item_form,
        'message_form': message_form,
        'image_form': image_form,
        'is_own_item': is_own_item,
    }
    return render(req, 'items/detail.html', context)

def all_items_view(req):
    object_list = Item.objects.all()
    if req.user.is_anonymous:
        seller = None
    else:
        seller = get_object_or_404(Profile, user=req.user)
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
        'image_form': image_form,
        'seller': seller
    }
    if req.method == 'POST':
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
