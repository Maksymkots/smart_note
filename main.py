from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox , QInputDialog
from ui import Ui_MainWindow

import json

class NoteWindow(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes={}
        self.read_notes()
        self.connects()

    def connects(self):
        self.ui.note_list.itemClicked.connect(self.show_note)
        self.ui.new_note_btn.clicked.connect(self.add_note)
        self.ui.save_note_btn.clicked.connect(self.save_note)
        self.ui.delete_note_btn.clicked.connect(self.del_note)
        self.ui.add_tag_btn.clicked.connect(self.add_tag)
        self.ui.del_teg_btn.clicked.connect(self.del_teg)


        

    def read_notes(self):
        try:
            with open("notes.json","r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {"Ласкаво просимо в Розумні замітки!":{
                "текст":"Додайте свою першу замітку!","теги":[]
                }}
        self.ui.note_list.addItems(self.notes)

    

    def show_note(self):
        name = self.ui.note_list.selectedItems()[0].text()
        self.ui.note_title.setText(name)
        self.ui.note_text.setText(self.notes[name]["текст"])
        self.ui.teg_list.clear()
        self.ui.teg_list.addItems(self.notes[name]["теги"])

    def add_note(self):
        self.ui.note_title.clear()
        self.ui.note_text.clear()
        self.ui.teg_list.clear()

    def save_file(self):
        try:
            with open("notes.json","w",encoding="utf-8") as file:
                json.dump(self.notes, file, ensure_ascii=False)
        except:
            message = QMessageBox()
            message.setText("Не вдалось знайти")
            message.exec_()




    def save_note(self):
        title = self.ui.note_title.text()
        text = self.ui.note_text.toPlainText()
        if title not in self.notes:
            self.notes[title] = {"текст": text, "теги":[]}
        else:
            self.notes[title]["текст"] = text
        self.save_file()
        self.ui.note_list.clear()
        self.ui.note_list.addItems(self.notes)

    def del_note(self):
        title = self.ui.note_title.text()
        if title in self.notes:
            del self.notes[title]
            self.ui.note_list.clear()
            self.ui.note_list.addItems(self.notes)
            self.save_file()
            self.add_note()


    def add_tag(self):
        title = self.ui.note_title.text()
        teg_title, ok = QInputDialog.getText(self, "Введіть тег ")
        if ok and teg_title != "" and title!= "":
            self.notes[title]["теги"].append(tag_title)
            self.ui.teg_list.clear()
            self.ui.teg_list.addItems(self.notes[title]["теги"])


    def del_teg(self):
        title = self.ui.note_title.text()
        try:
            tag_title = self.ui.teg_listQInputDialog.getText(self, "Введіть тег ")
        except:
            teg_title = None
        if  tag_title and title!= "":
            self.notes[title]["теги"].remove(tag_title)
            self.ui.teg_list.clear()
            self.ui.teg_list.addItems(self.notes[title]["теги"])




app = QApplication([])
ex = NoteWindow()
ex.show()
app.exec_()

