# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import FormView
import JsonResponse


""" 
class Contact(self,request):
    def foo(request, ):
        return render_to_response("home.html",
                                  {"acounts": Account.objects.create_entity_using_attributes()})
"""


class ssss(JsonResponse.JSONResponseMixin, FormView):
    """
    A view that renders a template.  This view will also pass into the context
    any keyword arguments passed by the url conf.
    """

    def get(self, request, *args, **kwargs):
        context = {"aaaa": "Nguyen Van dadadad "}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {"aaaa": "Nguyen Van dadadad "}
        return self.render_to_response(context)
