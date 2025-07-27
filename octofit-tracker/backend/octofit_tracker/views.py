from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit Tracker API!",
        "url": "https://jubilant-capybara-49q55g4q42644-8000.app.github.dev"
    })
