# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_submission_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='staff_downloads',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
