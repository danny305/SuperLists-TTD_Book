from django.shortcuts import render,redirect
from .models import Item, List
from django.http import HttpResponse
# Create your views here.


#home_page = None
#def home_page(request):
    #return HttpResponse('<html><title>To-Do lists</title></html>')

def home_page(request):
    return render(request, 'home.html')     #simplified the homepage and moved all the lists stuff to /lists/ URL


    # if request.method == "POST":
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    #
    # items = Item.objects.all()
    # return render(request, 'home.html')






    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''
    # return render(request, 'home.html', {
    #     'new_item_text': new_item_text
    # })

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    #
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text',''),
    #  })

    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text',''),
    # })




def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

    # list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    # return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'] , list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')







def main_page(request):
    return render(request, 'home.html')

