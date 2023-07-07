from flet import *

class PatientDashboard(UserControl):
    def build(self):

        self.barchart = BarChart(
            bar_groups=[
                BarChartGroup(
                    x=0,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=12,
                            width=35,
                            color=colors.RED_600,
                            tooltip="1st Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=23,
                            width=35,
                            color=colors.GREEN_600,
                            tooltip="2nd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=35,
                            width=35,
                            color=colors.DEEP_PURPLE_200,
                            tooltip="3rd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=41,
                            width=35,
                            color=colors.BROWN_600,
                            tooltip="4th Year",
                            border_radius=15
                        ),
                    ]
                ),
                BarChartGroup(
                    x=1,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=32,
                            width=35,
                            color=colors.RED_600,
                            tooltip="1st Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=22,
                            width=35,
                            color=colors.GREEN_600,
                            tooltip="2nd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=43,
                            width=35,
                            color=colors.DEEP_PURPLE_200,
                            tooltip="3rd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=17,
                            width=35,
                            color=colors.BROWN_600,
                            tooltip="4th Year",
                            border_radius=15
                        ),
                    ]
                ),
                BarChartGroup(
                    x=3,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=21,
                            width=35,
                            color=colors.RED_600,
                            tooltip="1st Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=45,
                            width=35,
                            color=colors.GREEN_600,
                            tooltip="2nd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=50,
                            width=35,
                            color=colors.DEEP_PURPLE_200,
                            tooltip="3rd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=42,
                            width=35,
                            color=colors.BROWN_600,
                            tooltip="4th Year",
                            border_radius=15
                        ),
                    ]
                ),
                BarChartGroup(
                    x=2,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=14,
                            width=35,
                            color=colors.RED_600,
                            tooltip="1st Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=28,
                            width=35,
                            color=colors.GREEN_600,
                            tooltip="2nd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=45,
                            width=35,
                            color=colors.DEEP_PURPLE_200,
                            tooltip="3rd Year",
                            border_radius=15
                        ),
                        BarChartRod(
                            from_y=0,
                            to_y=35,
                            width=35,
                            color=colors.BROWN_600,
                            tooltip="4th Year",
                            border_radius=15
                        ),
                    ]
                ),
                
                
                
            ],
            border=border.all(1,colors.BLUE_100),
            left_axis=ChartAxis(
            title_size=40,
            title=Text("Number of Visits"),
            labels_interval=10,
            labels_size=40,
            ),
            bottom_axis=ChartAxis(
                labels_size=40,
                labels=[
                    ChartAxisLabel(
                        value=0,
                        label=Container(Text("BSIT"),padding=10)
                    ),
                    ChartAxisLabel(
                        value=1,
                        label=Container(Text("BSEntrep"),padding=10)
                    ),
                    ChartAxisLabel(
                        value=2,
                        label=Container(Text("BSEduc"),padding=10)
                    ),
                    ChartAxisLabel(
                        value=3,
                        label=Container(Text("BSFi"),padding=10)
                    ),



                ]

            ),
            horizontal_grid_lines=ChartGridLines(
                color = colors.GREY_500,
                width=1,
                dash_pattern=[3,3]
            ),
            tooltip_bgcolor=colors.with_opacity(0.5,colors.WHITE),
            max_y=60,
            interactive=True,
            expand=True
        )



        return Container(
            content=self.barchart
        )


        
    
    