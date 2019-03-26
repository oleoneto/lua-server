# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals

# System Views...
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    :param request: HTTP request object
    :return: render(request, template, context)
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Lua | Learning Management System for Teachers and Students'
        context['active'] = 'active'
        return context
