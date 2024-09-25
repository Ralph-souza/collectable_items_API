import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImageModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('url', models.URLField(blank=True, max_length=250, null=True)),
                ('label', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='LoanerModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'loaner',
                'verbose_name_plural': 'loaners',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('main_actor', models.CharField(blank=True, max_length=150, null=True)),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
                ('platform', models.CharField(blank=True, choices=[('nintendo_switch', 'Nintendo Switch'), ('pc', 'PC'), ('playstation', 'Playstation'), ('xbox', 'XBox')], default=None, max_length=150, null=True)),
                ('category', models.CharField(blank=True, choices=[('action_figures', 'Action Figures'), ('books', 'Books'), ('games', 'Games'), ('movies', 'Movies')], default=None, max_length=150, null=True)),
                ('media_type', models.CharField(blank=True, choices=[('bluray', 'Bluray'), ('book', 'Book'), ('comics', 'Comics'), ('digital', 'Digital'), ('dvd', 'DVD'), ('kindle', 'Kindle')], default=None, max_length=150, null=True)),
                ('launch_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'Available'), ('not_available', 'Not Available')], default=None, max_length=150, null=True)),
                ('loan_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.itemimagemodel')),
                ('loaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.loanermodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.usermodel')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='LoanHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.itemmodel')),
                ('loan_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaned_on', to='catalog.itemmodel')),
                ('loaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaner_name', to='catalog.loanermodel')),
                ('return_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='returned_on', to='catalog.itemmodel')),
            ],
            options={
                'verbose_name': 'history',
                'ordering': ('-return_date',),
            },
        ),
    ]
