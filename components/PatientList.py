from flet import *

class PatientList(UserControl):
    def __init__(self,id,name,course,yrsec,medcondition,getPatients,deletepatient,db):
        super().__init__()
        self.current_view = None
        self.id = id
        self.name = name
        self.course = course
        self.yrsec = yrsec
        self.medcondition = medcondition
        self.getPatients = getPatients
        self.delete = deletepatient
        self.db = db

    def build(self):
        
        self.nameText = Text(value=str(self.name),size=15)
        self.courseText = Text(value=str(self.course),size=15)
        self.yrsecText = Text(value=str(self.yrsec),size=15)
        self.medconditionText = Text(value=str(self.medcondition),size=15)
        self.edit_name = TextField(value=str(self.name),expand=1)
        self.edit_course = Dropdown(
            value=str(self.course),
            width=100,
            hint_text="Course",
            expand=True,
            options=[
                dropdown.Option("BSIT"),
                dropdown.Option("BSFi"),
                dropdown.Option("BSEd"),
                dropdown.Option("BSEntrep"),
            ],
        )
        self.edit_yrsec = TextField(value=str(self.yrsec),expand=1)
        self.edit_medcondition = TextField(value=str(self.medcondition),expand=1)

        self.display_view = Row( 
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.nameText,
                self.courseText,
                self.yrsecText,
                self.medconditionText,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.REMOVE_RED_EYE_OUTLINED,
                            tooltip="View",
                            icon_color=colors.ORANGE_100
                        ),
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit",
                            on_click=self.edit_clicked,
                            icon_color=colors.BLUE_500
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete",
                            on_click=self.delete_clicked,
                            icon_color=colors.RED_500
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                self.edit_course,
                self.edit_yrsec,
                self.edit_medcondition,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Save",
                    on_click=self.save_clicked,
                ),
                IconButton(
                    icon=icons.CANCEL_OUTLINED,
                    icon_color=colors.RED,
                    tooltip="Cancel",
                    on_click=self.cancel,
                ),
            ],
        )

        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def cancel(self,e):
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def save_clicked(self, e):
        newName = str(self.edit_name.value)
        newCourse = str(self.edit_course.value)
        newYrsec = str(self.edit_yrsec.value)
        newMedcondition = str(self.edit_medcondition.value)
        doc_ref =self.db.collection(u'patients').document(self.id)
        doc_ref.update({
            u'name' : newName,
            u'course' : newCourse,
            u'yrsec' : newYrsec,
            u'medcondition' : newMedcondition
        }

        )
        self.display_view.visible = True
        self.edit_view.visible = False
        self.getPatients()

    # def status_changed(self, e):
    #     doc_ref = self.db.collection(u'patients').document(self.id)

    #     if (self.display_info.value == True):
    #         doc_ref.update({
    #             u'completed' : not self.completed
    #         })
            
    #     else :
    #         doc_ref.update({
    #             u'completed' : not self.completed
    #         })

    #     self.getPatients()

    def delete_clicked(self, e):
        self.delete(self)
        self.db.collection(u'patients').document(self.id).delete()
        self.getPatients()

