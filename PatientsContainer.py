# from flet import *


# class PatientsView(UserControl):
#     def __init__(self, pat_name,pat_course,pat_yrsec, status_change, delete):
#         super().__init__()
#         self.completed = False
#         self.pat_name = pat_name
#         self.pat_course = pat_course
#         self.pat_yrsec = pat_yrsec
#         # self.status_change = status_change
#         self.delete = delete

#     def build(self):
#         self.display_info = Text(
#             value=str(self.pat_name) + " " + str(self.pat_course) + "-" + str(self.pat_yrsec)
#         )
#         self.edit_name = TextField(expand=1)

#         self.display_view = Row( 
#             alignment="spaceBetween",
#             vertical_alignment="center",
#             controls=[
#                 self.display_info,
#                 Row(
#                     spacing=0,
#                     controls=[
#                         IconButton(
#                             icon=icons.CREATE_OUTLINED,
#                             tooltip="Edit",
#                             on_click=self.edit_clicked,
#                             icon_color=colors.BLUE_500
#                         ),
#                         IconButton(
#                             icons.DELETE_OUTLINE,
#                             tooltip="Delete",
#                             on_click=self.delete_clicked,
#                             icon_color=colors.RED_500
#                         ),
#                     ],
#                 ),
#             ],
#         )

#         self.edit_view = Row(
#             visible=False,
#             alignment="spaceBetween",
#             vertical_alignment="center",
#             controls=[
#                 self.edit_name,
#                 IconButton(
#                     icon=icons.DONE_OUTLINE_OUTLINED,
#                     icon_color=colors.GREEN,
#                     tooltip="Save",
#                     on_click=self.save_clicked,
#                 ),
#             ],
#         )
#         return Column(controls=[self.display_view, self.edit_view])

#     def edit_clicked(self, e):
#         self.edit_name.value = self.display_info.value
#         self.display_view.visible = False
#         self.edit_view.visible = True
#         self.update()

#     def save_clicked(self, e):
#         self.display_info.value = self.edit_name.value
#         self.display_view.visible = True
#         self.edit_view.visible = False
#         self.update()

#     # def status_changed(self, e):
#     #     self.completed = self.display_info.value
#     #     self.status_change(self)

#     def delete_clicked(self, e):
#         self.delete(self)


# class TodoApp(UserControl):
#     def build(self):
#         self.new_name = TextField(
#             hint_text="Fullname",
#             on_submit=self.add_clicked,
#             expand=True)
#         self.new_course = TextField(
#             hint_text="Course",
#             on_submit=self.add_clicked,
#             expand=True)
#         self.new_yrsec = TextField(
#             hint_text="Year/Section",
#             on_submit=self.add_clicked,
#             expand=True)
#         self.patientItems = Column()

#         self.filter = Tabs(
#             selected_index=0,
#             on_change=self.tabs_changed,
#             tabs=[Tab(text="all"), Tab(text="confined"), Tab(text="discharged")],
#         )

#         return Column(
#             width=600,
#             controls=[
#                 Row([Text(value="Patient's View", style="headlineMedium")], alignment="center"),
#                 Row(
#                     controls=[
#                         self.new_name,
#                     ],
#                 ),
#                 Row(
#                     controls=[
#                         self.new_course,
#                     ],
#                 ),
#                 Row(
#                     controls=[
#                         self.new_yrsec,
#                         FloatingActionButton(icon=icons.ADD,width=300,bgcolor=colors.GREEN_800, on_click=self.add_clicked),
#                     ],
#                 ),
#                 Column(
#                     spacing=25,
#                     controls=[ 
#                         self.filter,
#                         self.patientItems,
#                         Row(
#                             alignment="spaceBetween",
#                             vertical_alignment="center",
#                             controls=[
#                                 OutlinedButton(
#                                     text="Clear Discharged Patients", on_click=self.clear_clicked
#                                 ),
#                             ],
#                         ),
#                     ],
#                 ),
#             ],
#         )

#     def add_clicked(self, e):
#         if self.new_name.value and self.new_course.value and self.new_yrsec:
#             patientItem = PatientsView(self.new_name.value,self.new_course.value,self.new_yrsec.value, self.status_change, self.delete)
#             self.patientItems.controls.append(patientItem)
#             self.new_name.value = ""
#             self.new_course.value = ""
#             self.new_yrsec.value = ""
#             self.new_name.focus()
#             self.new_course.focus()
#             self.new_yrsec.focus()
#             self.update()

#     def status_change(self, patientItem):
#         self.update()

#     def delete(self, patientItem):
#         self.patientItems.controls.remove(patientItem)
#         self.update()

#     def tabs_changed(self, e):
#         self.update()

#     def clear_clicked(self, e):
#         for patientItem in self.patientItems.controls[:]:
#             if patientItem.completed:
#                 self.delete(patientItem)

#     def update(self):
#         status = self.filter.tabs[self.filter.selected_index].text
#         for patientItem in self.patientItems.controls:
#             patientItem.visible = (
#                 status == "all"
#                 or (status == "confined" and patientItem.completed == False)
#                 or (status == "discharged" and patientItem.completed)
#             )
#         super().update()


# def main(page: Page):
#     page.title = "Patients View"
#     page.horizontal_alignment = "center"
#     page.scroll = "adaptive"
#     page.update()

#     page.add(TodoApp())

# app(target=main)