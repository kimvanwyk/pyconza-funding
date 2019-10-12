# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-12 14:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('S', 'Submitted'), ('U', 'Under Consideration'), ('G', 'Request Granted'), ('A', 'Offer accepted'), ('R', 'Funding not granted'), ('N', 'Offer not accepted'), ('C', 'Canceled')], default='S', max_length=1)),
                ('motivation', models.TextField(blank=True, help_text='Your motivation for why PyCon ZA should fund you')),
                ('country', models.TextField(blank=True, help_text='Which country will you be travelling from?')),
                ('travel_amount', models.DecimalField(decimal_places=2, default=0, help_text='Total Budget for travel (ZAR)', max_digits=10)),
                ('accomodation_amount', models.DecimalField(decimal_places=2, default=0, help_text='Total Budget for accomodation while attending PyCon ZA (ZAR)', max_digits=10)),
                ('food_amount', models.DecimalField(decimal_places=2, default=0, help_text='Total Budget for food while attending PyCon ZA (ZAR)', max_digits=10)),
                ('local_transport_amount', models.DecimalField(decimal_places=2, default=0, help_text='Total Budget for local transport expenses while attending PyCon ZA (ZAR)', max_digits=10)),
                ('other_expenses', models.DecimalField(decimal_places=2, default=0, help_text='Total Budget for other expenses (ZAR). Please explain these expenses in your budget description.', max_digits=10)),
                ('own_contribution', models.DecimalField(decimal_places=2, default=0, help_text='Amount you can contribute towards attending PyCon ZA (ZAR)', max_digits=10)),
                ('offered', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('budget_description', models.TextField(blank=True, help_text='Additional information and explanations about your budget figures (assumptions made, special considerations, etc.)')),
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='funding', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'funding application',
                'verbose_name_plural': 'funding applications',
                'permissions': (('view_all_applications', 'Can view all funding applications'), ('make_application_decisions', 'Can update the application status and make offers')),
            },
        ),
    ]