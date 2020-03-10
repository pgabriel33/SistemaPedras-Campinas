from .models import User
# from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
def obter_usuario_logado(request):
    try:
        usr = User.objects.get(id=request.user.id)
    except ObjectDoesNotExist:
        usr = ''

    return usr