# Generated by Django 4.2.5 on 2023-10-02 13:33

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_activelearning_cumulatednumdata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='data',
            field=picklefield.fields.PickledObjectField(default='default data', editable=False),
        ),
        migrations.AddField(
            model_name='dataset',
            name='labels',
            field=picklefield.fields.PickledObjectField(default='default labels', editable=False),
        ),
    ]