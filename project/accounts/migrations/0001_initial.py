# Generated by Django 3.0.5 on 2020-08-19 22:22

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('pronouns', models.CharField(max_length=20)),
                ('id_num', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clinician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('thumb', models.ImageField(default='default.png', max_length=300, upload_to='main_nav/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='GameTrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', max_length=300, upload_to='main_nav/%Y/%m/%d')),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('coords', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(blank=True, null=True), size=4)),
                ('clinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Clinician')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_data', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True), size=10)),
                ('computed_nums', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True), size=1)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('game_train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.GameTrain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ImageSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('clinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Clinician')),
                ('pic1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic1', to='accounts.Image')),
                ('pic10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic10', to='accounts.Image')),
                ('pic11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic11', to='accounts.Image')),
                ('pic2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic2', to='accounts.Image')),
                ('pic3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic3', to='accounts.Image')),
                ('pic4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic4', to='accounts.Image')),
                ('pic5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic5', to='accounts.Image')),
                ('pic6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic6', to='accounts.Image')),
                ('pic7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic7', to='accounts.Image')),
                ('pic8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic8', to='accounts.Image')),
                ('pic9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic9', to='accounts.Image')),
            ],
        ),
        migrations.CreateModel(
            name='ClientClinicianLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Client')),
                ('clinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Clinician')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='clinician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Clinician'),
        ),
    ]
