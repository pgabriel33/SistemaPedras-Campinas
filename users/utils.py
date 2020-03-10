from .models import User
# from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
def obter_usuario_logado(request):
    try:
        usr = User.objects.get(nome_usuario_id=request.user.pk)
    except ObjectDoesNotExist:
        usr = ''

    return usr