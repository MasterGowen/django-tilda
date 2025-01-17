# coding: utf-8
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class TildaPage(models.Model):
    id = models.CharField(
        _("Page id"),
        max_length=50,
        primary_key=True,
        unique=True
    )

    title = models.CharField(
        _("Title"),
        max_length=100
    )

    html = models.TextField(
        _("HTML"),
        blank=True
    )

    images = models.TextField(
        _("Images"),
        blank=True
    )

    css = models.TextField(
        _("CSS"),
        blank=True
    )

    js = models.TextField(
        _("JS"),
        blank=True
    )

    synchronized = models.DateTimeField(
        _("Synchronized time"),
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        _("Created"),
        auto_now_add=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = _("page")
        verbose_name_plural = _("Tilda Pages")

    def get_images_list(self):
        if self.images:
            return [
                os.path.join('/media/tilda/images', r['to'])
                for r in eval(self.images)
            ]
        return []

    def get_css_list(self):
        if self.css:
            return [
                os.path.join('/media/tilda/css', r['to'])
                for r in eval(self.css)
            ]
        return []

    def get_js_list(self):
        if self.js:
            return [
                os.path.join('/media/tilda/js', r['to'])
                for r in eval(self.js)
            ]
        return []

    def _path_images_list(self):
        if self.images:
            return [
                os.path.join(settings.TILDA_MEDIA_IMAGES, r['to'])
                for r in eval(self.images)
            ]
        return []

    def _path_css_list(self):
        if self.css:
            return [
                os.path.join(settings.TILDA_MEDIA_CSS, r['to'])
                for r in eval(self.css)
            ]
        return []

    def _path_js_list(self):
        if self.js:
            return [
                os.path.join(settings.TILDA_MEDIA_JS, r['to'])
                for r in eval(self.js)
            ]
        return []

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
