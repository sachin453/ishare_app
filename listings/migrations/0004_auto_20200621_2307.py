# Generated by Django 3.0.7 on 2020-06-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200621_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='College',
            field=models.CharField(choices=[('IIT (BHU)', 'IIT (BHU) Varanasi'), ('IITKGP', 'IIT kharagpur'), ('IITM', 'IIT Madras'), ('IITK', 'IIT Kanpur'), ('IITJMU', 'IIT Jammu'), ('IITP', 'IIT Patna'), ('IITBBS', 'IIT Bhubaneswar'), ('IITD', 'IIT Delhi'), ('IITI', 'IIT Indore'), ('IITR', 'IIT Roorkee'), ('IITJ', 'IIT Jodhpur'), ('IITDH', 'IIT Dharwad'), ('IITG', 'IIT Guwahati'), ('IITMandi', 'IIT Mandi'), ('IITRPR', 'IIT Ropar'), ('IITTP', 'IIT Tirupati'), ('IITB', 'IIT Bombay'), ('IITH', 'IIT Hyderabad'), ('IITBH', 'IIT Bhilai'), ('IITGoa', 'IIT Goa'), ('IITGN', 'IIT Gandhinagar'), ('IITPKD', 'IIT Palakkad'), ('IIT(ISM)', 'IIT (ISM) Dhanbad')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Bicycle', 'Bicycle'), ('Mobiles', 'Mobiles'), ('Others', 'Others'), ('Electronics', 'Electronics')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=100),
        ),
    ]
