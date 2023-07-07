from flet import *
from .RecordList import RecordList 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./digihealthservicekey.json")
firebase_admin.initialize_app(cred,name='otherApp')

db = firestore.client()

class AddRecord(UserControl):
    def build(self):
        self.name = TextField(
            hint_text="Fullname",
            expand=True)
        self.gender = RadioGroup(
            content= Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=
            [
                Radio(value="male", label="Male"),
                Radio(value="female", label="Female"),
            ]),
        )
        self.age = TextField(
            hint_text="Age",
            expand=True)
        self.height = TextField(
            hint_text="Height/cm",
            expand=True)
        self.weight = TextField(
            hint_text="Weight/kg",
            expand=True)
        self.recordItems = ListView(height=220)

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                Tab(text="all"), 
                Tab(text="male"), 
                Tab(text="female"), 
                ],
        )

        return Column(
            width=600,
            height=550,
            controls=[
                Row([Text(value="Medical Record", style="headlineMedium")], alignment="center"),
                Row(
                    controls=[
                        self.name,self.gender,
                    ],
                ),
                Row(
                    controls=[
                        self.age,self.height,self.weight,
                    ],
                ),
                Row(
                    expand=True,
                    controls=[
                        FloatingActionButton(icon=icons.ADD,width=600,bgcolor=colors.GREEN_800, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    controls=[ 
                        self.filter,
                        self.recordItems,
                    ],
                ),
                Row(
                    alignment=MainAxisAlignment.START,
                    controls=[
                        OutlinedButton(
                            text="Clear All Records", on_click=self.clear_clicked
                        ),
                    ],
                ),
            ],
        )

    def did_mount(self):
        self.getrecords()
    
    def getrecords(self):
        records = db.collection(u'records').stream()
        self.recordItems.controls.clear()
        for record in records:
            print(record)
            self.recordItems.controls.append(RecordList(record.id,
                                                   record.to_dict()['name'],
                                                   record.to_dict()['gender'],
                                                   record.to_dict()['age'],
                                                   record.to_dict()['height'],
                                                   record.to_dict()['weight'],
                                                   self.getrecords,
                                                   self.deleterecord,db))
            self.update()

    def add_clicked(self,e):
        #self.recordItems.controls.append(recordItem(self.input.value,self.deleterecord))
        doc_ref = db.collection("records").document(self.name.value)
        doc_ref.set({
            u'name' : str(self.name.value),
            u'gender' : str(self.gender.value),
            u'age' : str(self.age.value),
            u'height' : str(self.height.value),
            u'weight' : str(self.weight.value),
        })

        self.name.value = ""
        self.age.value = ""
        self.height.value = ""
        self.weight.value = ""
        self.getrecords()

    def deleterecord(self,record):
        self.recordItems.controls.remove(record)
        self.update()

    def tabs_changed(self, e):
        gender = self.filter.tabs[self.filter.selected_index].text
        for i in self.recordItems.controls:
            i.visible = (
                gender == "all"
                or (gender == "male" and i.gender == "male")
                or (gender == "female" and i.gender == "female")
            )
        self.update()

    def clear_clicked(self, e):
        records_ref = db.collection(u'records')
        records = records_ref.stream()
        self.recordItems.controls.clear()
        for record in records:
            record.reference.delete()
        self.update()
