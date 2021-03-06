# coding=UTF-8
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_markdown.models import MarkdownField

from app.models.generic import BaseModel


@python_2_unicode_compatible
class Blog(BaseModel):

    label = models.CharField(default=None, null=True, blank=True,
                             max_length=200,
                             help_text=_(u"A recall of what this blog "
                                         u"contains (language independant)"),
                             verbose_name=_(u'Label'),)
    date_publication = models.DateTimeField(default=datetime.datetime.now,
                                            null=True, blank=True,
                                            verbose_name=_(u'Publication date'))
    ordre_si_top = models.IntegerField(
        null=True, blank=True, default=None,
        help_text=_(u'Priority: the higher first '
                    u'("2" is <b>before</b> "1" and so on...).<br />'
                    u'<b>Let it blank if you don\'t want this blog on top</b>'),
        verbose_name=_(u'If this blog is always on top'))

    date_envoi_newsletter = models.DateField(
        null=True, blank=True, default=None,
        help_text=_(u"Blank = never sent. "
                    u"If the date is older than now it will be sent tonight."),
        verbose_name=_(u'Add this blog into the newsletter'))

    def __str__(self):
        if not self.label:
            return u''
        return (self.label[:95] + '...') if len(self.label) > 90 else self.label

    class Meta(BaseModel.Meta):
        ordering = ['date_v_debut']
        verbose_name = _(u'Blog')
        verbose_name_plural = _(u'Blogs')


@python_2_unicode_compatible
class BlogTraduit(BaseModel):
    blog = models.ForeignKey(Blog, default=None, null=True, blank=True,
                             on_delete=models.CASCADE)
    locale = models.CharField(default=None, null=True, blank=True,
                              max_length=2,
                              help_text=_(u"Blog's locale (en, fr, ...)"),
                              verbose_name=_(u"Blog's locale"),)
    title = models.CharField(default=None, null=True, blank=True,
                             max_length=200,
                             help_text=_(u"Blog's title"),
                             verbose_name=_(u'Title'),)
    content = MarkdownField(default=None, null=True, blank=True,
                            help_text=_(u"Blog's content"),
                            verbose_name=_(u'Content'),)

    def description(self):
        a = u'{} / {} - {}'.format(
            self.locale if self.locale else _(u'no locale'),
            self.title if self.locale else _(u'no title'),
            self.content if self.content else _(u'no content yet'),)
        return (a[:95] + '...') if len(a) > 90 else a

    def __str__(self):
        return self.description().strip()

    class Meta(BaseModel.Meta):
        ordering = ['date_v_debut']
        verbose_name = _(u'Blog-translated content')
        verbose_name_plural = _(u'Blogs-translated')
