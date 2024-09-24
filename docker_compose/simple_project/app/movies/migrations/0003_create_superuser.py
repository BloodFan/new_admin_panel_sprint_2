import os
from os.path import join
from pathlib import Path

from django.contrib.auth.models import User
from django.db import migrations
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = join(BASE_DIR, "dev", "env", ".env")

load_dotenv(dotenv_path)


def create_superuser(apps, schema_editor):
    username = os.environ.get("SUPERUSER_USERNAME")
    email = os.environ.get("SUPERUSER_EMAIL")
    password = os.environ.get("SUPERUSER_PASSWORD")

    if username and email and password:
        User.objects.create_superuser(username=username, email=email, password=password)


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_alter_personfilmwork_role"),
    ]

    operations = [
        migrations.RunPython(create_superuser, migrations.RunPython.noop),
    ]
