from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from .models import Persona, Regalo
from .forms import PersonaForm, RegaloForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('mi_lista')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        nombre_completo = request.POST.get('nombre_completo')
        
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe')
        elif len(password) < 6:
            messages.error(request, 'La contraseña debe tener al menos 6 caracteres')
        elif not nombre_completo:
            messages.error(request, 'El nombre completo es requerido')
        else:
            # Crear usuario
            user = User.objects.create_user(username=username, email=email, password=password)
            # Crear persona asociada
            Persona.objects.create(usuario=user, nombre=nombre_completo, email=email)
            auth_login(request, user)
            messages.success(request, f'¡Bienvenido {nombre_completo}! Ahora puedes agregar tus 6 regalos deseados.')
            return redirect('mi_lista')
    
    return render(request, 'regalos/register.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('mi_lista')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'¡Bienvenido {user.username}!')
            if user.is_superuser:
                return redirect('panel_admin')
            return redirect('mi_lista')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'regalos/login.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request, '¡Hasta pronto!')
    return redirect('login')

@login_required(login_url='login')
def mi_lista(request):
    # Obtener o crear la persona del usuario actual
    persona, created = Persona.objects.get_or_create(
        usuario=request.user,
        defaults={'nombre': request.user.username, 'email': request.user.email}
    )
    regalos = persona.regalos.all()
    
    # Verificar si la lista está completa
    if not persona.tiene_lista_completa():
        faltantes = persona.regalos_faltantes()
        if faltantes == 6:
            messages.warning(request, f'⚠️ Debes agregar tus 6 regalos para completar tu lista navideña.')
        else:
            messages.warning(request, f'⚠️ Te faltan {faltantes} regalo(s) para completar tu lista. ¡Agrega todos tus regalos!')
    
    return render(request, 'regalos/mi_lista.html', {
        'persona': persona,
        'regalos': regalos
    })

@login_required(login_url='login')
def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'regalos/lista_personas.html', {'personas': personas})

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser, login_url='mi_lista')
def panel_admin(request):
    personas = Persona.objects.annotate(
        total_regalos=Count('regalos'),
        total_gastado=Sum('regalos__precio')
    ).order_by('-total_gastado')
    
    regalos = Regalo.objects.select_related('persona').order_by('-fecha_creacion')
    
    # Calcular listas completas e incompletas
    todas_personas = Persona.objects.all()
    listas_completas = sum(1 for p in todas_personas if p.tiene_lista_completa())
    listas_incompletas = todas_personas.count() - listas_completas
    
    stats = {
        'total_personas': Persona.objects.count(),
        'total_regalos': Regalo.objects.count(),
        'total_gastado': Regalo.objects.aggregate(Sum('precio'))['precio__sum'] or 0,
        'regalos_comprados': Regalo.objects.filter(comprado=True).count(),
        'regalos_pendientes': Regalo.objects.filter(comprado=False).count(),
        'listas_completas': listas_completas,
        'listas_incompletas': listas_incompletas,
    }
    
    return render(request, 'regalos/panel_admin.html', {
        'personas': personas,
        'regalos': regalos,
        'stats': stats
    })

@login_required(login_url='login')
def detalle_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    regalos = persona.regalos.all()
    return render(request, 'regalos/detalle_persona.html', {
        'persona': persona,
        'regalos': regalos
    })

@login_required(login_url='login')
def agregar_regalo_mi_lista(request):
    persona = request.user.persona
    
    if not persona.puede_agregar_regalo():
        messages.error(request, 'Ya tienes el máximo de 6 regalos en tu lista.')
        return redirect('mi_lista')
    
    if request.method == 'POST':
        form = RegaloForm(request.POST)
        if form.is_valid():
            regalo = form.save(commit=False)
            regalo.persona = persona
            try:
                regalo.save()
                regalos_actuales = persona.regalos.count()
                if regalos_actuales == 6:
                    messages.success(request, '🎉 ¡Felicidades! Has completado tu lista con 6 regalos.')
                else:
                    faltantes = 6 - regalos_actuales
                    messages.success(request, f'✅ Regalo agregado. Te faltan {faltantes} regalo(s) para completar tu lista.')
                return redirect('mi_lista')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = RegaloForm()
    
    return render(request, 'regalos/agregar_regalo_mi_lista.html', {
        'form': form,
        'persona': persona
    })

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser, login_url='mi_lista')
def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Persona agregada exitosamente!')
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'regalos/agregar_persona.html', {'form': form})

@login_required(login_url='login')
def agregar_regalo(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    
    if not persona.puede_agregar_regalo():
        messages.error(request, 'Esta persona ya tiene el máximo de 6 regalos.')
        return redirect('detalle_persona', persona_id=persona_id)
    
    if request.method == 'POST':
        form = RegaloForm(request.POST)
        if form.is_valid():
            regalo = form.save(commit=False)
            regalo.persona = persona
            try:
                regalo.save()
                messages.success(request, '¡Regalo agregado exitosamente!')
                return redirect('detalle_persona', persona_id=persona_id)
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = RegaloForm()
    
    return render(request, 'regalos/agregar_regalo.html', {
        'form': form,
        'persona': persona
    })

@login_required(login_url='login')
def eliminar_regalo(request, regalo_id):
    regalo = get_object_or_404(Regalo, pk=regalo_id)
    
    # Verificar que el regalo pertenece al usuario actual o es admin
    if regalo.persona.usuario != request.user and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para eliminar este regalo.')
        return redirect('mi_lista')
    
    persona_regalo = regalo.persona
    regalo.delete()
    
    regalos_actuales = persona_regalo.regalos.count()
    if regalos_actuales < 6:
        faltantes = 6 - regalos_actuales
        messages.warning(request, f'Regalo eliminado. ⚠️ Ahora te faltan {faltantes} regalo(s) para completar tu lista obligatoria.')
    else:
        messages.success(request, 'Regalo eliminado exitosamente.')
    
    if request.user.is_superuser and 'from_admin' in request.GET:
        return redirect('detalle_persona', persona_id=persona_regalo.id)
    return redirect('mi_lista')

@login_required(login_url='login')
def marcar_comprado(request, regalo_id):
    regalo = get_object_or_404(Regalo, pk=regalo_id)
    
    # Verificar que el regalo pertenece al usuario actual o es admin
    if regalo.persona.usuario != request.user and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para modificar este regalo.')
        return redirect('mi_lista')
    
    regalo.comprado = not regalo.comprado
    regalo.save()
    
    if request.user.is_superuser and 'from_admin' in request.GET:
        return redirect('detalle_persona', persona_id=regalo.persona.id)
    return redirect('mi_lista')
