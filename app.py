import buscador_selenium_clase
def app():    
    Buscador = buscador_selenium_clase.Buscador("INDUCCION", "123456")
    Buscador.inicio_sesion_zeus()

if __name__ == '__main__':
    app()
    