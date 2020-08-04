# coding=utf-8

from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import *



class HomeView(View):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{})