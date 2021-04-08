from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Funcionario, Servicos, Recurso
from .forms import ContatoForms


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForms
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'Mensagem enviada com sucesso!!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)