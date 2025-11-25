# 📦 Comandos para Subir a GitHub

## Paso 1: Inicializar Git (si no está inicializado)

```bash
git init
```

## Paso 2: Agregar todos los archivos

```bash
git add .
```

## Paso 3: Hacer el primer commit

```bash
git commit -m "🎄 Initial commit: Lista Navideña - Aplicación Django completa"
```

## Paso 4: Conectar con el repositorio remoto

```bash
git remote add origin https://github.com/andresu34t-bit/lista_navidad.git
```

## Paso 5: Verificar la conexión

```bash
git remote -v
```

## Paso 6: Subir al repositorio

```bash
# Si es la primera vez
git push -u origin main

# O si la rama principal es master
git push -u origin master

# Si tienes problemas, fuerza el push (solo la primera vez)
git push -u origin main --force
```

---

## Comandos Adicionales Útiles

### Ver el estado de los archivos
```bash
git status
```

### Ver el historial de commits
```bash
git log
git log --oneline
```

### Crear una nueva rama
```bash
git checkout -b nombre-rama
```

### Cambiar de rama
```bash
git checkout main
```

### Ver diferencias
```bash
git diff
```

### Deshacer cambios
```bash
# Deshacer cambios en un archivo
git checkout -- archivo.py

# Deshacer el último commit (mantiene cambios)
git reset --soft HEAD~1

# Deshacer el último commit (elimina cambios)
git reset --hard HEAD~1
```

---

## Flujo de Trabajo Recomendado

### Para nuevos cambios:

1. **Hacer cambios en el código**

2. **Ver qué cambió**
```bash
git status
git diff
```

3. **Agregar cambios**
```bash
# Agregar todos los archivos
git add .

# O agregar archivos específicos
git add archivo1.py archivo2.py
```

4. **Hacer commit**
```bash
git commit -m "Descripción clara de los cambios"
```

5. **Subir a GitHub**
```bash
git push origin main
```

---

## Mensajes de Commit Recomendados

### Formato
```
tipo: descripción breve

Descripción detallada (opcional)
```

### Tipos comunes
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Cambios de formato (no afectan código)
- `refactor:` Refactorización de código
- `test:` Agregar o modificar tests
- `chore:` Tareas de mantenimiento

### Ejemplos
```bash
git commit -m "feat: Agregar sistema de registro de usuarios"
git commit -m "fix: Corregir validación de precio máximo"
git commit -m "docs: Actualizar README con instrucciones de instalación"
git commit -m "style: Mejorar diseño del header con gradientes"
git commit -m "refactor: Optimizar consultas de base de datos"
```

---

## Solución de Problemas Comunes

### Error: "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/andresu34t-bit/lista_navidad.git
```

### Error: "Updates were rejected"
```bash
# Opción 1: Pull primero
git pull origin main --rebase

# Opción 2: Forzar push (cuidado, sobrescribe el remoto)
git push origin main --force
```

### Error: "Permission denied"
```bash
# Configurar credenciales
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# O usar token de acceso personal
# Ve a GitHub → Settings → Developer settings → Personal access tokens
```

### Olvidé agregar un archivo al .gitignore
```bash
# Remover del tracking
git rm --cached archivo.py

# Agregar a .gitignore
echo "archivo.py" >> .gitignore

# Commit
git commit -m "chore: Actualizar .gitignore"
```

---

## Configuración Inicial de Git

```bash
# Configurar nombre
git config --global user.name "Tu Nombre"

# Configurar email
git config --global user.email "tu@email.com"

# Ver configuración
git config --list

# Configurar editor por defecto
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "nano"         # Nano
```

---

## Ignorar Archivos Sensibles

Asegúrate de que `.gitignore` incluya:

```
# Base de datos
*.sqlite3
db.sqlite3

# Variables de entorno
.env
.env.local

# Archivos de Python
__pycache__/
*.pyc
*.pyo

# IDE
.vscode/
.idea/

# Logs
*.log
```

---

## Clonar el Repositorio (para otros usuarios)

```bash
# Clonar
git clone https://github.com/andresu34t-bit/lista_navidad.git

# Entrar al directorio
cd lista_navidad

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

---

## Branches (Ramas)

### Crear y trabajar con ramas

```bash
# Crear nueva rama
git checkout -b feature/nueva-funcionalidad

# Ver todas las ramas
git branch

# Cambiar de rama
git checkout main

# Fusionar rama
git checkout main
git merge feature/nueva-funcionalidad

# Eliminar rama
git branch -d feature/nueva-funcionalidad

# Subir rama a GitHub
git push origin feature/nueva-funcionalidad
```

---

## Tags (Versiones)

```bash
# Crear tag
git tag -a v1.0.0 -m "Primera versión estable"

# Ver tags
git tag

# Subir tags
git push origin --tags

# Subir tag específico
git push origin v1.0.0
```

---

## Comandos de Emergencia

### Deshacer TODO y volver al último commit
```bash
git reset --hard HEAD
```

### Volver a un commit específico
```bash
git reset --hard <commit-hash>
```

### Ver archivos en un commit específico
```bash
git show <commit-hash>
```

### Recuperar archivo eliminado
```bash
git checkout HEAD -- archivo.py
```

---

## Checklist Antes de Subir

- [ ] Código funciona localmente
- [ ] Tests pasan (si los hay)
- [ ] .gitignore configurado
- [ ] README actualizado
- [ ] Archivos sensibles no incluidos
- [ ] Commit message descriptivo
- [ ] Sin archivos innecesarios

---

## Recursos Adicionales

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

¡Listo para subir tu proyecto! 🚀
