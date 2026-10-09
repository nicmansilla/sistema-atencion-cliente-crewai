Sistema de Atención al Cliente con CrewAI

Sistema desarrollado en Python que utiliza CrewAI para organizar agentes de inteligencia artificial especializados en la atención al cliente. El proyecto clasifica consultas y asigna una respuesta según el área correspondiente.

## Objetivo

Desarrollar un sistema de atención al cliente que permita organizar las consultas, utilizar agentes especializados y generar respuestas mediante un modelo de lenguaje.

## Características

* Clasificación de consultas por área.
* Agentes especializados en ventas, soporte técnico y atención general.
* Asignación de consultas según el tipo de solicitud.
* Uso de CrewAI para coordinar las tareas de los agentes.
* Ejecución interactiva desde la terminal.

## Agentes del sistema

| Agente | Área             | Función                                                        |
| ------ | ---------------- | -------------------------------------------------------------- |
| Ana    | Ventas           | Consultas sobre productos, precios, descuentos y cotizaciones. |
| Luis   | Soporte técnico  | Consultas sobre acceso, conexión, instalación y errores.       |
| María  | Atención general | Consultas generales e información para clientes.               |

## Tecnologías utilizadas

* **Python 3.13:** lenguaje de programación.
* **CrewAI:** creación y coordinación de agentes.
* **Groq API:** acceso al modelo de lenguaje.
* **LiteLLM:** integración con el proveedor del modelo.
* **python-dotenv:** lectura de variables de entorno.
* **uv:** gestión del entorno y las dependencias.
* **Git y GitHub:** control de versiones y publicación del código.

## Requisitos

* Python 3.13.
* uv instalado.
* Una clave de API válida de Groq.
* Conexión a Internet.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DE_TU_REPOSITORIO
cd sistema-atencion-cliente-crewai
```

Reemplaza `URL_DE_TU_REPOSITORIO` por la dirección real del repositorio.

### 2. Configurar las variables de entorno

Crea un archivo `.env` en la carpeta principal del proyecto con este contenido:

```dotenv
GROQ_API_KEY=TU_CLAVE_DE_GROQ
GROQ_MODEL=openai/gpt-oss-120b
```

Reemplaza `TU_CLAVE_DE_GROQ` por tu clave personal. No compartas ni publiques este archivo.

### 3. Instalar las dependencias

```bash
uv sync
```

Este comando instala las dependencias definidas en `pyproject.toml` y utiliza `uv.lock` cuando está disponible.

### 4. Ejecutar el sistema

```bash
uv run sistema_atencion_cliente_crewai.py
```

## Ejemplos de consultas

```text
¿Cuánto cuesta el producto?
No puedo iniciar sesión.
¿Qué descuentos tienen disponibles?
¿Cuál es el horario de atención?
```

Para finalizar la ejecución, escribe `salir` si el programa está esperando una consulta.

## Funcionamiento general

1. El cliente ingresa una consulta.
2. El sistema clasifica la consulta mediante palabras clave.
3. Se identifica el área correspondiente.
4. CrewAI ejecuta la tarea con el agente especializado.
5. El modelo genera una respuesta que se muestra al cliente.

## Seguridad

* El archivo `.env` no debe publicarse.
* Las carpetas de entornos virtuales deben excluirse del repositorio.
* No se deben incluir claves de API en el código fuente ni en el historial de Git.

## Limitaciones

La clasificación depende de las palabras clave definidas en el programa. Las respuestas dependen del modelo de lenguaje y pueden requerir validación. El sistema es una implementación académica y no sustituye por sí solo una plataforma empresarial completa de atención al cliente.

## Autoría

Proyecto académico de práctica en Python, inteligencia artificial y sistemas multiagente con CrewAI.
