
import flet as ft
from math import pi
import random
import time

def main(page: ft.Page):
    
    animation_speed = 100

    down_arrow = ft.Icon(name=ft.icons.ARROW_DROP_DOWN_OUTLINED, color=ft.colors.BLACK, size=50),

    chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                8,
                color=ft.colors.BLUE,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.YELLOW,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.PINK,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.GREEN,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.BLUE,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.YELLOW,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.PINK,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.GREEN,
                radius=100,
            ),ft.PieChartSection(
                8,
                color=ft.colors.BLUE,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.YELLOW,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.PINK,
                radius=100,
            ),
            ft.PieChartSection(
                8,
                color=ft.colors.GREEN,
                radius=100,
            ),
        ],
        sections_space=0,
        center_space_radius=0,
        expand=True,
    )

    c = ft.Container(
        chart,
        width=100,
        height=100,
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(animation_speed),
    )
    

    def animate(e):
        seconds_to_run = random.randint(3, 5)
        animation_speed = 100000
        

        start_time = time.time()
        while time.time() - start_time < seconds_to_run:
            c.rotate.angle += pi
            animation_speed = animation_speed - 10
            c.animate_rotation = ft.animation.Animation(animation_speed)
            page.update()

        animation_speed = 0
        c.animate_rotation = ft.animation.Animation(0)
        page.update()

        # while c.rotate.angle > or animation_speed >= 0:
        #     print(animation_speed)
        #     # print(c.rotate.angle)
        #     # if c.rotate.angle <= 0:
        #     #     c.rotate.angle = pi / 2
        #     # else:
        #     #     c.rotate.angle -= pi / 2

        #     # if animation_speed <= 0:
        #     #     animation_speed = 0
        #     # else:
        #     #     animation_speed = animation_speed - 10
        #     c.animate_rotation = ft.animation.Animation(animation_speed)
        #     page.update()
        
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        c,
        ft.ElevatedButton("Animate!", on_click=animate),
    )

ft.app(main)