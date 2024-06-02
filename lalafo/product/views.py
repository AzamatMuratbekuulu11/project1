from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'product'

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.GET.get('category')
        search_query = self.request.GET.get('q')

        if category:
            queryset = queryset.filter(category__id=category)

        if search_query:
            queryset = queryset.filter(product_name__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')