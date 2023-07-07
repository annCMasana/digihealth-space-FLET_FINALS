from flet import *

class Members(UserControl):
    def build(self):
        self.img = Column(
            controls=[
                Image(
                    src=f"img/doc1.jpg",
                    width=300,
                    height=300,
                    fit=ImageFit.CONTAIN,
                    border_radius=border_radius.all(10),
                ),
                Text("Paul Andrews", size=20,color=colors.WHITE,weight=FontWeight.BOLD),
                Text("Nurse",style=TextThemeStyle.HEADLINE_SMALL, italic=True, size=15),
            ]
        )
        
        self.img1 = Column(
            controls=[
                Image(
                    src=f"img/doc2.jpg",
                    width=300,
                    height=300,
                    fit=ImageFit.CONTAIN,
                    border_radius=border_radius.all(10),
                ),
                Text("Aisha Mays", size=20,color=colors.WHITE,weight=FontWeight.BOLD),
                Text("Assistant 1",style=TextThemeStyle.HEADLINE_SMALL, italic=True, size=15),
            ]
        )

        self.img2 = Column(
            controls=[
                Image(
                    src=f"img/doc3.jpg",
                    width=300,
                    height=300,
                    fit=ImageFit.CONTAIN,
                    border_radius=border_radius.all(10),
                ),
                Text("Antonio Irving", size=20,color=colors.WHITE,weight=FontWeight.BOLD),
                Text("Assistant 2",style=TextThemeStyle.HEADLINE_SMALL, italic=True, size=15),
            ]
        )

        self.row = Row(
            expand=1, 
            wrap=False, 
            scroll="always",
            controls=[
                self.img,self.img1,self.img2
            ]
        )

        self.title = Container(
            alignment=alignment.center,
            margin = margin.only(left=300,bottom=30),
            content=Text(
                        spans=[
                            TextSpan(
                                "Faculty Members",
                                TextStyle(
                                    size=30,
                                    weight=FontWeight.BOLD,
                                    color=colors.GREEN_200,
                                    decoration=TextDecoration.UNDERLINE
                                ),
                            ),
                        ],
                    )
        )

        return Column(
            [
                self.row,
                self.title
            ]
        )
    
    