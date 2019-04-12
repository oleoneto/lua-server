# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals

# System Views...
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from guardian.shortcuts import get_objects_for_user


@method_decorator(login_required, name='get')
class DashboardView(TemplateView):
    """
    :param request: HTTP request object
    :return: render(request, template, context)
    """
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Dashboard | Lua | Learning Management System'
        return context
