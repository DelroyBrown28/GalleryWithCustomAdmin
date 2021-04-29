from django.db import models

from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock



class NavbarBlock(blocks.StructBlock):
    nav_items = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('navbar_link_text_1', blocks.CharBlock(required=True, max_length=40, help_text="Name of Art Piece")),
                ('navbar_link_1', blocks.PageChooserBlock(required=False)),
                ('navbar_link_text_2', blocks.CharBlock(required=True, max_length=40, help_text="Name of Art Piece")),
                ('navbar_link_2', blocks.PageChooserBlock(required=False)),
                ('navbar_link_text_3', blocks.CharBlock(required=True, max_length=40, help_text="Name of Art Piece")),
                ('navbar_link_3', blocks.PageChooserBlock(required=False)),

            ]
        )
    )

    class Meta:
        template = 'blocks/navbar_block.html'
        icon = "edit"
        label = 'Navbar Options'



class TitleAndTextBlock(blocks.StructBlock):
    """Title and text."""

    title = blocks.CharBlock(required=False, help_text='Add a title')
    text = blocks.RichTextBlock(required=False, help_text='Additional Text')

    class Meta:
        template = 'cart/product_list.html'
        icon = "edit"
        label = 'Title & Text'
        


class RichtextBlock(blocks.RichTextBlock):


    class Meta:
        template = 'blocks/richtext_block.html'
        icon = 'doc-full'
        label = 'Full Richtext'

        

class ArtBlock(blocks.StructBlock):
    gallery_block_title = blocks.RichTextBlock(required=True)

    art_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title_of_picture', blocks.CharBlock(required=True, max_length=40, help_text="Name of Art Piece")),
                ('image', ImageChooserBlock(required=True)),
                ('picture_description', blocks.RichTextBlock(required=True, max_length=200)),
                ('button_to_site_page', blocks.PageChooserBlock(required=False)),
                ('button_to_external_URL', blocks.URLBlock(required=False, help_text='Here, you can link to an external website')),
                ('button_text', blocks.CharBlock(required=True, max_length=25, help_text='Text that will be displayed on the button')),

            ]
        )
    )

    class Meta:
        template = "blocks/art_block.html"
        icon = 'pencil'
        label = 'Art cards'


class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=100)
    text = blocks.RichTextBlock(required=True, features=['bold', 'italic'])
    cta_image = ImageChooserBlock(required=True)
    button_page = blocks.PageChooserBlock(required=False) 
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Learn More', max_length=40)



    class Meta:
        template = 'blocks/cta_block.html'
        icon = 'image'
        label = 'Call To Action'


class LargeJumbotronBlock(blocks.StructBlock):
    jumbotron_title = blocks.CharBlock(required=True, max_length=100)
    jumbotron_text = blocks.RichTextBlock(required=True, features=['bold', 'italic'])
    jumbotron_image = ImageChooserBlock(required=True)
    jumbotron_button_page = blocks.PageChooserBlock(required=False) 
    jumbotron_button_url = blocks.URLBlock(required=False)
    jumbotron_button_text = blocks.CharBlock(required=False, default='Learn More', max_length=40)
   
    class Meta:
        template = 'blocks/large_jumbotron_block.html'
        icon = 'image'
        label = 'Large Jumbotron'



class ExibitionDatesBlock(blocks.StructBlock):
    exibition_section_title = blocks.CharBlock(required=True, max_length=100)
    exibition_dates = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('city_or_town_location', blocks.CharBlock(required=True, max_length=40, help_text="Name of Art Piece")),
                ('venue', blocks.CharBlock(required=True, max_length=40, help_text="Name of Art Piece")),
                ('date', blocks.DateTimeBlock(required=True,help_text='The date of the show')),
                ('buy_tickets', blocks.URLBlock(required=False)),

            ]
        )
    )

    class Meta:
        template = 'blocks/exibition_dates_block.html'
        icon = 'clock'
        label = 'Date/Time'
