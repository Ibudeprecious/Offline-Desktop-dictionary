import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton

def finder():
    data = json.load(open('001 data.json', 'r'))
    try:
        found = data[text.text().strip()]
        final = ''
        for a in found:
            final += a + '\n\n'
        result.setText(f'This is/are the meaning:\n{final}')
    except:
        result.setText(f'{text.text()} is not an English Word. Please enter an English Word')

app = QApplication([])
window = QWidget()
window.setWindowTitle("Ibude's Dictionary")


layout = QVBoxLayout()


description = QLabel('Input the Unknown Word here')
layout.addWidget(description)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Search')
btn.clicked.connect(finder)
layout.addWidget(btn)

result = QLabel('')
layout.addWidget(result)

window.setLayout(layout)
window.show()
app.exec()