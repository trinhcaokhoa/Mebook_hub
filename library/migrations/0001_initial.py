# Generated by Django 2.2.7 on 2022-03-12 21:41

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
            name='LibraryBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('author', models.CharField(default='author', max_length=50)),
                ('cover', models.ImageField(null=True, upload_to='covers/')),
                ('file', models.FileField(null=True, upload_to='doc/')),
                ('owner', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyBook',
            fields=[
                ('librarybook_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.LibraryBook')),
            ],
            bases=('library.librarybook',),
        ),
    ]
