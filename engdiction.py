import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton

def finder():
    data = json.load(open('001 data.json', 'r'))
    try:
        found = data[text.text().strip().lower()]
        final = ''
        for a in found:
            final += a + '\n\n'
        result.setText(f'This is/are the meaning:\n{final}')
    except:
        result.setText(f'Word not found')

app = QApplication([])
window = QWidget()
window.setWindowTitle("Ibude's Dictionary")


layout = QVBoxLayout()


description = QLabel('Input the Unknown Word here')
layout.addWidget(description)

layout2 = QHBoxLayout()
layout.addLayout(layout2)

text = QLineEdit()
layout2.addWidget(text)

btn = QPushButton('Search')
btn.clicked.connect(finder)
layout2.addWidget(btn)

result = QLabel('')
layout.addWidget(result)

window.setLayout(layout)
window.show()
app.exec()