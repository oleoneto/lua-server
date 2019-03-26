# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals

# System Views...
from django.views.generic import TemplateView


class DocumentationView(TemplateView):
    """
    :param request: HTTP request object
    :return: render(request, template, context)
    """
    template_name = 'documentation/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Documentation | Lua | Learning Management System'
        context['active'] = 'active'
        return context
