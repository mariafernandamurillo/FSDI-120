# Generated by Django 4.2.3 on 2023-07-25 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('date_picker', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, default=None, null=True)),
                ('thumbnail', models.ImageField(default=None, null=True, upload_to='event_images')),
                ('category', models.CharField(choices=[('Arts', 'Arts'), ('Music', 'Music'), ('Health', 'Health'), ('Games', 'Games'), ('Sports', 'Sports'), ('Technology', 'Technology'), ('Support', 'Support')], default='Arts', max_length=128)),
                ('modality', models.CharField(choices=[('Online', 'Online'), ('In-person', 'In-person')], default='Virtual', max_length=128)),
                ('city', models.CharField(choices=[('Los Angeles', 'Los Angeles'), ('San Francisco', 'San Francisco'), ('San Diego', 'San Diego'), ('Sacramento', 'Sacramento'), ('San Jose', 'San Jose'), ('Oakland', 'Oakland'), ('Long Beach', 'Long Beach'), ('Fresno', 'Fresno'), ('Bakersfield', 'Bakersfield'), ('Santa Ana', 'Santa Ana')], default='San Diego', max_length=128)),
                ('location', location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.status'),
        ),
    ]
