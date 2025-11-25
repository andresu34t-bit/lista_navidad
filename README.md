# 🎄 Lista Navideña - Proyecto Django

Una aplicación web para organizar tu lista de regalos navideños con un diseño elegante en dorado y rosa.

## ✨ Características

- 🔐 Sistema completo de autenticación (registro e inicio de sesión)
- 🎁 Cada usuario debe crear su lista con exactamente 6 regalos (obligatorio)
- 💰 Límite de S/ 25.00 por regalo
- 🎯 Exactamente 6 regalos por usuario (obligatorio)
- ✅ Marcar regalos como recibidos
- 🎨 Diseño moderno y profesional con colores dorado y rosa
- 📱 Totalmente responsivo (móvil, tablet y desktop)
- 📊 Panel de administración con estadísticas completas (solo admin)
- 👥 Vista global de todas las listas de usuarios (solo admin)
- 📈 Gráficos de progreso y resúmenes por persona
- 🎯 Interfaz intuitiva y fácil de usar
- 🔒 Cada usuario solo ve y gestiona su propia lista

## 🚀 Instalación y Uso

### Requisitos
- Python 3.8 o superior
- Django 5.2.7 (ya instalado)

### Iniciar el servidor

```bash
python manage.py runserver
```

### Acceder a la aplicación

- **Página principal**: http://127.0.0.1:8000/
- **Registrarse**: http://127.0.0.1:8000/register/
- **Iniciar sesión**: http://127.0.0.1:8000/login/
  - Usuario de prueba: `admin`
  - Contraseña: `admin123`
- **Panel de Administración** (solo superusuario): http://127.0.0.1:8000/panel-admin/
- **Panel Django Admin**: http://127.0.0.1:8000/admin/

## 📱 Uso de la Aplicación

### Para nuevos usuarios:
1. **Registrarse**: 
   - Ve a http://127.0.0.1:8000/register/
   - Completa tu nombre completo, usuario, email y contraseña
   - Al registrarte, se crea automáticamente tu lista personal

2. **Crear tu Lista de Deseos**:
   - ⚠️ **OBLIGATORIO**: Debes agregar exactamente 6 regalos
   - Cada regalo debe costar máximo S/ 25.00
   - Describe cada regalo para que sepan qué te gustaría
   - El sistema te notificará hasta que completes los 6 regalos

### Funcionalidades principales:
1. **Mi Lista**: Ver tu lista personal de regalos deseados
2. **Agregar Regalos**: Haz clic en "➕ Agregar Regalo" (obligatorio completar 6)
3. **Marcar como Recibido**: Usa el botón "✓ Recibido" cuando recibas un regalo
4. **Eliminar Regalos**: Usa el botón "🗑️ Eliminar" para quitar regalos de tu lista
5. **Ver Estadísticas**: Revisa cuántos regalos tienes y el total de su valor

### Para superusuarios (Admin):
- **Panel Admin**: Accede al panel de administración para:
  - Ver todas las listas de todos los usuarios
  - Ver estadísticas globales
  - Gestionar personas y regalos
  - Ver resúmenes completos

## 🎨 Diseño

### Paleta de Colores
- **Dorado** (dominante): #d4af37, #f4c430
- **Rosa** (dominante): #ff69b4, #ff1493
- **Complementarios**: Blanco, crema, verde (estados), azul (información)

### Características del Diseño
- ✨ Gradientes suaves y modernos
- 🎯 Interfaz intuitiva y profesional
- 📱 Totalmente responsivo (móvil, tablet, desktop)
- 🎨 Animaciones sutiles y transiciones fluidas
- 🌟 Iconos emoji para mejor experiencia visual

## 📋 Reglas de Negocio

- Cada usuario tiene su propia lista personal de regalos
- **OBLIGATORIO**: Debes agregar exactamente 6 regalos (no más, no menos)
- Precio máximo por regalo: S/ 25.00
- El sistema te notificará constantemente hasta que completes los 6 regalos
- Los regalos marcados como recibidos aparecen con estilo tachado
- El sistema valida automáticamente los límites
- Solo puedes ver y gestionar tu propia lista (excepto admin)
- Al registrarte, automáticamente se crea tu lista personal
- Si eliminas un regalo, deberás agregar otro para mantener los 6

## 🛠️ Estructura del Proyecto

```
lista_navidad/          # Configuración del proyecto Django
regalos/                # Aplicación principal
├── models.py          # Modelos Persona y Regalo
├── views.py           # Vistas de la aplicación
├── forms.py           # Formularios
├── urls.py            # Rutas de la aplicación
├── admin.py           # Configuración del admin
└── templates/         # Plantillas HTML
    └── regalos/
        ├── base.html
        ├── lista_personas.html
        ├── detalle_persona.html
        ├── agregar_persona.html
        └── agregar_regalo.html
```

## 🎯 Funcionalidades Futuras (Opcionales)

- Exportar lista a PDF
- Compartir listas por email
- Categorías de regalos
- Búsqueda y filtros
- Modo oscuro

¡Feliz Navidad! 🎅🎄
# lista
# lista
# lista_navidad
# lista_navidad
# lista_navidad
# lista_navidad
# lista_navidad
# lista_navidad
# lista_navidad
# lista_navidad
