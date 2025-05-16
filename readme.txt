Primer Proyecto Web Scrapping Orientado a hacer un Fetch de Notas en el Aplicativo empresarial ZeusSalud

Fue cambiado por el aplicativo que hace fetch en la base de Datos debido a que este es mucho mas lento en todos los sentidos.

*SE DESCARTO USAR "BEATYFULLSOUP"(bs4) DEBIDO A QUE EL APLICATIVO MANEJA 1 URL QUE ACTUALIZA DINAMICAMENTE CON JS

*El uso de WebScrapping permite multiples posibilidade tanto dentro del aplicativo como fuera del mismo*

*Elegimos Selenium debido a esta modalidad de funcionamiento UniURI*

Selenium funciona selecionando distintos elemntos presentes en el HTM a través de multiples modalidades, como buscar por -> "ID, NAME, TAG, CSSelector, CLASS"
El aplicativo usa Clases Comunes y CSSelector comunes (Recicla mucho codigo), de la misma forma que tags y names genericos; sin seguir ninguna convencion especifica, lo cual complico el desarrollo

Solucion? Explorar constantemente el HTML e identificar la estructura de etiquetas 

El aplicativo presentaba multiples "Frames, IFrames, DataFrames" los cuels entorpecieron su proceso de desarrollo
debido a que Selenium tiene el selector ubicado de foram predefinida en el "body", pero si el elemento está dentro de un cuadro que a su vez está dentor del body, va a presentar error de "elementoInexistente"

-   El codigo presenta POO orientado a crear un buscador y dirigirlo con funciones embebidas, primero se realizaron funciones que daban direccion simulando el flujo real de la APP,
    pero despues se hizo una simple redireccion posterior al login y seleccion de modulo, esto debido a que el sistema almacena la sesion en el navegador

-   Ingresa CC del paciente( Se pasa por parametro, o se almacena en variable, lo cual permite su crecimiento) y busca en la zona de fichero, selecciona el unico paciente que debe salir y entra a su HC

-   Selecciona Formato (Tuvo complejidad debido a que son 2 cuadros, uno bugeado que se mantiene fuera de vista, y otro donde está el contenido interactuable)
-   Selecciona SubFormato, espera a que la tabla se cargue y recupera todo su contenido


Esta vez se subira un proyecto modular con ofuscacion pyarmor, lo cual implica unos comandos ligeramente diferentes como ->

/*
 DEPRECADO O NO FUNCIONAL
    pyarmor init --src=. --entry "main.py"->Nombre del ejecutable del proyecto "mi_proyecto_protegido -> Nombre de la carpeta donde se duplicara la estructura de carpetas con cnfiguracion pyarmor"
    *TODO ESTO DENTRO DEL DIRACTORIO DEL PROYECTO*


    En la ruta del proyecto ejecutar pyarmor cfg init -> Me crea un archivo de configuracion del pyarmor, (pyarmor_config.cfg)
    en el cual tengo que marcar los parametros que antes se marcaban en el BASH
    Si no se crea hay que crearlo manual

    Ejcecutar el comando pyarmor gen y pasarle algunos argumentos como 

    ->  pyarmor gen -r -O dist main.py


    | Opción    | Significado                                       |
    | --------- | ------------------------------------------------- |
    | `gen`     | Comando para generar código protegido/ofuscado    |
    | `main.py` | Punto de entrada del programa                     |
    | `-r`      | Busca y protege recursivamente módulos importados |
    | `-O dist` | Carpeta donde se guardará el código ofuscado      |

*\
    pyarmor gen -r {Nombre de los archivos-Incluye extension} separados por espacio 