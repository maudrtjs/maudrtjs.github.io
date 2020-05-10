from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from search.models import Sheet
from .forms import ContactForm, SheetForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView


class ListScores(ListView):
    model = Sheet
    context_object_name = "list_sheets"
    template_name = "search/scores_list.html"
    paginate_by = 30

class ListScores_by_cat(ListView):
    model = Sheet
    template_name = "search/scores_list_by.html"
    context_object_name = "list_sheets"
    paginate_by = 30
    def get_queryset(self):
        return Sheet.objects.filter(style=self.kwargs['category'].capitalize())
    def get_context_data(self, **kwargs):
        context = super(ListScores_by_cat, self).get_context_data(**kwargs)
        context['types'] = str('style: ' + self.kwargs['category'].capitalize())
        return context

class ListScores_by_compositor(ListView):
    model = Sheet
    template_name = "search/scores_list_by.html"
    context_object_name = "list_sheets"
    paginate_by = 30
    def get_queryset(self):
        return Sheet.objects.filter(compositor=self.kwargs['compositor'])
    def get_context_data(self, **kwargs):
        context = super(ListScores_by_compositor, self).get_context_data(**kwargs)
        context['types'] = str('compositor: ' + self.kwargs['compositor'])
        return context

class ReadScore(DetailView):
    context_object_name = "sheet"
    model = Sheet
    template_name = "search/read.html"

    def get_object(self):
        score = super(ReadScore, self).get_object()
        score.popularity += 1
        score.save()
        return

class EditScore(FormView):
    template_name = 'search/edit_score.html'
    form_class = SheetForm
    succes_url = 'search/scores_list'

    def form_valid(self, form):
        return super().form_valid(form)


def home(request):
    return render(request, 'search/home.html', {})

def edit_score(request, id):
    sheet = get_object_or_404(Sheet, id=id)
    form = SheetForm(request.POST or None, instance=sheet)
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        title = form.cleaned_data['title']
        compositor = form.cleaned_data['compositor']
        pdf_link = form.cleaned_data['pdf_link']
        composition_date = form.cleaned_data['composition_date']
        send = True
        form.save()
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'search/edit_score.html', locals())


def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        mail_contact = form.cleaned_data['mail_contact']
        send_back = form.cleaned_data['send_back']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        send = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'search/contact.html', locals())

def add_score(request):
    form = SheetForm(request.POST or None)
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        title = form.cleaned_data['title']
        compositor = form.cleaned_data['compositor']
        pdf_link = form.cleaned_data['pdf_link']
        composition_date = form.cleaned_data['composition_date']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        send = True
        form.save()
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'search/add_score.html', locals())

