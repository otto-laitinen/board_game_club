# Generated by Django 3.2.9 on 2021-12-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_app', '0002_auto_20211202_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='board_game',
            new_name='boardgame',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=3),
        ),
    ]