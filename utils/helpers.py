def handle_api_error(response):
    """
    Gère les erreurs de l'API en fonction du code de statut HTTP.
    """
    if response.status_code not in [200, 201]:
        raise Exception(f"API Error: {response.status_code} - {response.text}")