from flet import *

class LineCharts(UserControl):
    def build(self):

        self.data_1 = [
            #IT
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 2),
                    LineChartDataPoint(2, 10),
                    LineChartDataPoint(3, 30),
                    LineChartDataPoint(4, 50),
                    LineChartDataPoint(5, 5),
                    LineChartDataPoint(6, 15),
                ],
                stroke_width=4,
                color=colors.LIGHT_GREEN,
                curved=True,
                stroke_cap_round=True,
            ),
            #FI
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 20),
                    LineChartDataPoint(2, 46),
                    LineChartDataPoint(3, 16),
                    LineChartDataPoint(4, 39),
                    LineChartDataPoint(5, 21),
                    LineChartDataPoint(6, 5),
                ],
                color=colors.PINK,
                # below_line_bgcolor=colors.with_opacity(0, colors.PINK),
                stroke_width=4,
                curved=True,
                stroke_cap_round=True,
            ),
            #EDUC
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 46),
                    LineChartDataPoint(2, 50),
                    LineChartDataPoint(3, 32),
                    LineChartDataPoint(4, 37),
                    LineChartDataPoint(5, 7),
                    LineChartDataPoint(6, 30),
                ],
                color=colors.CYAN,
                stroke_width=4,
                curved=True,
                stroke_cap_round=True,
            ),
            #ENTREP
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 24),
                    LineChartDataPoint(2, 18),
                    LineChartDataPoint(3, 12),
                    LineChartDataPoint(4, 6),
                    LineChartDataPoint(5, 32),
                    LineChartDataPoint(6, 50),
                ],
                color=colors.AMBER,
                stroke_width=4,
                curved=True,
                stroke_cap_round=True,
            ),
        ]

        self.chart = LineChart(
            data_series=self.data_1,
            # horizontal_grid_lines=ChartGridLines(
            #     interval=1, color=colors.with_opacity(0.2, colors.ON_SURFACE), width=1
            # ),
            # vertical_grid_lines=ChartGridLines(
            #     interval=1, color=colors.with_opacity(0.2, colors.ON_SURFACE), width=1
            # ),
            border=Border(
                bottom=BorderSide(4, colors.with_opacity(0.5, colors.ON_SURFACE))
            ),
            left_axis=ChartAxis(
                labels=[
                    ChartAxisLabel(
                        value=10,
                        label=Text("10", size=14, weight=FontWeight.BOLD),
                    ),
                    ChartAxisLabel(
                        value=20,
                        label=Text("20", size=14, weight=FontWeight.BOLD),
                    ),
                    ChartAxisLabel(
                        value=30,
                        label=Text("30", size=14, weight=FontWeight.BOLD),
                    ),
                    ChartAxisLabel(
                        value=40,
                        label=Text("40", size=14, weight=FontWeight.BOLD),
                    ),
                    ChartAxisLabel(
                        value=50,
                        label=Text("50", size=14, weight=FontWeight.BOLD),
                    ),
                    ChartAxisLabel(
                        value=60,
                        label=Text("60", size=14, weight=FontWeight.BOLD),
                    ),
                ],
                labels_size=40,
            ),
            bottom_axis=ChartAxis(
                labels=[
                    ChartAxisLabel(
                        value=1,
                        label=Container(
                            Text(
                                "JAN-FEB",
                                size=16,
                                weight=FontWeight.BOLD,
                                color=colors.with_opacity(0.5, colors.ON_SURFACE),
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=2,
                        label=Container(
                            Text(
                                "MARCH-APRIL",
                                size=16,
                                weight=FontWeight.BOLD,
                                color=colors.with_opacity(0.5, colors.ON_SURFACE),
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=3,
                        label=Container(
                            Text(
                                "MAY-JUN",
                                size=16,
                                weight=FontWeight.BOLD,
                                color=colors.with_opacity(0.5, colors.ON_SURFACE),
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=4,
                        label=Container(
                            Text(
                                "JULY-AUG",
                                size=16,
                                weight=FontWeight.BOLD,
                                color=colors.with_opacity(0.5, colors.ON_SURFACE),
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=5,
                        label=Container(
                            Text(
                                "SEP-OCT",
                                size=16,
                                weight=FontWeight.BOLD,
                                color=colors.with_opacity(0.5, colors.ON_SURFACE),
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=6,
                        label=Container(
                            Text(
                                "NOV-DEC",
                                size=16,
                                weight=FontWeight.BOLD,
                                color=colors.with_opacity(0.5, colors.ON_SURFACE),
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=colors.with_opacity(0.8, colors.BLUE_GREY),
            min_y=0,
            max_y=60,
            min_x=0,
            max_x=9,
            # animate=5000,
            expand=True,
        )

        return Container(
            content=self.chart
        )


        
    
    