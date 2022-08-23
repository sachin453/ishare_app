# Generated by Django 3.0.7 on 2020-06-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='College',
            field=models.CharField(choices=[('IITR', 'IIT Roorkee'), ('IITG', 'IIT Guwahati'), ('IITK', 'IIT Kanpur'), ('IITBBS', 'IIT Bhubaneswar'), ('IIT (BHU)', 'IIT (BHU) Varanasi'), ('IITJMU', 'IIT Jammu'), ('IITD', 'IIT Delhi'), ('IITI', 'IIT Indore'), ('IITDH', 'IIT Dharwad'), ('IITKGP', 'IIT kharagpur'), ('IITM', 'IIT Madras'), ('IITMandi', 'IIT Mandi'), ('IITP', 'IIT Patna'), ('IITGoa', 'IIT Goa'), ('IITBH', 'IIT Bhilai'), ('IITJ', 'IIT Jodhpur'), ('IITGN', 'IIT Gandhinagar'), ('IITB', 'IIT Bombay'), ('IITRPR', 'IIT Ropar'), ('IITH', 'IIT Hyderabad'), ('IITPKD', 'IIT Palakkad'), ('IIT(ISM)', 'IIT (ISM) Dhanbad'), ('IITTP', 'IIT Tirupati')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Bicycle', 'Bicycle'), ('Books&Sports', 'Books&Sports'), ('Others', 'Others'), ('Furniture', 'Furniture'), ('Mobiles', 'Mobiles'), ('Electronics', 'Electronics')], max_length=100),
        ),
    ]