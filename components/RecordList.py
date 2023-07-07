from flet import *

class RecordList(UserControl):
    def __init__(self,id,name,gender,age,height,weight,getRecords,deleterecord,db):
        super().__init__()
        self.current_view = None
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.getRecords = getRecords
        self.delete = deleterecord
        self.db = db

    def build(self):
        
        self.nameText = Text(value=str(self.name),size=15)
        self.genderText = Text(value=str(self.gender),size=15)
        self.ageText = Text(value=str(self.age),size=15)
        self.heightText = Text(value=str(self.height),size=15)
        self.weightText = Text(value=str(self.weight),size=15)
        self.edit_name = TextField(value=str(self.name),expand=1)
        self.edit_gender = RadioGroup(
            value=str(self.gender),
            content= Row([
                Radio(value="male", label="Male"),
                Radio(value="female", label="Female"),
            ]), 
        )
        self.edit_age = TextField(value=str(self.age),expand=1)
        self.edit_height = TextField(value=str(self.height),expand=1)
        self.edit_weight = TextField(value=str(self.weight),expand=1)
                

        self.title = Row(
            spacing=60,
            controls=[
                Text('FULLNAME', color=colors.YELLOW_200, weight=FontWeight.BOLD),
                Text('GENDER', color=colors.YELLOW_200, weight=FontWeight.BOLD),
                Text('AGE', color=colors.YELLOW_200, weight=FontWeight.BOLD),
                Text('HEIGHT', color=colors.YELLOW_200, weight=FontWeight.BOLD),
                Text('WEIGHT', color=colors.YELLOW_200, weight=FontWeight.BOLD),
            ]
        )

        self.display_view = Row( 
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.nameText,
                self.genderText,
                self.ageText,
                self.heightText,
                self.weightText,
                Row(
                    spacing=0,
                    controls=[
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
                self.edit_gender,
                self.edit_age,
                self.edit_height,
                self.edit_weight,
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

        return Column(controls=[self.title,self.display_view,self.edit_view])

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
        newGender = str(self.edit_gender.value)
        newAge = str(self.edit_age.value)
        newHeight = str(self.edit_height.value)
        newWeight = str(self.edit_weight.value)
        doc_ref =self.db.collection(u'records').document(self.id)
        doc_ref.update({
            u'name' : newName,
            u'gender' : newGender,
            u'age' : newAge,
            u'height' : newHeight,
            u'weight' : newWeight
        }

        )
        self.display_view.visible = True
        self.edit_view.visible = False
        self.getRecords()

    # def status_changed(self, e):
    #     doc_ref = self.db.collection(u'records').document(self.id)

    #     if (self.display_info.value == True):
    #         doc_ref.update({
    #             u'completed' : not self.completed
    #         })
            
    #     else :
    #         doc_ref.update({
    #             u'completed' : not self.completed
    #         })

    #     self.getRecords()

    def delete_clicked(self, e):
        self.delete(self)
        self.db.collection(u'records').document(self.id).delete()
        self.getRecords()


