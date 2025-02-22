from django.db import migrations
from django.forms.models import model_to_dict


def transfer_data(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    for old_profile in OldProfile.objects.all():
        profile_data = model_to_dict(old_profile)

        if 'user' in profile_data:
            try:
                profile_data['user'] = User.objects.get(id=profile_data['user'])
            except User.DoesNotExist:
                profile_data['user'] = None

        NewProfile.objects.create(**profile_data)


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
