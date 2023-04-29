##############################################
## IMPORTS
##############################################
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
#########################
# IMPORT GUI FILE
from ui_view import *
##############################################
## MAIN WINDOW CLASS
##############################################


class MainWindow(QMainWindow):



    def html_file(self, file_2_list, len_list):
        i = 0
        empty_lines = 0
        comment_lines = 0
        while (i < len_list):
            line = file_2_list[i].strip()
            if (line == ''):
                empty_lines+=1
            elif (line.find('<!--') == 0):
                comment_lines+=1
                while (line.find('-->')+2 != len(line)-1):
                    if (line == ''):
                        empty_lines += 1
                    else :
                        comment_lines += 1
                    i += 1
                    line = file_2_list[i].strip()
            i+=1
        self.ui.empty_line_lbl.setText(str(empty_lines))
        self.ui.comment_line_lbl.setText(str(comment_lines))
        self.ui.code_line_lbl.setText(str((len_list + 1) - (comment_lines + empty_lines)))
        self.ui.total_line_lbl.setText(str(len_list + 1))


    def css_file(self, file_2_list, len_list):
        i = 0
        empty_lines = 0
        comment_lines = 0
        while (i < len_list):
            line = file_2_list[i].strip()
            if (line == ''):
                empty_lines+=1
            elif (line.find('/*') == 0):
                comment_lines+=1
                while (line.find('*/')+1 != len(line)-1):
                    if (line == ''):
                        empty_lines += 1
                    else :
                        comment_lines += 1
                    i += 1
                    line = file_2_list[i].strip()
            i+=1
        self.ui.empty_line_lbl.setText(str(empty_lines))
        self.ui.comment_line_lbl.setText(str(comment_lines))
        self.ui.code_line_lbl.setText(str((len_list + 1) - (comment_lines + empty_lines)))
        self.ui.total_line_lbl.setText(str(len_list + 1))


    def js_file(self, file_2_list, len_list):
        i = 0
        empty_lines = 0
        comment_lines = 0
        while (i < len_list):
            line = file_2_list[i].strip()
            if (line == ''):
                empty_lines += 1
            elif (line.find('//') == 0):
                comment_lines += 1
            elif (line.find('/*') == 0):
                comment_lines += 1
                while (line.find('*/') + 1 != len(line) - 1):
                    if (line == ''):
                        empty_lines += 1
                    else:
                        comment_lines += 1
                    i += 1
                    line = file_2_list[i].strip()
            i += 1
        self.ui.empty_line_lbl.setText(str(empty_lines))
        self.ui.comment_line_lbl.setText(str(comment_lines))
        self.ui.code_line_lbl.setText(str((len_list + 1) - (comment_lines + empty_lines)))
        self.ui.total_line_lbl.setText(str(len_list + 1))


    def python_file(self, file_2_list, len_list):
        i = 0
        empty_lines = 0
        comment_lines = 0
        while (i < len_list):
            line = file_2_list[i].strip()
            if (line == ''):
                empty_lines += 1
            elif (line.find('#') == 0):
                comment_lines += 1
            i += 1
        self.ui.empty_line_lbl.setText(str(empty_lines))
        self.ui.comment_line_lbl.setText(str(comment_lines))
        self.ui.code_line_lbl.setText(str((len_list + 1) - (comment_lines + empty_lines)))
        self.ui.total_line_lbl.setText(str(len_list + 1))


    def file_type_detection(self, file_name, file_2_list, len_list):
        i = len(file_name)-1
        ch = ''
        while (file_name[i] != '.'):
            ch = file_name[i] + ch
            i-=1
        if (ch == 'html'):
            self.html_file(file_2_list, len_list)
        elif (ch == 'css'):
            self.css_file(file_2_list, len_list)
        elif (ch == 'js'):
            self.js_file(file_2_list, len_list)
        elif (ch == 'py'):
            self.python_file(file_2_list, len_list)
        else :
            self.ui.error_msg_lbl.setText("We Are Currently Working On That Type Of File...")


    def name_file(self, path):
        i = len(path)-1
        ch = ''
        while (path[i] != '/'):
            ch = path[i] + ch
            i-=1
        self.ui.file_name_lbl.setText(ch)


    def my_app_line_counter(self, file_2_list, len_list):
        i = 0
        empty_lines = 0
        comment_lines = 0
        while (i < len_list):
            line = file_2_list[i].strip()
            if (line == ''):
                empty_lines += 1
            elif (line.find('#') == 0):
                comment_lines += 1
            i += 1

        self.ui.my_app_line_code_label.setText(str((len_list + 1) - (comment_lines + empty_lines)))


    def my_app_code_line(self):
        try:
            my_main_code = open('main.py', "r")
            len_my_file = open('main.py', "r")
            if (my_main_code.readable()):
                len_list = len(len_my_file.readlines()) - 1
                file_2_list = my_main_code.readlines()
                self.my_app_line_counter(file_2_list, len_list)
                my_main_code.close()
                len_my_file.close()
            else:
                self.ui.error_msg_lbl.setText('File Is Not Readable...!')
        except Exception as e:
            print(e)


    def browse(self):
        self.ui.empty_line_lbl.setText('00')
        self.ui.comment_line_lbl.setText('00')
        self.ui.code_line_lbl.setText('00')
        self.ui.total_line_lbl.setText('00')
        self.ui.file_name_lbl.setText('...')
        self.ui.error_msg_lbl.setText('')
        try:
            file_path = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);;")
            if (file_path[0] != ''):
                try:
                    file_to_convert = open(file_path[0], "r")
                    len_file_to_convert = open(file_path[0], "r")
                    self.name_file(file_path[0])
                    if (file_to_convert.readable()):
                        len_list = len(len_file_to_convert.readlines())-1
                        file_2_list = file_to_convert.readlines()
                        self.file_type_detection(file_path[0], file_2_list, len_list)
                        file_to_convert.close()
                        len_file_to_convert.close()
                    else:
                        self.ui.error_msg_lbl.setText('File Is Not Readable...!')
                except Exception as e:
                    print(e)
                    self.ui.error_msg_lbl.setText('File Is Not Readable...!')
        except Exception as e:
            print(e)
            self.ui.error_msg_lbl.setText('File Is Not Readable...!')


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("O N L Y   C O D E")
        self.showNormal()

        self.my_app_code_line()
        self.ui.browse_btn.clicked.connect(self.browse)


        self.show()
try:
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        Window = MainWindow()
        sys.exit(app.exec_())
except :
    print("erreur lors du chargenet de lapplication")