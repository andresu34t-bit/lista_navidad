# 🚀 Guía de Despliegue - Lista Navideña

## Opciones de Despliegue

### 1. Heroku (Recomendado para principiantes)

#### Requisitos
- Cuenta en Heroku
- Heroku CLI instalado

#### Archivos Adicionales Necesarios

**Procfile**
```
web: gunicorn lista_navidad.wsgi
```

**runtime.txt**
```
python-3.11.0
```

**Actualizar requirements.txt**
```
Django==5.2.7
gunicorn
whitenoise
psycopg2-binary
dj-database-url
```

#### Pasos

1. **Instalar Heroku CLI**
```bash
# Windows
# Descargar desde https://devcenter.heroku.com/articles/heroku-cli

# Mac
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

2. **Login en Heroku**
```bash
heroku login
```

3. **Crear aplicación**
```bash
heroku create lista-navidad-app
```

4. **Configurar variables de entorno**
```bash
heroku config:set SECRET_KEY='tu-secret-key-aqui'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='lista-navidad-app.herokuapp.com'
```

5. **Agregar PostgreSQL**
```bash
heroku addons:create heroku-postgresql:mini
```

6. **Actualizar settings.py**
```python
import dj_database_url

# En settings.py
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Agregar esto
    # ... resto del middleware
]
```

7. **Deploy**
```bash
git add .
git commit -m "Preparar para Heroku"
git push heroku main
```

8. **Migrar base de datos**
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

9. **Abrir aplicación**
```bash
heroku open
```

---

### 2. PythonAnywhere

#### Pasos

1. **Crear cuenta en PythonAnywhere**
   - Ve a https://www.pythonanywhere.com/
   - Crea una cuenta gratuita

2. **Subir código**
```bash
# En PythonAnywhere Bash console
git clone https://github.com/andresu34t-bit/lista_navidad.git
cd lista_navidad
```

3. **Crear entorno virtual**
```bash
mkvirtualenv --python=/usr/bin/python3.10 lista_navidad
pip install -r requirements.txt
```

4. **Configurar Web App**
   - Ve a "Web" tab
   - Add a new web app
   - Manual configuration
   - Python 3.10
   - Configura paths

5. **WSGI Configuration**
```python
import os
import sys

path = '/home/tuusuario/lista_navidad'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'lista_navidad.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

6. **Configurar Static Files**
   - URL: /static/
   - Directory: /home/tuusuario/lista_navidad/staticfiles/

7. **Recargar aplicación**

---

### 3. Railway

#### Pasos

1. **Crear cuenta en Railway**
   - Ve a https://railway.app/

2. **Conectar GitHub**
   - New Project → Deploy from GitHub repo

3. **Configurar variables**
```
SECRET_KEY=tu-secret-key
DEBUG=False
ALLOWED_HOSTS=*.railway.app
```

4. **Railway se encarga del resto automáticamente**

---

### 4. Render

#### Pasos

1. **Crear cuenta en Render**
   - Ve a https://render.com/

2. **New Web Service**
   - Conecta tu repositorio de GitHub

3. **Configuración**
```
Build Command: pip install -r requirements.txt
Start Command: gunicorn lista_navidad.wsgi:application
```

4. **Variables de entorno**
```
SECRET_KEY=tu-secret-key
DEBUG=False
PYTHON_VERSION=3.11.0
```

5. **Agregar PostgreSQL**
   - New → PostgreSQL
   - Conectar a tu web service

---

## Configuración de Producción

### settings.py para Producción

```python
import os
from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Database
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

---

## Checklist Pre-Despliegue

- [ ] SECRET_KEY en variable de entorno
- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS configurado
- [ ] Base de datos de producción configurada
- [ ] Static files configurados
- [ ] requirements.txt actualizado
- [ ] .gitignore configurado
- [ ] Migraciones aplicadas
- [ ] Superusuario creado
- [ ] Pruebas realizadas

---

## Comandos Útiles

### Colectar archivos estáticos
```bash
python manage.py collectstatic --noinput
```

### Ver logs (Heroku)
```bash
heroku logs --tail
```

### Ejecutar comandos remotos (Heroku)
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Reiniciar aplicación (Heroku)
```bash
heroku restart
```

---

## Solución de Problemas

### Error: DisallowedHost
- Verifica ALLOWED_HOSTS en settings.py
- Agrega el dominio de tu aplicación

### Error: Static files no cargan
- Ejecuta `collectstatic`
- Verifica STATIC_ROOT y STATIC_URL
- Asegúrate de tener whitenoise instalado

### Error: Database
- Verifica DATABASE_URL
- Ejecuta migraciones
- Verifica credenciales

### Error: 500 Internal Server Error
- Revisa logs
- Verifica SECRET_KEY
- Asegúrate de que DEBUG=False

---

## Monitoreo

### Heroku
```bash
heroku logs --tail
heroku ps
heroku run python manage.py shell
```

### Métricas
- Tiempo de respuesta
- Uso de memoria
- Errores 500
- Tráfico

---

## Backup

### Base de Datos (Heroku)
```bash
heroku pg:backups:capture
heroku pg:backups:download
```

### Archivos
- Usar S3 o similar para media files
- Backup regular de código en GitHub

---

## Actualizaciones

1. Hacer cambios localmente
2. Probar localmente
3. Commit y push a GitHub
4. Deploy automático o manual según plataforma

```bash
git add .
git commit -m "Descripción de cambios"
git push origin main
```

---

## Costos Estimados

| Plataforma | Plan Gratuito | Plan Básico |
|------------|---------------|-------------|
| Heroku | Limitado | $7/mes |
| PythonAnywhere | Sí | $5/mes |
| Railway | $5 crédito | $5/mes |
| Render | Sí | $7/mes |

---

## Recomendaciones

1. **Desarrollo**: Usar SQLite
2. **Producción**: Usar PostgreSQL
3. **Static Files**: Usar WhiteNoise o CDN
4. **Media Files**: Usar S3 o similar
5. **Monitoreo**: Configurar alertas
6. **Backup**: Automatizar backups diarios

---

¡Buena suerte con tu despliegue! 🚀
