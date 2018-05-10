# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_remove_django_extensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='points_earned',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]),
        ),
        migrations.AlterField(
            model_name='score',
            name='points_possible',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]),
        ),
    ]
