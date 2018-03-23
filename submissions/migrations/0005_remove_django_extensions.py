# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_submission_staff_downloads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, db_index=True),
        ),
    ]
