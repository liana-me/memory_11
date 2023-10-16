#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import *

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    #показать панель ответов 
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    # показать панель вопросов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    Question.setText(q.question)
    Otvet1.setText(q.right_answer)
    show_question() 
def next_question():
    '''window.next_q1 += 1 
    if window.next_q1 >= len(list_q):
        window.next_q1 = 0 
    q = list_q[window.next_q1]
    ask(q) # спросили'''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    question_с = randint(0, len(list_q) - 1)  
    q = list_q[question_с]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer() 
    else:
        next_question() 

def show_correct(res):
    Otvet.setText(res)
    show_result()

def check_answer():
    
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

list_q = [] 
list_q.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
list_q.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
list_q.append(Question('Какая настоящая фамилия у Сталина?', 'Джугашвили', 'Сталин', 'Петровский', 'Стальский'))
list_q.append(Question('Как зовут Гитлера?', 'Адольф', 'Арнольд', 'Фрэнсис', 'Джозеф'))
list_q.append(Question('Государственный язык России', 'Русский', 'Французский', 'Украинский', 'Английский'))
list_q.append(Question('Столица Дагестана', 'Махачкала', 'Дербент', 'Избербаш', 'Каспийск'))

app = QApplication([])

# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


ans1 = QHBoxLayout()   
ans2 = QVBoxLayout()
ans3 = QVBoxLayout()
ans2.addWidget(rbtn_1) 
ans2.addWidget(rbtn_2)
ans3.addWidget(rbtn_3) 
ans3.addWidget(rbtn_4)

ans1.addLayout(ans2)
ans1.addLayout(ans3)

RadioGroupBox.setLayout(ans1)

AnsGroupBox = QGroupBox("Результат теста")
Otvet = QLabel('правильно/неправильно') # здесь размещается надпись "правильно" или "неправильно"
Otvet1 = QLabel('правильный ответ') # здесь будет написан текст правильного ответа

res = QVBoxLayout()
res.addWidget(Otvet, alignment=(Qt.AlignLeft))
res.addWidget(Otvet1, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(res)


line1 = QHBoxLayout() # вопрос
line2 = QHBoxLayout() # варианты ответов или результат теста
line3 = QHBoxLayout() # кнопка "Ответить"

line1.addWidget(Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(RadioGroupBox)   
line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide()

 
line3.addStretch(1)
line3.addWidget(btn_OK, stretch=2) 
line3.addStretch(1)


card = QVBoxLayout()

card.addLayout(line1, stretch=2)
card.addLayout(line2, stretch=8)
card.addStretch(1)
card.addLayout(line3, stretch=1)
card.addStretch(1)
card.setSpacing(5) 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
window = QWidget()
window.setLayout(card)
window.setWindowTitle('Memo Card')
window.next_q1 = -1
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.resize(500, 400)
window.show()
app.exec()


