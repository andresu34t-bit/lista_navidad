# 🚀 Desplegar en Render - Guía Rápida

## ✅ Archivos Preparados

Ya he creado todos los archivos necesarios:
- ✅ `requirements.txt` - Con gunicorn, whitenoise, psycopg2-binary
- ✅ `build.sh` - Script de construcción
- ✅ `render.yaml` - Configuración automática
- ✅ `settings.py` - Configurado para producción

---

## 🎯 Pasos para Desplegar

### 1. Subir Cambios a GitHub

```bash
git add .
git commit -m "feat: Configurar para despliegue en Render"
git push origin main
```

### 2. Configurar en Render

1. Ve a https://dashboard.render.com/
2. Haz clic en **"New +"** → **"Web Service"**
3. Conecta tu repositorio de GitHub
4. Selecciona `lista_navidad`

### 3. Configuración del Servicio

Render debería detectar automáticamente la configuración de `render.yaml`, pero verifica:

**Build Command:**
```bash
./build.sh
```

**Start Command:**
```bash
gunicorn lista_navidad.wsgi:application
```

**Environment Variables:**
- `SECRET_KEY`: (Render lo genera automáticamente)
- `DEBUG`: `False`
- `PYTHON_VERSION`: `3.11.0`

### 4. Crear Base de Datos (Opcional)

Si quieres usar PostgreSQL en lugar de SQLite:

1. En Render Dashboard, clic en **"New +"** → **"PostgreSQL"**
2. Nombre: `lista-navidad-db`
3. Copia la **Internal Database URL**
4. En tu Web Service, agrega variable de entorno:
   - Key: `DATABASE_URL`
   - Value: (pega la URL de la base de datos)

### 5. Deploy

1. Haz clic en **"Create Web Service"**
2. Render comenzará a construir y desplegar
3. Espera 5-10 minutos

---

## 🔧 Solución de Problemas

### Error: "gunicorn: command not found"
✅ **YA SOLUCIONADO** - Agregué gunicorn a requirements.txt

### Error: "No module named 'whitenoise'"
✅ **YA SOLUCIONADO** - Agregué whitenoise a requirements.txt

### Error: "Permission denied: ./build.sh"
Solución:
```bash
chmod +x build.sh
git add build.sh
git commit -m "fix: Hacer build.sh ejecutable"
git push origin main
```

### Error: "Static files not found"
✅ **YA SOLUCIONADO** - Configuré whitenoise y STATIC_ROOT

### Error: "Database connection failed"
- Si usas SQLite: No necesitas base de datos externa
- Si usas PostgreSQL: Verifica que DATABASE_URL esté configurada

---

## 📝 Después del Deploy

### 1. Crear Superusuario

En Render Dashboard:
1. Ve a tu servicio
2. Clic en **"Shell"** (en el menú lateral)
3. Ejecuta:
```bash
python manage.py createsuperuser
```

### 2. Verificar la Aplicación

Tu app estará disponible en:
```
https://lista-navidad.onrender.com
```

(O el nombre que hayas elegido)

### 3. Configurar Dominio Personalizado (Opcional)

1. En Render Dashboard → Settings
2. Scroll hasta "Custom Domain"
3. Agrega tu dominio
4. Configura DNS según las instrucciones

---

## 🎯 Comandos Útiles en Render Shell

```bash
# Ver logs
python manage.py check

# Migrar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Colectar archivos estáticos
python manage.py collectstatic --no-input

# Abrir shell de Django
python manage.py shell
```

---

## 💰 Costos

- **Plan Gratuito**: 
  - 750 horas/mes
  - Se duerme después de 15 min de inactividad
  - Perfecto para demos y proyectos personales

- **Plan Starter ($7/mes)**:
  - Siempre activo
  - Sin límite de horas
  - Mejor rendimiento

---

## 🔄 Actualizaciones Futuras

Para actualizar tu app:

1. Hacer cambios localmente
2. Commit y push a GitHub:
```bash
git add .
git commit -m "Descripción de cambios"
git push origin main
```

3. Render detecta el push y redespliega automáticamente

---

## 📊 Monitoreo

En Render Dashboard puedes ver:
- **Logs**: Logs en tiempo real
- **Metrics**: CPU, memoria, requests
- **Events**: Historial de deploys
- **Shell**: Acceso a terminal

---

## ⚡ Optimizaciones

### 1. Agregar Persistent Disk (para SQLite)

Si usas SQLite y quieres que los datos persistan:

1. En Render Dashboard → Settings
2. Scroll hasta "Disks"
3. Add Disk:
   - Name: `data`
   - Mount Path: `/opt/render/project/src/data`
   - Size: 1 GB

4. Actualiza settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/opt/render/project/src/data/db.sqlite3',
    }
}
```

### 2. Configurar Health Check

En Render Dashboard → Settings → Health Check Path:
```
/admin/login/
```

---

## 🎉 ¡Listo!

Tu aplicación Django está desplegada en Render.

**URLs importantes:**
- App: https://tu-app.onrender.com
- Admin: https://tu-app.onrender.com/admin/
- Dashboard: https://dashboard.render.com/

---

## 📞 Soporte

- [Render Docs](https://render.com/docs)
- [Render Community](https://community.render.com/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

¡Feliz despliegue! 🚀
