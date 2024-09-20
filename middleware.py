from django.http import HttpResponsePermanentRedirect

class RedirectToCustomDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se o domínio não é o personalizado
        host = request.get_host()
        if host.startswith("list-to-do-") and host.endswith(".onrender.com"):
            # Redireciona para o domínio final
            return HttpResponsePermanentRedirect(f"https://listadetarefasltd.com{request.path}")
        
        return self.get_response(request)
