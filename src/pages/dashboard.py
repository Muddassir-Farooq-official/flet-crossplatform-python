import flet as ft
from shortcuts.helper import THEME_COLOR
import asyncio

data = [
    {
        "Name": "Alice",
        "Age": 30,
        "Occupation": "Engineer"
    },
    {
        "Name": "Bob",
        "Age": 25,
        "Occupation": "Designer"
    },
    {
        "Name": "Charlie",
        "Age": 35,
        "Occupation": "Teacher"
    }
]

class DashboardPage(ft.View):
    def __init__(self,page):
        super().__init__()

        self.search = ft.TextField(
            hint_text="Search",
            border_color=THEME_COLOR,
            border_radius=20,
            bgcolor="white",
            color=THEME_COLOR,
            cursor_color=THEME_COLOR,
            width=500,
            on_change=self.searching
        )
    
        self.source = ft.Column(
            [
                ft.Text("No data to display",color=THEME_COLOR)
            ]
        )        
        self.controls = [
            self.search,self.source
            
            
        ]
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        #self.bgcolor = ft.Colors.BLACK
        self.padding = 20
       
    
    def build(self):
        return self.controls
    

    def searching(self,e):
        query = self.search.value.lower()


        # filtered_data = [
        #     item for item in data
        #     if query in item["Name"].lower()
        # ]


        for x in data:
            if query in x["Name"].lower():
               self.source.controls = [
                   ft.Text(f"Name: {x['Name']}, Age: {x['Age']}, Occupation: {x['Occupation']}",color=THEME_COLOR)
               ]
               break
            else:
                self.source.controls = [
                     ft.Text("No matching data found",color=THEME_COLOR)
                ]

        self.update()
            # else:
            #    self.source.controls = [
            #        ft.Text("No matching data found",color=THEME_COLOR)
            # ]
            # self.update()

        # if filtered_data:
        #     self.source.controls = [
        #         ft.Text(f"Name: {item['Name']}, Age: {item['Age']}, Occupation: {item['Occupation']}",color=THEME_COLOR)
        #         for item in filtered_data
        #     ]
        # else:
        #     self.source.controls = [ft.Text("No matching data found",color=THEME_COLOR)]

        # self.update()
