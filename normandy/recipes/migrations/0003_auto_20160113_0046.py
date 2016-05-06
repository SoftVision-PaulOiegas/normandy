# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 00:46
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import normandy.recipes.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20151231_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='count_limit',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='locale',
            field=normandy.recipes.fields.LocaleField(blank=True, choices=[('en-US', 'English (US)'), ('uz', 'Uzbek'), ('ga', 'Irish'), ('lv', 'Latvian'), ('brx', 'Bodo'), ('sat', 'Santali'), ('is', 'Icelandic'), ('he', 'Hebrew'), ('wo', 'Wolof'), ('ko', 'Korean'), ('ta-IN', 'Tamil (India)'), ('ta', 'Tamil'), ('ln', 'Lingala'), ('ga-IE', 'Irish'), ('ha', 'Hausa'), ('eo', 'Esperanto'), ('kk', 'Kazakh'), ('hy-AM', 'Armenian'), ('pt-PT', 'Portuguese (Portugal)'), ('ja', 'Japanese'), ('pa', 'Punjabi'), ('mk', 'Macedonian'), ('hi', 'Hindi'), ('mai', 'Maithili'), ('az', 'Azerbaijani'), ('lo', 'Lao'), ('xh', 'Xhosa'), ('sa', 'Sanskrit'), ('nl', 'Dutch'), ('fr', 'French'), ('cak', 'Kaqchikel'), ('ne-NP', 'Nepali'), ('fi', 'Finnish'), ('kn', 'Kannada'), ('nr', 'Ndebele, South'), ('bg', 'Bulgarian'), ('pt-BR', 'Portuguese (Brazilian)'), ('nso', 'Northern Sotho'), ('sl', 'Slovenian'), ('hi-IN', 'Hindi (India)'), ('ee', 'Ewe'), ('bn-BD', 'Bengali (Bangladesh)'), ('es-ES', 'Spanish (Spain)'), ('hr', 'Croatian'), ('ig', 'Igbo'), ('oc', 'Occitan (Lengadocian)'), ('mi', 'Maori (Aotearoa)'), ('gu-IN', 'Gujarati (India)'), ('ach', 'Acholi'), ('tn', 'Tswana'), ('ku', 'Kurdish'), ('cs', 'Czech'), ('sk', 'Slovak'), ('mr', 'Marathi'), ('sr-Latn', 'Serbian'), ('lij', 'Ligurian'), ('lg', 'Luganda'), ('bs', 'Bosnian'), ('de-CH', 'German (Switzerland)'), ('mn', 'Mongolian'), ('ss', 'Siswati'), ('ve', 'Venda'), ('ak', 'Akan'), ('ms', 'Malay'), ('csb', 'Kashubian'), ('et', 'Estonian'), ('en-NZ', 'English (New Zealand)'), ('ar', 'Arabic'), ('es', 'Spanish'), ('x-testing', 'Testing'), ('en-ZA', 'English (South African)'), ('son', 'Songhai'), ('ca', 'Catalan'), ('ml', 'Malayalam'), ('ru', 'Russian'), ('cy', 'Welsh'), ('gl', 'Galician'), ('be', 'Belarusian'), ('uk', 'Ukrainian'), ('sw', 'Swahili'), ('dsb', 'Lower Sorbian'), ('ff', 'Fulah'), ('eu', 'Basque'), ('hsb', 'Upper Sorbian'), ('de', 'German'), ('en-GB', 'English (British)'), ('sv-SE', 'Swedish'), ('hu', 'Hungarian'), ('te', 'Telugu'), ('or', 'Oriya'), ('nn-NO', 'Norwegian (Nynorsk)'), ('ast', 'Asturian'), ('nb-NO', 'Norwegian (Bokmål)'), ('lt', 'Lithuanian'), ('id', 'Indonesian'), ('it', 'Italian'), ('bn-IN', 'Bengali (India)'), ('gu', 'Gujarati'), ('rw', 'Kinyarwanda'), ('gn', 'Guarani'), ('th', 'Thai'), ('tsz', 'Purépecha'), ('en-AU', 'English (Australian)'), ('el', 'Greek'), ('tt-RU', 'Tatar'), ('zu', 'Zulu'), ('fy-NL', 'Frisian'), ('my', 'Burmese'), ('km', 'Khmer'), ('af', 'Afrikaans'), ('ka', 'Georgian'), ('tr', 'Turkish'), ('de-DE', 'German (Germany)'), ('ks', 'Kashmiri'), ('en-CA', 'English (Canadian)'), ('st', 'Southern Sotho'), ('ca-valencia', 'Catalan (Valencian)'), ('gd', 'Gaelic (Scotland)'), ('ro', 'Romanian'), ('br', 'Breton'), ('bm', 'Bambara'), ('pa-IN', 'Punjabi (India)'), ('am-et', 'Amharic'), ('sah', 'Sakha'), ('es-AR', 'Spanish (Argentina)'), ('ja-JP-mac', 'Japanese'), ('as', 'Assamese'), ('es-CL', 'Spanish (Chile)'), ('an', 'Aragonese'), ('sq', 'Albanian'), ('ts', 'Tsonga'), ('fa', 'Persian'), ('vi', 'Vietnamese'), ('de-AT', 'German (Austria)'), ('zh-TW', 'Chinese (Traditional)'), ('zh-CN', 'Chinese (Simplified)'), ('fj-FJ', 'Fijian'), ('sr', 'Serbian'), ('tl', 'Tagalog'), ('ta-LK', 'Tamil (Sri Lanka)'), ('mg', 'Malagasy'), ('yo', 'Yoruba'), ('ur', 'Urdu'), ('da', 'Danish'), ('la', 'Latin'), ('fur-IT', 'Friulian'), ('pl', 'Polish'), ('sr-Cyrl', 'Serbian'), ('si', 'Sinhala'), ('dbg', 'Debug Robot'), ('es-MX', 'Spanish (Mexico)'), ('rm', 'Romansh'), ('kok', 'Konkani')], default='', max_length=255),
        ),
    ]
