from django.db import models

from blocks import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (FieldPanel, PageChooserPanel,
                                            MultiFieldPanel,
                                            StreamFieldPanel,
                                            InlinePanel,
                                            FieldRowPanel)
from wagtail.images.edit_handlers import ImageChooserPanel


class Index(Page):
    template = 'index.html'
    
    index_page_content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('art_cards', blocks.ArtBlock()),
            ('cta', blocks.CTABlock()),
            ('large_jumbotron', blocks.LargeJumbotronBlock()),
            ('navbar', blocks.NavbarBlock()),
        ],
        null=True,
        blank=True
    )
    
    content_panels = Page.content_panels + [
        StreamFieldPanel("index_page_content"),
    ]

    

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
        


class ProductList(Page):
    template = 'cart/product_detail.html'
    
    product_page_content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('art_cards', blocks.ArtBlock()),
            ('cta', blocks.CTABlock()),
            ('large_jumbotron', blocks.LargeJumbotronBlock()),
            ('navbar', blocks.NavbarBlock()),
        ],
        null=True,
        blank=True
    )
    
    content_panels = Page.content_panels + [
        StreamFieldPanel("product_page_content"),
    ]

    class Meta:
        verbose_name = "Product List Page"

    