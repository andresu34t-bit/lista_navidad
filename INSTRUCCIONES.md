# 📋 Instrucciones de Uso - Lista Navideña

## 🚀 Inicio Rápido

### 1. Iniciar el Servidor
```bash
python manage.py runserver
```

### 2. Acceder a la Aplicación
Abre tu navegador y ve a: **http://127.0.0.1:8000/**

## 👤 Crear tu Primera Cuenta

### Opción 1: Registrarse como Usuario Normal
1. Ve a http://127.0.0.1:8000/register/
2. Completa el formulario:
   - Nombre de usuario
   - Email
   - Contraseña (mínimo 6 caracteres)
   - Confirmar contraseña
3. Haz clic en "🎄 Crear Cuenta"
4. Serás redirigido automáticamente a tu lista

### Opción 2: Usar la Cuenta de Administrador
- Usuario: `admin`
- Contraseña: `admin123`
- Acceso completo al panel de administración

## 📱 Funcionalidades

### Para Todos los Usuarios

#### Gestionar Personas
1. **Agregar Persona**:
   - Clic en "➕ Agregar Nueva Persona"
   - Ingresa nombre y email (opcional)
   - Guarda

2. **Ver Detalles**:
   - Clic en "Ver Detalles" de cualquier persona
   - Verás sus regalos y estadísticas

#### Gestionar Regalos
1. **Agregar Regalo**:
   - Entra al detalle de una persona
   - Clic en "➕ Agregar Regalo"
   - Completa:
     - Nombre del regalo
     - Descripción (opcional)
     - Precio (máx. S/ 25.00)
   - Guarda

2. **Marcar como Comprado**:
   - Clic en "✓ Comprado" en cualquier regalo
   - El regalo aparecerá tachado
   - Clic en "↩️ Desmarcar" para revertir

3. **Eliminar Regalo**:
   - Clic en "🗑️ Eliminar"
   - Confirma la acción

### Para Superusuarios (Admin)

#### Panel de Administración
1. Clic en "📊 Panel Admin" en el header
2. Verás:
   - **Estadísticas Globales**:
     - Total de personas
     - Total de regalos
     - Total gastado
     - Regalos comprados/pendientes
   
   - **Resumen por Persona**:
     - Lista completa de todas las personas
     - Cantidad de regalos por persona
     - Total gastado por persona
     - Barra de progreso (máx. 5 regalos)
   
   - **Todos los Regalos**:
     - Lista completa de todos los regalos
     - Estado (comprado/pendiente)
     - Persona asignada
     - Precio y fecha

## 🎨 Diseño Responsivo

La aplicación se adapta automáticamente a:
- 📱 **Móviles** (< 480px): Diseño vertical optimizado
- 📱 **Tablets** (480px - 768px): Diseño adaptado
- 💻 **Desktop** (> 768px): Diseño completo

### Características Responsivas:
- Menús y botones se reorganizan en pantallas pequeñas
- Tablas con scroll horizontal en móviles
- Formularios optimizados para touch
- Fuentes ajustadas para mejor legibilidad
- Botones de tamaño adecuado para dedos

## 🎯 Reglas de Negocio

### Límites
- ✅ Máximo **S/ 25.00** por regalo
- ✅ Máximo **5 regalos** por persona
- ✅ Validación automática en formularios

### Validaciones
- El sistema no permite:
  - Agregar regalos con precio > S/ 25.00
  - Agregar más de 5 regalos a una persona
  - Crear usuarios con nombres duplicados
  - Contraseñas menores a 6 caracteres

## 🔐 Seguridad

- Todas las páginas requieren autenticación
- Las contraseñas se almacenan encriptadas
- El panel admin solo es accesible para superusuarios
- Protección CSRF en todos los formularios

## 💡 Consejos

1. **Organización**: Crea una persona por cada familiar o amigo
2. **Presupuesto**: El sistema te muestra el total gastado por persona
3. **Seguimiento**: Marca los regalos como comprados para no olvidar
4. **Móvil**: Usa la app desde tu celular mientras compras
5. **Admin**: Si eres admin, revisa el panel para ver el presupuesto total

## 🎄 Colores y Tema

- **Dorado**: Representa la elegancia y festividad navideña
- **Rosa**: Añade calidez y modernidad
- **Gradientes**: Crean profundidad y profesionalismo
- **Animaciones**: Mejoran la experiencia sin ser intrusivas

## 🆘 Solución de Problemas

### No puedo iniciar sesión
- Verifica usuario y contraseña
- Usa `admin` / `admin123` para probar
- Crea una nueva cuenta si olvidaste tu contraseña

### No veo el botón "Panel Admin"
- Solo los superusuarios ven este botón
- Inicia sesión con la cuenta `admin`

### El servidor no inicia
```bash
# Verifica que Django esté instalado
pip install django

# Aplica las migraciones
python manage.py migrate

# Inicia el servidor
python manage.py runserver
```

### Error al agregar regalo
- Verifica que el precio sea ≤ S/ 25.00
- Verifica que la persona tenga < 5 regalos
- Completa todos los campos requeridos

## 📞 Soporte

Para más información, consulta el archivo `README.md` o revisa el código en:
- `regalos/models.py` - Modelos de datos
- `regalos/views.py` - Lógica de la aplicación
- `regalos/templates/` - Plantillas HTML

¡Feliz Navidad! 🎅🎄🎁
