from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Buscador():
    def __init__(self, usuario, contraseña):
        self.usuario=usuario
        self.contraseña = contraseña
        self.options = Options()
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36")
        #Inicializar servicio y navegador
        self.service = Service(ChromeDriverManager().install())
        # self.options.add_argument('--headless')
        # self.options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        

   
    def inicio_sesion_zeus(self):
        '''Establecido para el formulario Inicio sesion Zeus. No recibe parametros,
        solo utiliza el usuario y contraseña del constructor'''
         
        try:
        
            url_inicio_sesion = 'http://192.168.100.50:8001/ZeusSalud/ips/iniciando.php'
            self.driver.get(url_inicio_sesion)

            campo_usuario = self.driver.find_element(By.ID, "usuario")
            campo_usuario.send_keys(self.usuario)
            
            campo_usuario.send_keys(Keys.RETURN)
            
            campo_contraseña= self.driver.find_element(By.ID,"password")
            campo_contraseña.send_keys(self.contraseña)
            
            campo_conexion = self.driver.find_element(By.ID, "conexion")
            campo_conexion.send_keys(Keys.RETURN)
            
            campo_conexion.send_keys(Keys.ARROW_DOWN)

            campo_conexion.send_keys(Keys.RETURN)
            
            boton_inicio_sesion= self.driver.find_element(By.ID,"btnEnviar")
            boton_inicio_sesion.send_keys(Keys.ENTER)            
            
            # self.buscar_modulo_deseado()
            self.navegacion_hasta_censo()

        except Exception as error: 
                print(error)
#----------------------------------------------------------------------

    def navegacion_hasta_censo(self):
        time.sleep(1)
        #El contenido del selector de modulos está dentro de un Iframe, entonces ->
        #Esperamos a que el IFRAME esté disponible en el selector
        tiempo_espera_iframe= WebDriverWait(self.driver,10)
        tiempo_espera_iframe.until(EC.presence_of_element_located((By.ID,"topFrame")))
        
        #Seleccionamos el iframe despeus que esté esté disponible
        iframe = self.driver.find_element(By.ID,"topFrame")
        self.driver.switch_to.frame(iframe)

        #Esperamos disponibilidad de los botones
        tiempo_espera_botones = WebDriverWait(self.driver,10)
        tiempo_espera_botones.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "/Vistas/Configuracion/censo.php?padre=4&origen=1")]')))  
        
        #Linea que clickea el boton de CENSO
        self.driver.find_element(By.XPATH, '//div[contains(@onclick, "/Vistas/Configuracion/censo.php?padre=4&origen=1")]').click()

        self.buscar_paciente_fichero_pacientes("0000000")
        # self.buscar_paciente_fichero_pacientes("15316533")
      
#---------------------------------------------------------
    def buscar_paciente_fichero_pacientes(self,cedula_paciente):
        # Ir directamente al destino
        time.sleep(3)
        self.driver.get('http://192.168.100.50:8001/ZeusSalud/ips/App/Vistas/Facturacion/FicheroPaciente.php')

        espera_por_check= WebDriverWait(self.driver,40)
        #Clickea el boton que nos lleva a una HC vacia
        espera_por_check.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(., "Historia clínica")]'))).click()

        campo_cedula_paciente = self.driver.find_element(By.ID,'ident')
        campo_cedula_paciente.send_keys(cedula_paciente)
        campo_cedula_paciente.send_keys(Keys.ENTER)
        time.sleep(2)

        self.buscar_paciente_hc()

#----------------------------------------------------------------
    def buscar_paciente_hc(self):
        #Esperamos por el cuadro contenedor de los elementos
        esperar_frameset = WebDriverWait(self.driver,10)
        espera_frameset = esperar_frameset.until(EC.presence_of_element_located((By.ID,'leftFrame')))
        frameset = self.driver.find_element(By.ID,'leftFrame')
        self.driver.switch_to.frame(frameset)

        #Empieza el proceso de espera por el elemento
        espera_por_boton_formato= WebDriverWait(self.driver,10)
        espera_al_boton_formato= espera_por_boton_formato.until(EC.element_to_be_clickable((By.NAME,'formatos_li'))).click()
        #CLIKEA EXITOSAMENTE

        boton_hospitalizadosEnferm = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='HOSPITALIZADOS ENFERMERIA']"))).click()
        #ACCEDE CORRECTAMENTE

        # Espera hasta que la tabla esté presente en la página
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[@id='TableHistoricoFormatos']/tbody/tr")))

        tabla_encontrada= self.driver.find_element(By.ID,'TableHistoricoFormatos')

        valores = []
        time.sleep(4)
        filas = tabla_encontrada.find_elements(By.XPATH, "//table[@id='TableHistoricoFormatos']/tbody/tr")
        
        time.sleep(2)
        encabezados = tabla_encontrada.find_elements(By.TAG_NAME, "th")
        encabezados_texto = [encabezado.text.strip() for encabezado in encabezados]
        print("Encabezados:", encabezados_texto)

        for fila in filas:
            celdas = fila.find_elements(By.TAG_NAME,'td') 

            if celdas:
                fila_valores= [celda.text.strip() for celda in celdas]
                valores.append(fila_valores)
        print(valores)


        time.sleep(30)

#-------------------------------------------------------------------------------------

    def obtener_datos_tabla(self,refTabla):
        
        pass

        # self.driver.quit()

