from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField


class HomePage(Page):
    """Home Page Model."""

    templates = "home/home_page.html"

    hero_title = models.CharField(max_length=100, blank=False, null=True)
    hero_subtitle = models.CharField(max_length=300, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle")
    ]

    api_fields = [
        APIField('hero_title'),
        APIField('hero_subtitle'),
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
