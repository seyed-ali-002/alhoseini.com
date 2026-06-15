from modeltranslation.translator import TranslationOptions, translator, register
from .models import Post


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ['title', 'body', 'summary']
