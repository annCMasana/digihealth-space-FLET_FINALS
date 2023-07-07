from flet import *

class StaffContainer(UserControl):
    def build(self):

        self.title = Container(
        content = Text(
            "Organizational Chart",
            color=colors.WHITE,
            weight=FontWeight.BOLD,
            font_family="Consolas",
            size=25
        ),
        bgcolor=colors.TRANSPARENT,
        padding=10,
        alignment=alignment.top_center,
        border=border.all(1.0,colors.WHITE54),
        margin=margin.all(5),
        )

        self.con = Container(
            alignment=alignment.center,
            margin = margin.only(left=-100,top=5),
            content=Image(
            src=f"img/head_nurse.jpg",
            width=500,
            height=500,
            fit=ImageFit.CONTAIN,
        )
        )

        return Column(
            [
                self.title,
                self.con
            ]
        )
    
    