from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import AuthorForm,BookForm

# Create your views here.
def createBook(request):
    books=Book.objects.all()
    if request.method == "POST":
        form=BookForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/booklist')
    else:
        form = BookForm()
    return render(request,'admin/book.html', {'form':form ,'books':books})

def createAuthor(request):
    author=Author.objects.all()
    if request.method == "POST":
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=AuthorForm()
    return render(request,'admin/author.html',{'form':form , 'author':author})

def deleteAuthorView(request, book_id):
    book=Author.objects.get(id=book_id)
    if request.method == "POST":
            book.delete()
            return redirect('/')
    return render(request,'admin/deleteview.html', {'book':book})

def updateAuthorView(request,book_id):
    book=Author.objects.get(id=book_id)
    if request.method == 'POST':
        form=BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Author(book)
    return render(request,'admin/updateauthorview.html',{'form':form})


def listBook(request):
    books=Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admin/listbook.html',{'books':books,'page':page})

def detailsBook(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'admin/detailsview.html',{'book':book})

def updateBook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form=BookForm(request.POST ,request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/booklist')
    else:
        form=BookForm(instance=book)
    return render(request,'admin/updateview.html',{'form':form})

def deleteBook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('/booklist')
    return render(request,'admin/deleteview.html',{'book':book})

def SearchBook(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query)|Q(author__name__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}

    return render(request,'admin/search.html', context)


def home(request):
    return render(request,'admin/home.html')
