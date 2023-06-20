from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Products, Comment
from .forms import CommentForm


# def test_translate(request):
#     result = _('Hello')
#     messages.warning(request, 'Fuck you ')
#     return render(request, 'products/test.html')


class ProductsListView(generic.ListView):
    # model = Products
    paginate_by = 8
    queryset = Products.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(SuccessMessageMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_message = _("Comment Successfully Add")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Products, id=product_id)
        obj.product = product
        return super().form_valid(form)




