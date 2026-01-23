import flet as ft
from shortcuts.helper import THEME_COLOR, MENU

class DashboardPage(ft.View):
    def __init__(self, page):
        super().__init__()

        self.controls = [
            ft.Row(
                [
                    MENU(page),
                    ft.VerticalDivider(width=1, color=THEME_COLOR),
                    
                    # 1. MAIN GRID (Expanded to take up most of the screen)
                    ft.Column(
                        [
                            ft.Text("(POS) Billing", size=24, weight="bold", color=THEME_COLOR),
                            ft.Row(
                                [
                                    ft.Container(
                                        height=180, width=180,
                                        bgcolor=THEME_COLOR,
                                        border_radius=10,
                                        alignment=ft.Alignment.CENTER,
                                        content=ft.Text("Product", color="white"),
                                    ) for _ in range(30)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                expand=True,
                                wrap=True,
                                scroll=ft.ScrollMode.AUTO,
                            ),
                        ],
                        expand=True, # This pushes the bill to the right
                        horizontal_alignment="center",
                        spacing=20,
                    ),
                    
                    # 2. BILLING CONTAINER (Fixed width for responsiveness)
                    ft.Container(
                        width=320,  # Fixed width keeps it looking like a sidebar bill
                        bgcolor="white",
                        margin=ft.margin.only(right=15, top=15, bottom=15),
                        padding=20,
                        
                        content=ft.Column(
                            [
                                ft.Text("BILL RECEIPT", color="black", weight="bold", size=22),
                                ft.Text("Order #12345", color="black54", size=12),
                                ft.Divider(color="black12", height=20),
                                
                                # Dummy Scrollable Items area
                                ft.Column([
                                    ft.Row([ft.Text("Item 1", color="black", weight="w500"), ft.Text("$20.00", color="black")], alignment="spaceBetween"),
                                    ft.Row([ft.Text("Item 2", color="black", weight="w500"), ft.Text("$15.50", color="black")], alignment="spaceBetween"),
                                    ft.Row([ft.Text("Item 3", color="black", weight="w500"), ft.Text("$10.00", color="black")], alignment="spaceBetween"),
                                ], scroll=ft.ScrollMode.AUTO, expand=True),
                                
                                ft.Divider(color="black", thickness=1),
                                
                                # Totals section
                                ft.Container(
                                    padding=ft.padding.only(top=10, bottom=20),
                                    content=ft.Column([
                                        ft.Row([
                                            ft.Text("Subtotal", color="black54"),
                                            ft.Text("$45.50", color="black54")
                                        ], alignment="spaceBetween"),
                                        ft.Row([
                                            ft.Text("Total:", color="black", weight="bold", size=18),
                                            ft.Text("$45.50", color="black", weight="bold", size=18)
                                        ], alignment="spaceBetween"),
                                    ])
                                ),
                                
                                ft.ElevatedButton(
                                    "COMPLETE CHECKOUT",
                                    bgcolor=THEME_COLOR,
                                    color="white",
                                    height=50,
                                    width=300,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                    )
                                )
                            ],
                        )
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=0
            )
        ]
        self.vertical_alignment = "start"
        self.horizontal_alignment = "start"
        self.padding = 0
        self.margin = 0

    def build(self):
        return self.controls