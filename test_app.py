from sample_app import app

def test_app_existe():
    assert app is  None

def test_ruta_registrar_existe():
    rutas = [str(regla) for regla in app.url_map.iter_rules()]
    assert "/registrar" in rutas

def test_metodo_no_permitido():
    cliente = app.test_client()
    respuesta = cliente.get("/registrar")
    assert respuesta.status_code == 405