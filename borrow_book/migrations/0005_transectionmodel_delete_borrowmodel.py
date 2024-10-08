# Generated by Django 5.0.6 on 2024-07-07 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accountmodel_user'),
        ('book', '0004_alter_bookmodel_image'),
        ('borrow_book', '0004_alter_borrowmodel_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='accounts.accountmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='BorrowModel',
        ),
    ]
