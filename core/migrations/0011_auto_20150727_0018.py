# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='event_page_content',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='event_page_content',
        ),
        migrations.AddField(
            model_name='eventpagecontent',
            name='coaches',
            field=models.ManyToManyField(blank=True, to='core.Coach', related_name='event_page_contents'),
        ),
        migrations.AddField(
            model_name='eventpagecontent',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='core.Sponsor', related_name='event_page_contents'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='photo',
            field=models.ImageField(help_text='For best display keep it square', blank=True, upload_to='event/coaches/', null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='twitter_handle',
            field=models.CharField(help_text='No @, No http://, just username', blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(help_text='The best would be 356 x 210px', blank=True, upload_to='event/cities/', null=True),
        ),
        migrations.AlterField(
            model_name='eventpagemenu',
            name='url',
            field=models.CharField(help_text='http://djangogirls.org/city/<the value you enter here>', max_length=255),
        ),
        migrations.AlterField(
            model_name='postmortem',
            name='applicants_count',
            field=models.IntegerField(verbose_name='Number of applicants'),
        ),
        migrations.AlterField(
            model_name='postmortem',
            name='attendees_count',
            field=models.IntegerField(verbose_name='Number of attendees'),
        ),
        migrations.AlterField(
            model_name='postmortem',
            name='comments',
            field=models.TextField(null=True, blank=True, verbose_name='Anything else you want to share with us?'),
        ),
        migrations.AlterField(
            model_name='postmortem',
            name='costs',
            field=models.TextField(help_text='We only collect this information for statistics and advice for future organizers.', blank=True, verbose_name='What are the total costs of the event?', null=True),
        ),
        migrations.AlterField(
            model_name='postmortem',
            name='discovery',
            field=models.TextField(null=True, blank=True, verbose_name='What was the most important thing you discovered during the workshop?'),
        ),
        migrations.AlterField(
            model_name='postmortem',
            name='feedback',
            field=models.TextField(null=True, blank=True, verbose_name='How we can make DjangoGirls better?'),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(upload_to='stories/'),
        ),
    ]
