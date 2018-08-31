# djangomultitenancy
* Django multitenancy 
### Requirement :
```
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"


[requires]

python_version = "3.6"


[packages]

django = "==2.0.5"
django-tenant-schemas = "*"
djangorestframework = "*"
django-tenants = "*"
"python3-openid" = "*"
```

```
mkdir djangotenancy2
cd djangotenancy2
pipenv install
pipenv shell
django-admin.py startproject djangotenancy
cd djangotenancy
python manage.py startapp customers
```

``
ctrl+shift+t
``
```
sudo -u postgres createdb irfan2
sudo -u postgres createdb latihan2
sudo -u postgres psql
grant all privileges on database belajar4 to irfan;
```
```
python manage.py makemigrations customers
python manage.py migrate_schemas --shared
python manage.py shell 
```

```
from customers.models import Client, Domain

### create your first real tenant
tenant = Client(schema_name='tenant1',
name='Fonzy Tenant',
paid_until='2014-12-05',
on_trial=True)
tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

### Add one or more domains for the tenant
domain = Domain()
domain.domain = 'tenant.my-domain.com' # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()
```