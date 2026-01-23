import flet as ft

THEME_COLOR = ft.Colors.RED

def MENU(page: ft.Page):
    # State variables
    is_expanded = True
    selected_index = 0  # Tracks which menu item is active
    
    # 1. Update Logic
    def toggle_rail(e):
        nonlocal is_expanded
        is_expanded = not is_expanded
        update_rail()

    def update_rail():
        # Toggle Menu Icon (Menu Open vs Close icons)
        menu_button.icon = ft.Icons.MENU_OPEN if is_expanded else ft.Icons.MENU
        
        # Update width and toggle text visibility
        rail.width = 200 if is_expanded else 65
        
        for i, item in enumerate(menu_items.controls):
            if isinstance(item, ft.ListTile):
                # Update text visibility
                item.title.visible = is_expanded
                # Update active state background color
                item.bgcolor = ft.Colors.with_opacity(0.1, THEME_COLOR) if selected_index == i else None
        
        rail.update()

    def handle_item_click(index):
        nonlocal selected_index
        selected_index = index
        update_rail()

    # 2. Define Menu Button separately to update its icon easily
    menu_button = ft.IconButton(
        icon=ft.Icons.MENU_OPEN, # Default open
        icon_color=THEME_COLOR,
        on_click=toggle_rail,
    )

    # 3. Create the items
    # We use a helper function or loop to assign indices
    items_data = [
        {"icon": ft.Icons.HOME, "label": "Home"},
        {"icon": ft.Icons.SETTINGS, "label": "Settings"},
        {"icon": ft.Icons.PERSON, "label": "Profile"},
    ]

    menu_items = ft.Column(spacing=5, horizontal_alignment="center")

    for idx, data in enumerate(items_data):
        menu_items.controls.append(
            ft.ListTile(
                leading=ft.Icon(data["icon"], color=THEME_COLOR),
                title=ft.Text(data["label"]),
                tooltip=data["label"],
                # Capture the index using a default argument in lambda
                on_click=lambda e, i=idx: handle_item_click(i),
                shape=ft.RoundedRectangleBorder(radius=8), # Nice rounded selection
                bgcolor=ft.Colors.with_opacity(0.1, THEME_COLOR) if selected_index == idx else None
            )
        )

    # 4. The Rail Container
    rail = ft.Container(
        content=ft.Column(
            [
                menu_button,
                ft.Divider(height=1,thickness=0, color=ft.Colors.TRANSPARENT),
                menu_items,
            ],
            horizontal_alignment="center",
        ),
        width=160,
        #bgcolor=ft.Colors.SURFACE,
        padding=5,
        animate=ft.Animation(400, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN),
    )

    # 5. Handle Window Resize
    def handle_resize(e):
        nonlocal is_expanded
        if page.width < 600 and is_expanded:
            is_expanded = False
            update_rail()
        elif page.width >= 600 and not is_expanded:
            is_expanded = True
            update_rail()

    page.on_resize = handle_resize

    return rail

