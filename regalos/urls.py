from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.mi_lista, name='mi_lista'),
    path('mi-lista/', views.mi_lista, name='mi_lista'),
    path('agregar-regalo/', views.agregar_regalo_mi_lista, name='agregar_regalo_mi_lista'),
    path('panel-admin/', views.panel_admin, name='panel_admin'),
    path('panel-admin/personas/', views.lista_personas, name='lista_personas'),
    path('panel-admin/persona/<int:persona_id>/', views.detalle_persona, name='detalle_persona'),
    path('panel-admin/agregar-persona/', views.agregar_persona, name='agregar_persona'),
    path('panel-admin/persona/<int:persona_id>/agregar-regalo/', views.agregar_regalo, name='agregar_regalo'),
    path('regalo/<int:regalo_id>/eliminar/', views.eliminar_regalo, name='eliminar_regalo'),
    path('regalo/<int:regalo_id>/comprado/', views.marcar_comprado, name='marcar_comprado'),
]
