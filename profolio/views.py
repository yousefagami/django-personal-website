from django.shortcuts import render

from .models import Profolio ,category 

from django.views.generic import ListView

# Create your views here.



class ProfolioList(ListView):
    model = Profolio
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = category.objects.all()
        return context
    
    