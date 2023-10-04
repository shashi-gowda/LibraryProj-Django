from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Language, Book, Author, BookInstance
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required #for function based views
from django.contrib.auth.mixins import LoginRequiredMixin #for class based views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books':num_books,
        'num_instance':num_instances,
        'num_instances_avail':num_instances_avail
    }
    return render(request, 'catalog/index.html', context=context)

class BookCreate(LoginRequiredMixin, CreateView): #looks for model_form.html --> book_form.html
    model = Book
    fields = '__all__'

class BookDetail(DetailView): #looks for model_detail.html --> book_detail.html
    model = Book

@login_required #for restricting access to people who not logged in
def my_view(request): 
    return render(request, 'catalog/my_view.html')


class SignUpView(CreateView):
    form_class = UserCreationForm   #overwriting
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'

class CheckedOutBooksByUserView(LoginRequiredMixin, ListView):
    #list all BookInstances But i will filter based off currently logged in user session
    model = BookInstance
    template_name='catalog/profile.html'
    paginate_by=5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)