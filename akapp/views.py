from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import AnkenForm, ShuhoForm
from django.urls import reverse_lazy,reverse
from .models import Anken, Shuho
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


class IndexView(TemplateView):
    template_name = 'akapp/index.html'


class AnkenListView(ListView):
    template_name = 'akapp/anken_list.html'
    model = Anken


class AnkenDetailView(DetailView):
    template_name = 'akapp/anken_detail.html'
    model = Anken


class AnkenCreateView(CreateView):
    template_name = 'akapp/anken_create.html'
    form_class = AnkenForm
    #success_url = reverse_lazy('akapp:anken_create_complete')
    success_url = reverse_lazy('akapp:anken_list')
    

class AnkenCreateCompleteView(TemplateView):
    template_name = 'akapp/anken_create_complete.html'


class AnkenUpdateView(UpdateView):
    template_name = 'akapp/anken_update.html'
    form_class = AnkenForm
    model = Anken
    #success_url = reverse_lazy('akapp:anken_list')

    def get_success_url(self):
        return reverse('akapp:anken_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        anken = form.save(commit=False)
        anken.updated_at = timezone.now()
        anken.save()
        return super().form_valid(form)


class AnkenDeleteView(DeleteView):
    template_name = 'akapp/anken_delete.html'
    model = Anken
    success_url = reverse_lazy('akapp:anken_list')


class ShuhoCreateView(CreateView):
    template_name = 'akapp/shuho_create.html'
    form_class = ShuhoForm
    #success_url = reverse_lazy('akapp:shuho_create_complete')
    
    def get_success_url(self):
        print(self.object.anken.pk)
        return reverse('akapp:anken_detail', kwargs={'pk': self.object.anken.pk})

            
class ShuhoCreateCompleteView(TemplateView):
    template_name = 'akapp/shuho_create_complete.html'


class ShuhoUpdateView(UpdateView):
    template_name = 'akapp/shuho_update.html'
    form_class = ShuhoForm
    model = Shuho
    #success_url = reverse_lazy('akapp:anken_list')
    
    def get_success_url(self):
        print(self.object.anken.pk)
        return reverse('akapp:anken_detail', kwargs={'pk': self.object.anken.pk})

    def form_valid(self, form):
        shuho = form.save(commit=False)
        shuho.updated_at = timezone.now()
        shuho.save()
        return super().form_valid(form)


class ShuhoDeleteView(DeleteView):
    template_name = 'akapp/shuho_delete.html'
    model = Shuho
    #success_url = reverse_lazy('akapp:anken_list')

    def get_success_url(self):
        print(self.object.anken.pk)
        return reverse('akapp:anken_detail', kwargs={'pk': self.object.anken.pk})


