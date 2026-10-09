"""
Sistema de Atención al Cliente con CrewAI
Basado en:
- 2-crewai_orchestration.py -> agentes, tareas y Crew
- 8-resource-allocation.py -> habilidades, capacidad y balance de carga

Requiere:
    pip install "crewai[litellm]" python-dotenv

Archivo .env:
    GROQ_API_KEY=gsk_tu_clave
    GROQ_MODEL=openai/gpt-oss-120b   # opcional
"""

import os
from dataclasses import dataclass
from typing import List

from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# WORKAROUND: CrewAI puede agregar `cache_breakpoint` a los mensajes.
# Groq no acepta ese campo, por lo que lo desactivamos antes de crear el LLM.
try:
    import crewai.llms.cache as crewai_cache
    crewai_cache.mark_cache_breakpoint = lambda msg: msg
except Exception:
    pass

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print("❌ Falta GROQ_API_KEY en el archivo .env")
    raise SystemExit(1)

llm = LLM(
    model=f"groq/{os.getenv('GROQ_MODEL', 'openai/gpt-oss-120b')}",
    temperature=0.2,
)


@dataclass
class Specialist:
    """Representa un agente especializado y su carga actual."""
    id: str
    name: str
    skill: str
    current_load: int = 0
    capacity: int = 3

    def available(self) -> bool:
        return self.current_load < self.capacity


# ---------------------------------------------------------
# 1. EQUIPO DE ATENCIÓN
# ---------------------------------------------------------
specialists = [
    Specialist("ventas", "Ana - Ventas", "ventas", capacity=3),
    Specialist("soporte", "Luis - Soporte Técnico", "soporte", capacity=3),
    Specialist("general", "María - Atención General", "general", capacity=4),
]

agents = {
    "ventas": Agent(
        role="Especialista de Ventas",
        goal="Resolver consultas sobre productos, precios, descuentos y cotizaciones.",
        backstory=(
            "Eres Ana, especialista en ventas. Conoces productos, precios, "
            "promociones y cotizaciones. Respondes de forma clara y profesional."
        ),
        llm=llm,
        verbose=False,
    ),
    "soporte": Agent(
        role="Especialista de Soporte Técnico",
        goal="Resolver problemas técnicos de clientes de manera ordenada y segura.",
        backstory=(
            "Eres Luis, especialista en soporte técnico. Atiendes problemas de "
            "login, conexión, aplicaciones y errores. Das pasos simples y concretos."
        ),
        llm=llm,
        verbose=False,
    ),
    "general": Agent(
        role="Especialista de Atención General",
        goal="Responder consultas generales y orientar al cliente hacia el área correcta.",
        backstory=(
            "Eres María, especialista en atención general. Tu objetivo es entregar "
            "una respuesta amable, clara y útil, derivando al área correspondiente "
            "cuando sea necesario."
        ),
        llm=llm,
        verbose=False,
    ),
}


# ---------------------------------------------------------
# 2. CLASIFICACIÓN DE LA CONSULTA
# ---------------------------------------------------------
def classify_query(query: str) -> str:
    """Clasificación sencilla por palabras clave para seleccionar especialista."""
    text = query.lower()

    sales_words = [
        "precio", "precios", "producto", "productos", "comprar", "compra",
        "cotización", "cotizacion", "descuento", "descuentos", "promoción",
        "promocion", "oferta", "venta", "vender"
    ]
    support_words = [
        "error", "login", "contraseña", "contrasena", "conexión", "conexion",
        "no funciona", "falló", "fallo", "problema", "instalar", "reinstalar",
        "aplicación", "aplicacion", "técnico", "tecnico", "soporte"
    ]

    if any(word in text for word in sales_words):
        return "ventas"
    if any(word in text for word in support_words):
        return "soporte"
    return "general"


# ---------------------------------------------------------
# 3. ASIGNACIÓN BALANCEADA
# ---------------------------------------------------------
def assign_specialist(area: str) -> Specialist | None:
    """Selecciona al especialista disponible con menor carga."""
    candidates = [s for s in specialists if s.skill == area and s.available()]
    if not candidates:
        return None
    return min(candidates, key=lambda s: s.current_load)


# ---------------------------------------------------------
# 4. PROCESAMIENTO CON CREWAI
# ---------------------------------------------------------
def process_customer_request(query: str) -> None:
    print("\n" + "=" * 70)
    print("📞 SISTEMA DE ATENCIÓN AL CLIENTE")
    print("=" * 70)
    print(f"👤 Cliente: {query}")

    area = classify_query(query)
    specialist = assign_specialist(area)

    print(f"🔎 Área detectada: {area.upper()}")

    if specialist is None:
        print("⚠️ El especialista está ocupado. No se puede asignar el ticket.")
        return

    specialist.current_load += 1
    print(f"👨‍💼 Asignado a: {specialist.name}")
    print(f"📊 Carga: {specialist.current_load}/{specialist.capacity}")

    agent = agents[area]

    task = Task(
        description=(
            f"Atiende la siguiente consulta de un cliente:\n\n"
            f"{query}\n\n"
            "Entrega una respuesta directa, amable y fácil de entender. "
            "No inventes datos como precios exactos, políticas o números de pedido. "
            "Si falta información, indica qué dato necesita entregar el cliente."
        ),
        expected_output=(
            "Una respuesta final para el cliente, de máximo 150 palabras, "
            "con pasos o información concreta cuando corresponda."
        ),
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    try:
        result = crew.kickoff()
        print("\n🤖 RESPUESTA DEL SISTEMA")
        print("-" * 70)
        print(result)
    except Exception as error:
        print(f"\n❌ Error al ejecutar CrewAI: {error}")
    finally:
        specialist.current_load = max(0, specialist.current_load - 1)


# ---------------------------------------------------------
# 5. MODO INTERACTIVO
# ---------------------------------------------------------
def main():
    print("\n" + "=" * 70)
    print("🤖 SISTEMA MULTI-AGENTE DE ATENCIÓN AL CLIENTE")
    print("=" * 70)
    print("Agentes disponibles:")
    for specialist in specialists:
        print(f"  - {specialist.name}: {specialist.skill}")

    print("\nEscribe una consulta del cliente.")
    print("Ejemplos:")
    print("  - ¿Cuánto cuesta el producto X?")
    print("  - No puedo iniciar sesión en mi cuenta")
    print("  - ¿Cuál es el horario de atención?")
    print("Escribe 'salir' para terminar.\n")

    while True:
        query = input("👤 Cliente > ").strip()

        if query.lower() == "salir":
            print("👋 Sistema finalizado.")
            break

        if not query:
            print("⚠️ Escribe una consulta.")
            continue

        process_customer_request(query)


if __name__ == "__main__":
    main()