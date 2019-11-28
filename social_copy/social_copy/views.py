from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = '../../social_copy1/templates/index.html'


class TestPage(TemplateView):
    template_name = '../../social_copy1/templates/test.html'


class ThanksPage(TemplateView):
    template_name = '../../social_copy1/templates/thanks.html'
