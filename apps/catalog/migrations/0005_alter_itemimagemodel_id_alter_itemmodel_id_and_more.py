# Generated by Django 5.1.1 on 2024-12-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_itemimagemodel_id_alter_itemmodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimagemodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
