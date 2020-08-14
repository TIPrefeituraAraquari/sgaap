# coding=utf-8

from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import *



class DashboardView(View):
    template_name = 'dashboard.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{})