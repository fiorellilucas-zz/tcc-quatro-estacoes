from django.urls import path

from . import views

app_name = "quatroestacoes"
urlpatterns = [

    # USUÁRIO COMUM E ADMIN
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    
    path("moradores/", views.MoradoresListaView.as_view(), name="moradores_lista"),
    path("moradores/<int:id_morador>", views.MoradoresInfoView.as_view(), name="moradores_info"),
    
    path("calendario", views.CalendarioView.as_view(), name="calendario"),
    
    path("avisos/", views.AvisosListaView.as_view(), name="avisos_lista"),
    path("avisos/<int:pk>", views.AvisosInfoView.as_view(), name="avisos_info"),
    path("avisos/<int:pk>/alterar", views.AvisosUpdView.as_view(), name="avisos_upd"),
    path("avisos/<int:pk>/deletar", views.AvisosDelView.as_view(), name="avisos_del"),
    path("avisos/adicionar", views.AvisosAddView.as_view(), name="avisos_add"),
    
    path("reclamacoes/", views.ReclamacoesListaView.as_view(), name="reclamacoes_lista"),
    path("reclamacoes/<int:pk>", views.ReclamacoesInfoView.as_view(), name="reclamacoes_info"),
    path("reclamacoes/<int:pk>/alterar", views.ReclamacoesUpdView.as_view(), name="reclamacoes_upd"),
    path("reclamacoes/<int:pk>/deletar", views.ReclamacoesDelView.as_view(), name="reclamacoes_del"),    
    path("reclamacoes/adicionar", views.ReclamacoesAddView.as_view(), name="reclamacoes_add"),
    
    path("reunioes/", views.ReunioesListaView.as_view(), name="reunioes_lista"),
    path("reunioes/<int:pk>", views.ReunioesInfoView.as_view(), name="reunioes_info"),
    path("reunioes/<int:pk>/alterar", views.ReunioesUpdView.as_view(), name="reunioes_upd"),
    path("reunioes/<int:pk>/deletar", views.ReunioesDelView.as_view(), name="reunioes_del"),
    path("reunioes/adicionar", views.ReunioesAddView.as_view(), name="reunioes_add"),
    
    path("reservas/", views.ReservasListaView.as_view(), name="reservas_lista"),
    path("reservas/adicionar/", views.ReservasAddView.as_view(), name="reservas_add"),
    
    # EXCLUSIVAMENTE ADMIN
    path("moradores/adicionar/", views.MoradoresAddView.as_view(), name="moradores_add"),
    path("moradores/<int:pk>/alterar", views.MoradoresUpdView.as_view(), name="moradores_upd"),
    path("moradores/<int:pk>/deletar", views.MoradoresDelView.as_view(), name="moradores_del"),
]
