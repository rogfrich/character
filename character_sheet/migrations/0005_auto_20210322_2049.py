# Generated by Django 3.1.7 on 2021-03-22 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character_sheet', '0004_auto_20210318_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight_lbs', models.DecimalField(decimal_places=2, max_digits=5)),
                ('modifying_ability', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponDamage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_dice', models.IntegerField(default=1)),
                ('type_dice', models.IntegerField(default=6)),
                ('damage_type', models.ManyToManyField(to='character_sheet.DamageType')),
                ('weapon', models.ManyToManyField(to='character_sheet.Weapon')),
            ],
        ),
        migrations.AddField(
            model_name='weapon',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='character_sheet.weaponcategory'),
        ),
    ]
