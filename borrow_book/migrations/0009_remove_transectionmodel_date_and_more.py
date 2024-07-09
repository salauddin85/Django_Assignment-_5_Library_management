# Generated by Django 5.0.6 on 2024-07-07 19:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_book', '0008_remove_transectionmodel_amount_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transectionmodel',
            name='date',
        ),
        migrations.AddField(
            model_name='transectionmodel',
            name='transaction_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transectionmodel',
            name='transaction_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='transectionmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
    ]
