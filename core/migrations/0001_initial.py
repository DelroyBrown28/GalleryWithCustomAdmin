# Generated by Django 3.1.4 on 2021-04-29 10:04

import blocks.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('index_page_content', wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add a title', required=False)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Additional Text', required=False))])), ('full_richtext', blocks.blocks.RichtextBlock()), ('art_cards', wagtail.core.blocks.StructBlock([('gallery_block_title', wagtail.core.blocks.RichTextBlock(required=True)), ('art_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title_of_picture', wagtail.core.blocks.CharBlock(help_text='Name of Art Piece', max_length=40, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('picture_description', wagtail.core.blocks.RichTextBlock(max_length=200, required=True)), ('button_to_site_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_to_external_URL', wagtail.core.blocks.URLBlock(help_text='Here, you can link to an external website', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Text that will be displayed on the button', max_length=25, required=True))])))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('cta_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=False))])), ('large_jumbotron', wagtail.core.blocks.StructBlock([('jumbotron_title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('jumbotron_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('jumbotron_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('jumbotron_button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('jumbotron_button_url', wagtail.core.blocks.URLBlock(required=False)), ('jumbotron_button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=False))])), ('navbar', wagtail.core.blocks.StructBlock([('nav_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('navbar_link_text_1', wagtail.core.blocks.CharBlock(help_text='Name of Art Piece', max_length=40, required=True)), ('navbar_link_1', wagtail.core.blocks.PageChooserBlock(required=False)), ('navbar_link_text_2', wagtail.core.blocks.CharBlock(help_text='Name of Art Piece', max_length=40, required=True)), ('navbar_link_2', wagtail.core.blocks.PageChooserBlock(required=False)), ('navbar_link_text_3', wagtail.core.blocks.CharBlock(help_text='Name of Art Piece', max_length=40, required=True)), ('navbar_link_3', wagtail.core.blocks.PageChooserBlock(required=False))])))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
