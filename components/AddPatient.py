from flet import *
from .PatientList import PatientList 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./digihealthservicekey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class AddPatient(UserControl):
    def build(self):
        self.name = TextField(
            hint_text="Fullname",
            expand=True)
        self.course = Dropdown(
            hint_text="Course",
            expand=True,
            options=[
                dropdown.Option("BSIT"),
                dropdown.Option("BSFi"),
                dropdown.Option("BSEd"),
                dropdown.Option("BSEntrep"),
            ],
        )
        self.yrsec = TextField(
            hint_text="Year/Section",
            expand=True)
        self.medcondition = TextField(
            hint_text="Medical Condition",
            expand=True)
        self.patientItems = ListView(height=180,spacing=10)

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                Tab(text="all"), 
                Tab(text="BSIT"), 
                Tab(text="BSFi"),
                Tab(text="BSEd"), 
                Tab(text="BSEntrep"), 
                ],
        )

        return Column(
            width=600,
            controls=[
                Row([Text(value="Patient's View", style="headlineMedium")], alignment="center"),
                Row(
                    controls=[
                        self.name,
                    ],
                ),
                Row(
                    controls=[
                        self.course,
                    ],
                ),
                Row(
                    controls=[
                        self.yrsec,
                    ],
                ),
                Row(
                    controls=[
                        self.medcondition,
                        FloatingActionButton(icon=icons.ADD,width=300,bgcolor=colors.GREEN_800, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[ 
                        self.filter,
                        self.patientItems,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                OutlinedButton(
                                    text="Clear All Patients", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    def did_mount(self):
        self.getPatients()
    
    def getPatients(self):
        patients = db.collection(u'patients').stream()
        self.patientItems.controls.clear()
        for patient in patients:
            print(patient)
            self.patientItems.controls.append(PatientList(patient.id,
                                                   patient.to_dict()['name'],
                                                   patient.to_dict()['course'],
                                                   patient.to_dict()['yrsec'],
                                                   patient.to_dict()['medcondition'],
                                                   self.getPatients,
                                                   self.deletepatient,db))
            self.update()

    def add_clicked(self,e):
        #self.patientItems.controls.append(patientItem(self.input.value,self.deletepatient))
        doc_ref = db.collection("patients").document(self.name.value)
        doc_ref.set({
            u'name' : str(self.name.value),
            u'course' : str(self.course.value),
            u'yrsec' : str(self.yrsec.value),
            u'medcondition' : str(self.medcondition.value),
        })

        self.name.value = ""
        self.yrsec.value = ""
        self.medcondition.value = ""
        self.getPatients()

    def deletepatient(self,patient):
        self.patientItems.controls.remove(patient)
        self.update()

    def tabs_changed(self, e):
        course = self.filter.tabs[self.filter.selected_index].text
        for i in self.patientItems.controls:
            i.visible = (
                course == "all"
                or (course == "BSIT" and i.course == "BSIT")
                or (course == "BSFi" and i.course == "BSFi")
                or (course == "BSEd" and i.course == "BSEd")
                or (course == "BSEntrep" and i.course == "BSEntrep")
            )
        self.update()

    def clear_clicked(self, e):
        patients_ref = db.collection(u'patients')
        patients = patients_ref.stream()
        self.patientItems.controls.clear()
        for patient in patients:
            patient.reference.delete()
        self.update()
