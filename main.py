from flet import *
from components.AddPatient import AddPatient
from components.StaffContainer import StaffContainer
from components.LineChart import LineCharts
from components.BarChart import BarCharts
from components.Members import Members
from components.AddRecord import AddRecord

def main(page: Page):
    page.title = "DIGIHEALTH SPACE"
    page.theme_mode = ThemeMode.DARK
    page.window_full_screen = True

    def theme_changed(e):
        if page.theme_mode == ThemeMode.LIGHT:
            page.theme_mode = ThemeMode.DARK
            dark_light_text.value = "Dark theme"
        else:
            page.theme_mode = ThemeMode.LIGHT
            dark_light_text.value = "Light theme"
        page.update()

    def back(e):
        page.clean()
        page.add(
            Row(
            expand=True,
            controls=[
                view,VerticalDivider(width=1)
            ]
    )
        )
        page.update()

    def patient_nav_change(e):
        page.clean()
        page.add(
            Row(
                expand=True,
                controls=[
                    view,VerticalDivider(width=1),
                    Container(
                        alignment=alignment.center,
                        margin = margin.only(left=250,top=10),
                        content=AddPatient()
                    )
                ]
            )
        )
        page.update()
    
    def staff_nav_change(e):
        page.clean()
        page.add(
            Row(
                expand=True,
                controls=[
                    view,VerticalDivider(width=1),
                    Container(
                        alignment=alignment.center,
                        margin = margin.only(left=400,top=40),
                        content=StaffContainer()
                    )
                ]
            )
        )
        page.update()

    def linechart_nav_change(e):
        page.clean()
        page.add(
            IconButton(
                    icon=icons.ARROW_BACK_ROUNDED,
                    icon_color=colors.GREY_600,
                    icon_size=25,
                    tooltip="Back",
                    on_click=back
                ),
             Container(
                        alignment=alignment.center,
                        margin = margin.only(left=0,top=30),
                        content=
                            Text(
                                spans=[
                                    TextSpan(
                                        "VISITS FOR THE YEAR 2022",
                                        TextStyle(
                                            size=30,
                                            weight=FontWeight.BOLD,
                                            color=colors.WHITE70
                                        ),
                                    ),
                                ],
                            ), 
                    ),
                    Container(
                        alignment=alignment.center,
                        margin = margin.only(left=100,top=150),
                        content=LineCharts()                       
                        
                    )
        )
        page.update()

    def barchart_nav_change(e):
        page.clean()
        page.add(
            IconButton(
                    icon=icons.ARROW_BACK_ROUNDED,
                    icon_color=colors.GREY_600,
                    icon_size=25,
                    tooltip="Back",
                    on_click=back
                ),
             Container(
                        alignment=alignment.center,
                        margin = margin.only(left=0,top=30),
                        content=
                            Text(
                                spans=[
                                    TextSpan(
                                        "COMBINED VISITS FOR THE YEAR 2022-2023",
                                        TextStyle(
                                            size=30,
                                            weight=FontWeight.BOLD,
                                            color=colors.WHITE70
                                        ),
                                    ),
                                ],
                            ), 
                    ),
            Container(
                alignment=alignment.center,
                margin = margin.only(left=10,top=150),
                content=BarCharts()                       
                
            )
        )
        page.update()

    def member_nav_change(e):
        page.clean()
        page.add(
            Row(
                expand=True,
                controls=[
                    view,VerticalDivider(width=1),
                    Container(
                        alignment=alignment.center,
                        margin = margin.only(left=100,top=100),
                        content=Members()
                    )
                ]
            )
        )
        page.update()

    def open_modal(e):
        page.dialog = modal 
        modal.open = True
        page.update()

    def close_modal(e):
        modal.open=False
        page.update()

    def close_page(e):
        page.window_close()
    def minimize_page(e):
        page.window_minimized = True
    def maximize_page(e):
        page.window_maximized =True

    dark_light_text = Text("Light theme")

    page.appbar = AppBar(
        leading=Icon(icons.HEALTH_AND_SAFETY_SHARP, size=60, color=colors.AMBER_400),
        leading_width=100,
        title=Text("DIGIHEALTH SPACE", size=32, text_align="start", weight=FontWeight.BOLD),
        center_title=False,
        toolbar_height=110,
        bgcolor=colors.GREEN_800,
        actions=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="About Us"),
                    PopupMenuItem(),  # divider
                    PopupMenuItem(text="Contact Us"),
                    PopupMenuItem(),  # divider
                    PopupMenuItem(text="Careers"),
                ]
            ),
            IconButton(icons.REMOVE_ROUNDED,tooltip="minimize",on_click=minimize_page),
            IconButton(icons.CROP_SQUARE_ROUNDED,tooltip="maximize",on_click=maximize_page),
            IconButton(icons.CLOSE_ROUNDED,tooltip="close",on_click=close_page),
        ]
    )

    txt1 = Row([Text("People")], alignment="start")
    txt2 = Row([Text("Charts")], alignment="start")
    txt3 = Row([Text("Records")], alignment="start")

    div = Container(
        bgcolor=colors.GREY_800,
        border_radius=border_radius.all(30),
        height=1,
        alignment=alignment.center_right,
        width=220
    )

    theme = Row(
        controls=[
            IconButton(
                icon=icons.BRIGHTNESS_2_OUTLINED,
                tooltip="Toggle brightness",
                on_click=theme_changed,
            ),
            dark_light_text,
        ]
    )

    modal = AlertDialog(
        modal = True,
        content = AddRecord(),
        actions=[
            TextButton('Close', on_click=close_modal)
        ],
        actions_alignment=MainAxisAlignment.END
    )

    view = Container(
        content=Column(
        alignment=MainAxisAlignment.START,
        spacing=20,
        controls=[
            txt1, div,
            TextButton("Staff", icon=icons.PEOPLE, on_click=staff_nav_change),
            TextButton("Members", icon=icons.EMOJI_PEOPLE, on_click=member_nav_change),
            TextButton("Patients", icon=icons.PERSON, on_click=patient_nav_change),
            txt2, div,
            TextButton("Line Chart", icon=icons.SSID_CHART, on_click=linechart_nav_change),
            TextButton("Bar Chart", icon=icons.BAR_CHART_ROUNDED, on_click=barchart_nav_change),
            txt3, div,
            TextButton("Add Record", icon=icons.EVENT_NOTE, on_click=open_modal),
            Container(
                content=theme,
                margin=margin.only(top=90)
            )
        ]
    ),
        padding=padding.only(top=15, left=10),
        margin=margin.all(0),
        width=200,
        height=690,
    )

    page.add(Row(
        expand=True,
        controls=[
            view,VerticalDivider(width=1)
        ]
    ))

    page.update()


app(target=main)
