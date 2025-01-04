from blog.models import Post
from modeltranslation.translator import TranslationOptions, register


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
