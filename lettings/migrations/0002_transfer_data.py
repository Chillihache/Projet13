from django.db import migrations
from django.forms.models import model_to_dict


def transfer_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    for old_address in OldAddress.objects.all():
        address_data = model_to_dict(old_address)
        new_address = NewAddress.objects.create(**address_data)

        for old_letting in OldLetting.objects.filter(address=old_address):
            letting_data = model_to_dict(old_letting)
            letting_data['address'] = new_address
            NewLetting.objects.create(**letting_data)


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
