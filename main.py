#Импорт из библ. и др.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from design import Ui_MainWindow
from operator import add,sub,mul,truediv
from typing import Union,Optional

#Список мат. операций
operations = {
    '+' : add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

#Загрузка дизайна из файла.

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max_len =self.ui.main.maxLength()

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")


                    #Нажатие кнопок

        #Нажатие кнопок ( "0-9" )
        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        #Очистка строк ( "C-CE" )
        self.ui.btn_ce.clicked.connect (self.clear_temp)
        self.ui.btn_c.clicked.connect(self.clear_all)

        #Нажатие кнопки точки
        self.ui.btn_dot.clicked.connect(self.add_dot)

        #Нажатие кнопки деления,умножение
        self.ui.btn_divide.clicked.connect(lambda: self.add_temp('/'))
        self.ui.btn_multiply.clicked.connect(lambda: self.add_temp('*'))

        #Нажатие кнопки плюс,минус
        self.ui.btn_plus.clicked.connect(lambda: self.add_temp('+'))
        self.ui.btn_minus.clicked.connect(lambda: self.add_temp('-'))

        #Нажатие кнопки изменения знака
        self.ui.btn_plmi.clicked.connect(self.negate)

        #Нажатие кнопки равно
        self.ui.btn_equals.clicked.connect(self.calculate)

        # Нажатие кнопки Backspace
        self.ui.btn_backspace.clicked.connect(self.backspace)


    #Стирание
    def backspace(self) -> None:
        main = self.ui.main.text()
        if len (main) != 1:
            if len (main) == 2 and '-' in main:
                self.ui.main.setText('0')
            else:
                self.ui.main.setText(main [:-1])
        else:
            self.ui.main.setText('0')

    #Функция отрицания
    def negate(self):
        main = self.ui.main.text()
        if  '-' not in main:
            if main !='0':
                main = '-' + main
        else:
            main = main [1:]
        if len(main) == self.entry_max_len + 1 and '-' in main:
            self.ui.main.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.main.setMaxLength(self.entry_max_len)
        self.ui.main.setText(main)

    #Очистка поля ввода ( "main + temp" ) - Кнопка C
    def clear_all(self):
        self.ui.main.setText('0')
        self.ui.temp.clear ()

    # Очистка поля ввода ( "main" ) - Кнопка CE
    def clear_temp(self):
        self.ui.main.setText('0')

    #Добавление цифр в поле ввода ("main")
    def add_digit(self, btn_text: str):
        if self.ui.main.text() == '0':
            self.ui.main.setText(btn_text)
        else:
            self.ui.main.setText(self.ui.main.text() + btn_text)

    #Добавление точки
    def add_dot(self) -> None:
        if '.' not in self.ui.main.text():
            self.ui.main.setText (self.ui.main.text() + '.')

    #Обрезание незначащих нулей
    @staticmethod
    def  remove_trailing_zeros(num: str):
        n = str(float(num))  #Из str в float,обрезаються нули,кроме ".0"
        return n[:-2] if n[-2:] == '.0' else n #Обрезаются два последних знака если они = ".0"

    #Временное выражение
    def add_temp(self, math_sign: str):
        if not self.ui.temp.text() or self.get_math_sigh() == '=':
            self.ui.temp.setText(self.remove_trailing_zeros(self.ui.main.text()) + f' {math_sign} ')
            self.ui.main.setText('0')

    #Получение чисел из полей

         # Получение числа из ("main")
    def get_main_num(self) -> Union[int,float]:
        entry = self.ui.main.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

         # Получение числа из ("temp")
    def get_temp_num(self) -> Union[int,float,None]:
        if self.ui.temp.text():
            temps = self.ui.temp.text().strip('.').split()[0]
            return float(temps) if '.' in temps else int(temps)

        # Получение знака из ("temp")
    def get_math_sigh(self) -> Optional[str]:
        if self.ui.temp.text():
            return self.ui.temp.text().strip('.').strip()[-1]

    #Вычисление
    def calculate(self) -> Optional[str]:
        main = self.ui.main.text()
        temp = self.ui.temp.text()

        if temp:
            result = self.remove_trailing_zeros(
                str(operations[self.get_math_sigh()](self.get_temp_num(),self.get_main_num()))
            )
            self.ui.temp.setText(temp + self.remove_trailing_zeros(main) + ' =')
            self.ui.main.setText(result)
            return result

    #Математическая Операция
    def math_operation(self, math_sign: str):
        temp = self.ui.temp.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sigh() != math_sign:
                if self.get_math_sigh() == "=":
                    self.add_temp(math_sign)
                else:
                    self.ui.temp.setText(temp[:-2]+ f'{math_sign}')
            else:
                self.ui.temp.setText(self.calculate() + f'{math_sign}')


# Запуск программы
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()


    sys.exit(app.exec())