Sistema de Atención al Cliente con CrewAI
1. Descripción del proyecto

Este proyecto implementa un sistema de atención al cliente utilizando Python y CrewAI. Su objetivo es clasificar las consultas recibidas, asignarlas a un área especializada y generar una respuesta mediante un agente de inteligencia artificial.

El sistema combina la organización de agentes de CrewAI con un mecanismo básico de asignación de especialistas según el tipo de consulta y su disponibilidad.

2. Objetivos
Clasificar las consultas de los clientes.
Asignar cada consulta al área correspondiente.
Utilizar agentes especializados para generar respuestas.
Incorporar un mecanismo sencillo de control de carga de trabajo.
Practicar la implementación de sistemas multiagente con Python.
3. Agentes especializados
Agente	Área	Función
Ana	Ventas	Consultas sobre productos, precios, promociones y cotizaciones.
Luis	Soporte técnico	Consultas sobre errores, acceso, conexión e instalación.
María	Atención general	Consultas generales y orientación al cliente.
4. Tecnologías utilizadas
Python
CrewAI
LiteLLM
Groq API
python-dotenv
Git y GitHub
5. Requisitos
Python instalado.
Una clave de API de Groq.
Conexión a Internet para utilizar el modelo de inteligencia artificial.
6. Instalación

Clonar el repositorio y acceder a su carpeta:

git clone URL_DE_TU_REPOSITORIO
cd sistema-atencion-cliente-crewai

Crear un entorno virtual:

python -m venv .venv

Activar el entorno virtual en Windows:

.\.venv\Scripts\Activate.ps1

Instalar las dependencias:

pip install -r requirements.txt
7. Configuración

Crear un archivo llamado .env en la carpeta principal del proyecto.

Agregar las siguientes variables:

GROQ_API_KEY=TU_CLAVE_DE_GROQ
GROQ_MODEL=openai/gpt-oss-120b

Reemplazar TU_CLAVE_DE_GROQ por una clave válida.

Importante: no subir el archivo .env a GitHub ni compartir la clave de API. El archivo .env.example sirve como plantilla sin credenciales reales.

8. Ejecución

Desde la carpeta del proyecto, ejecutar:

python sistema_atencion_cliente_crewai.py

El programa permite ingresar consultas por consola y finaliza cuando el usuario escribe salir.

9. Ejemplos de consultas
¿Cuánto cuesta el producto?
No puedo iniciar sesión en mi cuenta.
¿Cuál es el horario de atención?
¿Qué descuentos tienen disponibles?
10. Funcionamiento general
El cliente ingresa una consulta.
El sistema clasifica la consulta por palabras clave.
Se selecciona el especialista correspondiente.
CrewAI ejecuta la tarea mediante el agente especializado.
El sistema muestra la respuesta generada.
Se actualiza la disponibilidad del especialista.
11. Seguridad y limitaciones

La clave de API debe mantenerse fuera del repositorio. El archivo .gitignore excluye las credenciales y los archivos temporales.

La clasificación actual utiliza palabras clave, por lo que algunas consultas ambiguas pueden ser derivadas a un área que no corresponda. Las respuestas generadas también dependen del modelo de inteligencia artificial y de la información disponible.

12. Autoría

Proyecto académico desarrollado para practicar Python, inteligencia artificial y orquestación de agentes con CrewAI.