# Generated by Django 5.0.6 on 2024-07-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_book', '0003_remove_borrowmodel_account_alter_borrowmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowmodel',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
