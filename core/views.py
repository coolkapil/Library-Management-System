from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .permissions import StaffRequiredMixin


class SignUpView(CreateView):
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


class AdminSignUpView(CreateView):
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your Admin profile was created successfully"

  def form_valid(self, form):
    form.instance.is_staff =True
    return super(AdminSignUpView, self).form_valid(form)


class BookList(ListView): 
    model = Book


class BookDetail(StaffRequiredMixin, DetailView): 
    model = Book


class BookCreate(StaffRequiredMixin, CreateView): 
    model = Book

    fields = ["name", "auther", "category"]


class BookUpdate(StaffRequiredMixin, UpdateView): 
    model = Book

    fields = ["name", "auther", "category"]


class BookDelete(StaffRequiredMixin, DeleteView): 
    model = Book

    success_url = reverse_lazy('book-list')