from noticias.models import Noticias

def global_news(request):
    ultimas_noticias = Noticias.objects.order_by('-fecha')[:3]
    return {'ultimas_noticias': ultimas_noticias}
