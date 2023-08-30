# Django Random ID

A model base class which provides custom designed random integer primary keys
to you Django models.

## Installation

Run the following to install:
```python
pip install django_random_id
```

## Usage

The original way of creating and assigning primary keys in Django models

```python
from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=30, blank=False)

steve = CustomUser.objects.create(name="Steve")
bill = CustomUser.objects.create(name="Bill")
print(steve.id) 
# >>> '1'
print(bill.id) 
# >>> '2'
```

The primary keys are auto-incremental integers.

Now, let's see what you can do with `RandomIDModel`:

```python
from django.db import models
from django_random_id import RandomIDModel

class CustomUser(RandomIDModel):
    name = models.CharField(max_length=30, blank=False)

steve = CustomUser.objects.create(name="Steve")
bill = CustomUser.objects.create(name="Bill")
print(steve.id) 
# >>> '425291518806427'
print(bill.id) 
# >>> '607559381880556'
```

The Random primary ID is guaranteed to be unique.

By default the ID will be 12 digits long, but you can override this in
settings.py with the `RANDOM_ID_MODEL_LENGTH` setting.

`RandomIDModel` inherits directly from `models.Model`

## Developing Django Random ID Model

To install django_random_id, along with the tools you need to develop and 
run the tests, run the following in your virtual environment:

```bash
$ pip install -e .[dev]
```