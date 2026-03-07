import flet as ft

def main(page: ft.Page):
    page.title = "Examen Final - Registro de Participantes"
    page.padding = 20
    page.scroll = "adaptive"

    titulo = ft.Text(
        "Registro de Participantes",
        size=30,
        weight=ft.FontWeight.BOLD,
    )
    
    nombre = ft.TextField(
        label="Nombre completo",
        width=400,
    )
    
    correo = ft.TextField(
        label="Correo electrónico",
        width=400,
    )
    
    taller_de_interes = ft.Dropdown(
        label="Taller de interés",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ],
        value="Python para Principiantes",
        width=400,
    )
    
    modalidad_de_pago = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Modalidad de pago:"),
            ft.Row([
                ft.Radio(value="Pago completo", label="Pago completo"),
                ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
        ])]),
        value="Pago completo",
    )
    
    requerimientos = ft.Checkbox(
        label="Requiere computadora portátil",
        value=False,
    )
    
    nivel_label = ft.Text("Nivel de experiencia:")
    nivel_experiencia = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        value=1,
        label="{value}",
        width=400,
    )
    
    txt_nivel_de_experiencia = ft.Text("Nivel: 1")

    def cambiar_experiencia(e):
        txt_nivel_de_experiencia.value = f"Nivel: {int(nivel_experiencia.value)}"
        page.update()

    nivel_experiencia.on_change = cambiar_experiencia

    resumen = ft.Text(
        value="",
        size=16,
        color=ft.Colors.BLUE_900,
    )

    linea = ft.Divider(height=20)
    
    def mostrar_resumen(e):
        if not nombre.value or nombre.value.strip() == "":
            resumen.value = "ERROR: El nombre no puede estar vacío"
            resumen.color = ft.Colors.RED
        elif not correo.value or correo.value.strip() == "":
            resumen.value = "ERROR: El correo no puede estar vacío"
            resumen.color = ft.Colors.RED
        else:
            resumen.value = f"""--- FICHA DEL PARTICIPANTE ---

Nombre: {nombre.value}
Email: {correo.value}
Taller: {taller_de_interes.value}
Pago: {modalidad_de_pago.value}
Requiere Portátil: {'Sí' if requerimientos.value else 'No'}
Nivel de Experiencia: {int(nivel_experiencia.value)}

--- Gracias por su registro ---"""
            resumen.color = ft.Colors.BLUE_900

        page.update()
    
    boton_resumen = ft.ElevatedButton(
        "Mostrar Ficha del Participante",
        on_click=mostrar_resumen,
        width=250,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_400,
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
            modalidad_de_pago,
            ft.Container(height=10),
            requerimientos,
            ft.Container(height=10),
            nivel_label,
            nivel_experiencia,
            txt_nivel_de_experiencia,
            ft.Container(height=20),
            ft.Row([boton_resumen], alignment=ft.MainAxisAlignment.CENTER),
            linea,
            resumen,
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.run(main)