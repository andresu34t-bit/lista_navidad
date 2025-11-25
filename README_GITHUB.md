# 🎄 Lista Navideña - Aplicación Web Django

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Una elegante aplicación web para gestionar tu lista de regalos navideños con un diseño profesional en dorado y rosa.

[Demo](#-demo) • [Características](#-características) • [Instalación](#-instalación) • [Uso](#-uso) • [Capturas](#-capturas-de-pantalla)

</div>

---

## 📖 Descripción

Lista Navideña es una aplicación web moderna desarrollada con Django que permite a los usuarios crear y gestionar su lista personal de regalos deseados para Navidad. Con un diseño profesional y responsivo, la aplicación facilita la organización de regalos con límites de precio y cantidad.

## ✨ Características

### 🎁 Funcionalidades Principales
- **Sistema de Autenticación Completo**: Registro e inicio de sesión seguro
- **Lista Personal**: Cada usuario tiene su propia lista de hasta 6 regalos
- **Límite de Precio**: Máximo S/ 25.00 por regalo
- **Gestión de Regalos**: Agregar, editar, eliminar y marcar como recibidos
- **Panel de Administración**: Vista completa para superusuarios

### 🎨 Diseño
- **Colores Principales**: Dorado y Rosa con paleta complementaria
- **Totalmente Responsivo**: Optimizado para móvil, tablet y desktop
- **Animaciones Fluidas**: Transiciones suaves y efectos modernos
- **Glassmorphism**: Efectos de vidrio esmerilado
- **Gradientes Dinámicos**: Colores vibrantes y profesionales

### 🔒 Seguridad
- Autenticación de usuarios
- Protección CSRF
- Contraseñas encriptadas
- Validaciones de datos

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/andresu34t-bit/lista_navidad.git
cd lista_navidad
```

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones**
```bash
python manage.py migrate
```

5. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Aplicación: http://127.0.0.1:8000/
- Panel Admin: http://127.0.0.1:8000/admin/

## 📱 Uso

### Para Usuarios Nuevos

1. **Registrarse**
   - Ve a `/register/`
   - Completa el formulario con tu información
   - Automáticamente se crea tu lista personal

2. **Agregar Regalos**
   - Haz clic en "➕ Agregar Regalo"
   - Completa nombre, descripción y precio
   - Máximo 6 regalos por usuario

3. **Gestionar Lista**
   - Marca regalos como recibidos
   - Elimina regalos que ya no deseas
   - Visualiza estadísticas de tu lista

### Para Administradores

- Accede al panel admin para ver todas las listas
- Visualiza estadísticas globales
- Gestiona usuarios y regalos

## 🎨 Paleta de Colores

| Color | Hex | Uso |
|-------|-----|-----|
| Dorado | `#d4af37` | Principal |
| Dorado Claro | `#f4c430` | Acentos |
| Rosa | `#ff69b4` | Principal |
| Rosa Oscuro | `#ff1493` | Acentos |
| Verde | `#51cf66` | Éxito |
| Azul | `#2196F3` | Información |
| Rojo | `#ff6b6b` | Peligro |

## 📋 Reglas de Negocio

- ✅ Cada usuario tiene su propia lista personal
- ✅ Máximo 6 regalos por usuario
- ✅ Precio máximo de S/ 25.00 por regalo
- ✅ Solo puedes ver y gestionar tu propia lista
- ✅ Los administradores pueden ver todas las listas

## 🛠️ Tecnologías

- **Backend**: Django 5.2.7
- **Base de Datos**: SQLite (desarrollo)
- **Frontend**: HTML5, CSS3, JavaScript
- **Diseño**: CSS Gradients, Animations, Glassmorphism

## 📂 Estructura del Proyecto

```
lista_navidad/
├── lista_navidad/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── regalos/                # Aplicación principal
│   ├── models.py          # Modelos (Persona, Regalo)
│   ├── views.py           # Vistas
│   ├── forms.py           # Formularios
│   ├── urls.py            # Rutas
│   ├── admin.py           # Configuración admin
│   └── templates/         # Plantillas HTML
│       └── regalos/
│           ├── base.html
│           ├── login.html
│           ├── register.html
│           ├── mi_lista.html
│           ├── panel_admin.html
│           └── ...
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎯 Características Técnicas

### Modelos
- **Persona**: Usuario con lista de regalos
- **Regalo**: Item con nombre, descripción, precio y estado

### Validaciones
- Precio máximo por regalo
- Límite de regalos por persona
- Validación de formularios
- Protección contra duplicados

### Responsive Design
- Breakpoints: 480px, 768px, 968px
- Diseño mobile-first
- Imágenes y fuentes adaptativas

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Andrés**
- GitHub: [@andresu34t-bit](https://github.com/andresu34t-bit)

## 🎄 Agradecimientos

- Diseño inspirado en las festividades navideñas
- Paleta de colores: Dorado y Rosa
- Iconos: Emojis nativos

## 📞 Soporte

Si tienes alguna pregunta o problema:
- Abre un [Issue](https://github.com/andresu34t-bit/lista_navidad/issues)
- Contacta al autor

---

<div align="center">

**¡Feliz Navidad! 🎅🎄🎁**

Hecho con ❤️ y Django

</div>
