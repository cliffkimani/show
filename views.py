from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from models import Recipe, Food

from django.views.generic import ListView, CreateView, DetailView


def root(request):
    return HttpResponseRedirect("/cookbook")

class RecipeListView(ListView):
    model = Recipe
    paginate_by = 25

    def get_queryset(self):
        qs = Recipe.objects.all()
        return qs

class RecipeDetailView(DetailView):
    model = Recipe

    def get_object(self, queryset=None):
        recipe = super(RecipeDetailView, self).get_object(queryset=queryset)
        if 'scale' in self.request.GET:
            recipe.scale = float(self.request.GET['scale'])
            print "set scale to", recipe.scale
        else:
            recipe.scale = 1.0
        return recipe

class FoodConversionListView(ListView):
    model = Food

    def get_queryset(self):
        qs = Food.objects.with_conversions()
        return qs
    
    
class RecipeView(DetailView):
    model = Recipe

    def get_object(self, queryset=None):
        recipe = super(RecipeDetailView, self).get_object(queryset=queryset)
        if 'scale' in self.request.GET:
            recipe.scale = float(self.request.GET['scale'])
            print "set scale to", recipe.scale
        else:
            recipe.scale = 1.0
        return recipe
    
class CartDiscountCodeDeleteView(View):
    success_url = reverse_lazy('checkout_selection')

    def get_success_url(self):
        return self.success_url

    def post(self, *args, **kwargs):
        cart = get_or_create_cart(self.request)
        cart.cartdiscountcode_set.all().delete()
        return redirect(self.get_success_url())