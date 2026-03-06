import flet as ft

def main(page: ft.Page):
    page.title = "Examen final- Registro de participantes"
    page.padding = 20
    page.scroll = "adaptive"

    
    titulo = ft.Text(
        "REGISTRO DE EVENTOS",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        italic=True,
    )
    
    nombre = ft.TextField(
        label="Nombre completo",
        width=400,
    )
    
    correo = ft.TextField(
        label="Correo electronico",
        width=400,
    )
    
    taller_de_interes = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ],
        value="Conferencia",
        width=400,
    )
    
    modalidad_de_pago = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
        ]),
        value="Pago completo",
        )
    
    requerimientos = ft.Checkbox(
        label="¿Requiere computadora portátil?",
        value=False,
    )
    
    nivel_experiencia = ft.Slider(
        min=1,
        max=5,
        divisions=5,
        value=1,
        label="{value}",
        width=400,
    )
    
    txt_nivel_de_experiencia = ft.Text("Nivel seleccionado: 1")

    def cambiar_experiencia(e):
        txt_nivel_de_experiencia.value = f"Duración seleccionada: {int(nivel_experiencia.value)}"
        page.update()

    nivel_experiencia.on_change = cambiar_experiencia

    resumen = ft.Text(
        value="",
        size=16,
    )
    
    resumen = ft.Text(
        value="",
        size=16,
    )

    linea = ft.Divider(height=20)
    
    def mostrar_resumen(e):
        if not nombre.value or nombre.value.strip() == "":
            resumen.value = "ERROR: El nombre no puede estar vacío"
            resumen.color = ft.Colors.RED
        else:
            resumen.value = f"""
FICHA DEL PARTICIPANTE
Nombre: {nombre.value}
Correo: {correo.value}
Taller: {taller_de_interes.value}
Modalidad de pago: {modalidad_de_pago.value}
Requerimientos: {'Sí' if requerimientos.value else 'No'}
Nivel de experiencia: {int(nivel_experiencia.value)} horas
---GRACIAS POR SU REGISTRO---
"""

            resumen.color = ft.Colors.BLACK

        page.update()
    
    boton_resumen = ft.ElevatedButton(
        "Mostrar Ficha del Participante",
        on_click=mostrar_resumen,
        width=200,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_600,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    
    page.add(
    ft.Column([
        titulo,
        ft.Container(height=10),
        nombre,
        ft.Container(height=10),
        correo,
        ft.Container(height=10),
        taller_de_interes,
        ft.Container(height=10),
        ft.Text("Modalidad de pago:"),
        modalidad_de_pago,
        ft.Container(height=10),
        requerimientos,
        ft.Container(height=10),
        ft.Container(height=10),
        ft.Text("Nivel de experiencia:"),
        nivel_experiencia,
        txt_nivel_de_experiencia,
        ft.Container(height=20),
        ft.Row([boton_resumen]),
        linea,
        resumen,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    
    

ft.run(main)