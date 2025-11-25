# 🔧 Solucionar Error 403 - Permission Denied

## ❌ Error Actual
```
remote: Permission to andresu34t-bit/lista_navidad.git denied to Andres3r.
fatal: unable to access 'https://github.com/andresu34t-bit/lista_navidad.git/': 
The requested URL returned error: 403
```

**Problema**: Estás intentando subir con el usuario `Andres3r` pero el repositorio pertenece a `andresu34t-bit`.

---

## ✅ Solución 1: Token de Acceso Personal (RECOMENDADO)

### Paso 1: Crear Token en GitHub

1. Ve a GitHub.com e inicia sesión con `andresu34t-bit`
2. Haz clic en tu foto de perfil (arriba derecha) → **Settings**
3. En el menú izquierdo, baja hasta **Developer settings**
4. Haz clic en **Personal access tokens** → **Tokens (classic)**
5. Haz clic en **Generate new token** → **Generate new token (classic)**
6. Configura:
   - **Note**: "Lista Navidad - Push Access"
   - **Expiration**: 90 days (o lo que prefieras)
   - **Scopes**: Marca ✅ **repo** (esto incluye todos los permisos de repositorio)
7. Haz clic en **Generate token**
8. **¡IMPORTANTE!** Copia el token (empieza con `ghp_...`) - Solo lo verás una vez

### Paso 2: Actualizar Remote con Token

```bash
# Remover el remote actual
git remote remove origin

# Agregar nuevo remote con token
git remote add origin https://TU_TOKEN_AQUI@github.com/andresu34t-bit/lista_navidad.git

# Ejemplo (reemplaza TU_TOKEN con tu token real):
# git remote add origin https://ghp_xxxxxxxxxxxxxxxxxxxx@github.com/andresu34t-bit/lista_navidad.git
```

### Paso 3: Push

```bash
git push -u origin main
```

---

## ✅ Solución 2: Usar GitHub CLI (Alternativa)

### Instalar GitHub CLI

**Windows:**
```bash
winget install --id GitHub.cli
```

O descarga desde: https://cli.github.com/

### Autenticarse

```bash
gh auth login
```

Sigue las instrucciones:
1. Selecciona "GitHub.com"
2. Selecciona "HTTPS"
3. Selecciona "Login with a web browser"
4. Copia el código que te da
5. Presiona Enter
6. Se abrirá el navegador, pega el código
7. Autoriza GitHub CLI

### Push

```bash
git push -u origin main
```

---

## ✅ Solución 3: Cambiar Credenciales de Windows

### Opción A: Credential Manager

1. Presiona `Windows + R`
2. Escribe: `control /name Microsoft.CredentialManager`
3. Haz clic en **Windows Credentials**
4. Busca entradas de `git:https://github.com`
5. Elimínalas todas
6. Intenta push de nuevo - te pedirá nuevas credenciales

### Opción B: Comando Git

```bash
# Limpiar credenciales guardadas
git credential-manager-core erase https://github.com

# O
git config --global --unset credential.helper
git config --global credential.helper manager-core

# Intentar push - te pedirá credenciales
git push -u origin main
```

---

## ✅ Solución 4: SSH (Más Seguro a Largo Plazo)

### Paso 1: Generar Clave SSH

```bash
ssh-keygen -t ed25519 -C "tu_email@example.com"
```

Presiona Enter 3 veces (usa ubicación y contraseña por defecto)

### Paso 2: Copiar Clave Pública

```bash
# Windows
type %USERPROFILE%\.ssh\id_ed25519.pub

# O abre el archivo manualmente:
# C:\Users\johan\.ssh\id_ed25519.pub
```

Copia todo el contenido (empieza con `ssh-ed25519`)

### Paso 3: Agregar a GitHub

1. Ve a GitHub → Settings → SSH and GPG keys
2. Haz clic en **New SSH key**
3. Title: "Mi PC"
4. Key: Pega la clave pública
5. Haz clic en **Add SSH key**

### Paso 4: Cambiar Remote a SSH

```bash
# Remover remote actual
git remote remove origin

# Agregar remote SSH
git remote add origin git@github.com:andresu34t-bit/lista_navidad.git

# Push
git push -u origin main
```

---

## 🎯 Solución Rápida (Más Fácil)

### Opción 1: Usar Token en la URL

```bash
# Formato:
git remote set-url origin https://TU_TOKEN@github.com/andresu34t-bit/lista_navidad.git

# Ejemplo (reemplaza ghp_xxx con tu token):
git remote set-url origin https://ghp_xxxxxxxxxxxxxxxxxxxx@github.com/andresu34t-bit/lista_navidad.git

# Push
git push -u origin main
```

### Opción 2: Push con Token en el Comando

```bash
git push https://TU_TOKEN@github.com/andresu34t-bit/lista_navidad.git main
```

---

## 📝 Verificar Usuario Actual

```bash
# Ver configuración de Git
git config --global user.name
git config --global user.email

# Ver remote actual
git remote -v

# Ver credenciales guardadas (Windows)
git config --global credential.helper
```

---

## 🔄 Cambiar Usuario de Git

Si necesitas cambiar el usuario:

```bash
# Configurar nombre
git config --global user.name "andresu34t-bit"

# Configurar email
git config --global user.email "tu_email@example.com"

# Verificar
git config --global --list
```

---

## ⚠️ Importante

1. **Nunca compartas tu token** - Es como una contraseña
2. **No subas el token al repositorio** - Mantenlo privado
3. **Usa tokens con permisos mínimos** - Solo marca "repo"
4. **Renueva tokens periódicamente** - Por seguridad

---

## 🎯 Recomendación

**Para este caso específico, usa la Solución 1 (Token):**

1. Crea un token en GitHub
2. Ejecuta:
```bash
git remote set-url origin https://TU_TOKEN@github.com/andresu34t-bit/lista_navidad.git
git push -u origin main
```

3. ¡Listo!

---

## 📞 Si Sigues Teniendo Problemas

1. Verifica que estás logueado en GitHub con `andresu34t-bit`
2. Verifica que el repositorio existe
3. Verifica que tienes permisos de escritura
4. Intenta crear el repositorio de nuevo si es necesario

---

## 🆘 Última Opción: Crear Nuevo Repositorio

Si nada funciona:

1. Ve a GitHub
2. Crea un nuevo repositorio con otro nombre
3. Actualiza el remote:
```bash
git remote set-url origin https://github.com/andresu34t-bit/NUEVO_NOMBRE.git
git push -u origin main
```

---

¡Elige la solución que prefieras y estarás listo! 🚀
