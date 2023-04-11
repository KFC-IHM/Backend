from django.conf import settings
from django.core.management import BaseCommand

from database.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            for user,password in settings.ADMINS:
                CustomUser.objects.create_superuser(user, password)
                print('Admin account created for {} with password {}'.format(user, password))
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
