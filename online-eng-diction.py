import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt6.QtCore import QThread, pyqtSignal


class DictionaryThread(QThread):
    result_ready = pyqtSignal(str)

    def __init__(self, word):
        super().__init__()
        self.word = word

    def run(self):
        try:
            url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{self.word}'
            r = requests.get(url)
            j = r.json()
            final = ''
            word = j[0].get('word', '')
            phonetics = j[0].get('phonetics', [])
            audio = ''
            for ph in phonetics:
                if ph.get('audio'):
                    audio = ph['audio']
                    break
            source = j[0].get('sourceUrls', [])
            urls = '\n'.join(source)
            meanings = j[0].get('meanings', [])
            for meaning in meanings:
                part_of_speech = meaning.get('partOfSpeech', '')
                for definition in meaning.get('definitions', []):
                    def_text = definition.get('definition', '')
                    syns = ', '.join(definition.get('synonyms', []))
                    ants = ', '.join(definition.get('antonyms', []))
                    final += f"{part_of_speech}: {def_text}\n"
                    if syns:
                        final += f"  Synonyms: {syns}\n"
                    if ants:
                        final += f"  Antonyms: {ants}\n"
                    example = definition.get('example', '')
                    if example:
                        final += f"  Example: {example}\n"
                    final += "\n"

            output = f'This is/are the meaning of {word}:\n{final}\nAudio: {audio}\nSource: {urls}'
            self.result_ready.emit(output)
        except Exception as e:
            self.result_ready.emit('You are either offline or Word not found')


def finder():
    found = text.text().strip().lower()
    result.setText("Searching...")
    thread = DictionaryThread(found)
    thread.result_ready.connect(result.setText)
    thread.start()


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
