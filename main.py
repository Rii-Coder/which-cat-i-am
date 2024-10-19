
import flet as ft
from math import pi
import random
import time

def main(page: ft.Page):

    def ran_cat():
        num = random.randint(1, 12)
        if num == 1:
            result="Gato Enojao","imgs/gato_enojao.jpg"
        elif num == 2:
            result="Gato Paciente","imgs/gato_escucha.jpg"
        elif num == 3:
            result="Gato Feli","imgs/gato_feli.jpg"
        elif num == 4:
            result="Gato Fiestero","imgs/gato_fiesta.jpg"
        elif num == 5:
            result="Gato GoGoGO","imgs/gato_gogogo.jpg"
        elif num == 6:
            result="Gato Hambriado","imgs/gato_hambre.jpg"
        elif num == 7:
            result="Gato Inteligente","imgs/gato_inteligente.jpg"
        elif num == 8:
            result="Gato Lindo","imgs/gato_lindo.jpg"
        elif num == 9:
            result="Gato Mimi","imgs/gato_mimi.jpg"
        elif num == 10:
            result="Gato Serio","imgs/gato_serio.jpg"
        elif num == 11:
            result="Gato Sus","imgs/gato_sus.jpg"
        elif num == 12:
            result="Gato Triste","imgs/gato_triste.jpg"
        return result
    
    def close_banner(e):
        page.banner.open = False
        page.update()

    def show_banner_click(e, result):
        page.banner.open = True
        page.banner.content = ft.Column([
            ft.Container(ft.Text(result[0])),
            ft.Container(ft.Image (src=f"{result[1]}",width=300,height=300,)),
        ])
        page.update()
    
    animation_speed = 100
    size_chart = 200
    page.cat = ran_cat()
    page.banner = ft.AlertDialog(
        modal=True,
        title=ft.Text("Eres un gato..."),
        actions=[
            ft.TextButton("Salir", on_click=close_banner),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.update()

    chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                8,
                color=ft.colors.BLUE,
                radius=size_chart,
                
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.YELLOW,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.PINK,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.GREEN,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.BLUE,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.YELLOW,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.PINK,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.GREEN,
                radius=size_chart,
            ),ft.PieChartSection(
                8,
                color=ft.colors.BLUE,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.YELLOW,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.PINK,
                radius=size_chart,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.GREEN,
                radius=size_chart,
            ),
        ],
        sections_space=0,
        center_space_radius=0,
        expand=True,
    )

    c = ft.Container(
        ft.Container(chart, alignment=ft.alignment.center,),
        width=300,
        height=300,
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        alignment=ft.alignment.center,
        animate_rotation=ft.animation.Animation(animation_speed),
    )

    

    def animate(e):
        seconds_to_run = random.randint(3, 5)
        animation_speed = 100000
        

        start_time = time.time()
        while time.time() - start_time < seconds_to_run:
            c.rotate.angle += 1
            animation_speed = animation_speed - 10
            c.animate_rotation = ft.animation.Animation(animation_speed)
            page.update()

        animation_speed = 0
        c.animate_rotation = ft.animation.Animation(0)
        page.update()

        result = ran_cat()
        show_banner_click(e, result)

    base = ft.Container(
        content=ft.Column([
            ft.Container(ft.Icon(name=ft.icons.ARROW_DROP_DOWN_OUTLINED, color=ft.colors.BLACK, size=50),alignment=ft.alignment.top_center, margin=30),
            ft.Container(c,alignment=ft.alignment.center),
            ft.Container(ft.ElevatedButton("Miaw Miaw Miaw", on_click=animate),alignment=ft.alignment.bottom_center, margin=50),
            
            
        ])
    )   
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(base)

ft.app(main)