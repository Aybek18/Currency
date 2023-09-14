import json

from django.db import migrations


def import_data(app, _):
    Currency = app.get_model("currency", "Currency")
    with open("currency/migrations/data.json") as f:
        currencies = json.load(f)
        for _, currency in currencies.items():
            Currency.objects.create(name=currency["description"], code=currency["code"])


class Migration(migrations.Migration):
    dependencies = [
        ("currency", "0001_initial"),
    ]

    operations = [migrations.RunPython(import_data, migrations.RunPython.noop)]
