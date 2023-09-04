import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QTextEdit, QTabWidget, QMessageBox

class User:
    def __init__(self, first_name, last_name, birth_date, address, is_pcd,male_checkbox,female_checkbox):
        self.first_name = first_name 
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.is_pcd = is_pcd 
        self.male_checkbox = male_checkbox
        self.female_checkbox = female_checkbox

class HospitalQueueApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Fila de Hospital")
        self.setGeometry(100, 100, 500, 500)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()

        self.tab_queue = QWidget()
        self.tab_processing = QWidget()
        self.tab_attended = QWidget()

        self.tab_widget.addTab(self.tab_queue, "Fila de Atendimento")
        self.tab_widget.addTab(self.tab_processing, "Em Atendimento")
        self.tab_widget.addTab(self.tab_attended, "Já Atendidos")

        self.layout.addWidget(self.tab_widget)

        self.init_queue_tab()
        self.init_processing_tab()
        self.init_attended_tab()

        self.queue = []
        self.processing_user = None
        self.attended_users = []
        self.timer = None

    def init_queue_tab(self):
        self.first_name_label = QLabel("Nome:")
        self.first_name_input = QLineEdit()

        self.last_name_label = QLabel("Sobrenome:")
        self.last_name_input = QLineEdit()

        self.birth_date_label = QLabel("Data de Nascimento (DD/MM/AAAA):")
        self.birth_date_input = QLineEdit()
        self.pcd_checkbox = QCheckBox("Pessoa com Deficiência (PCD)")

        self.address_label = QLabel("Endereço:")
        self.address_input = QLineEdit()
        
        
        self.female_checkbox = QCheckBox("Feminino")

        self.male_checkbox = QCheckBox("Masculino")
        self.male_checkbox.setChecked(True)
        self.male_checkbox.stateChanged.connect(self.on_checkbox_state_changed)
        
        self.enqueue_button = QPushButton("Entrar na Fila")
        self.enqueue_button.clicked.connect(self.enqueue_user)

        self.queue_text = QTextEdit()
        self.queue_text.setReadOnly(True)
        self.checkbox_layout = QVBoxLayout()
        layout = QVBoxLayout(self.tab_queue)
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.birth_date_label)
        layout.addWidget(self.birth_date_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.pcd_checkbox)
        layout.addWidget(self.male_checkbox)
        layout.addWidget(self.female_checkbox)
        


        self.female_checkbox.stateChanged.connect(self.on_checkbox_state_changed)

        
        layout.addWidget(self.enqueue_button)
        layout.addWidget(self.queue_text)
        self.layout.addLayout(self.checkbox_layout)
        
    def on_checkbox_state_changed(self):#TESTE que deu certo
        sender = self.sender()
        if sender == self.male_checkbox and sender.isChecked():
            self.female_checkbox.setChecked(False)
        elif sender == self.female_checkbox and sender.isChecked():
            self.male_checkbox.setChecked(False)
            
    def init_processing_tab(self):
        self.processing_text = QTextEdit()
        self.processing_text.setReadOnly(True)

        layout = QVBoxLayout(self.tab_processing)
        layout.addWidget(self.processing_text)

    def init_attended_tab(self):
        self.attended_text = QTextEdit()
        self.attended_text.setReadOnly(True)

        layout = QVBoxLayout(self.tab_attended)
        layout.addWidget(self.attended_text)

    def enqueue_user(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        birth_date = self.birth_date_input.text()
        address = self.address_input.text()
        is_pcd = self.pcd_checkbox.isChecked()

        male_checkbox = self.male_checkbox.isChecked()
        female_checkbox = self.female_checkbox.isChecked()

        if not (first_name and last_name and birth_date and address): 
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos.")
            return
        QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso!")
        user = User(first_name, last_name, birth_date, address, is_pcd, male_checkbox, female_checkbox)

        self.queue.append(user)
        self.update_queue_text()
        self.clear_fields()

        if not self.timer:
            self.process_next_user()

    def process_next_user(self):
        if self.queue:
            self.processing_user = self.queue.pop(0)
            self.update_queue_text()
            self.update_processing_text()
            self.timer = self.start_timer()
        else:
            self.processing_text.clear()
            self.processing_text.append("Nenhum usuário em atendimento.")
            self.queue_text.append("A fila está vazia.")

    def start_timer(self):
        return QTimer.singleShot(40000, self.finish_processing)

    def finish_processing(self):
        self.attended_users.append(self.processing_user)
        self.processing_user = None
        self.timer = None
        self.queue_text.append("Usuário anterior foi atendido. Próximo usuário será atendido em 40 segundos.")
        self.process_next_user()
        self.update_attended_text()

    def update_queue_text(self):
        self.queue_text.clear()
        self.queue_text.append("Fila de Atendimento:")
        for idx, user in enumerate(self.queue, start=1):
            self.queue_text.append(f"{idx}. {user.first_name} {user.last_name} - Prioridade: ")
        
        if not self.queue:
            self.queue_text.append("A fila está vazia.")

    def update_processing_text(self):
        self.processing_text.clear()
        if self.processing_user:
            self.processing_text.append("Usuário em atendimento:")
            self.processing_text.append(f"Nome: {self.processing_user.first_name} {self.processing_user.last_name}")
            self.processing_text.append(f"Data de Nascimento: {self.processing_user.birth_date}")
            self.processing_text.append(f"Endereço: {self.processing_user.address}")
            self.processing_text.append(f"Gênero Feminino: {self.processing_user.female_checkbox}")
            self.processing_text.append(f"Gênero Masculino: {self.processing_user.male_checkbox}")
        else:
            self.processing_text.append("Nenhum usuário em atendimento.")

    def update_attended_text(self):
        self.attended_text.clear()
        self.attended_text.append("Usuários Atendidos:")
        for idx, user in enumerate(self.attended_users, start=1):
            self.attended_text.append(f"{idx}. {user.first_name} {user.last_name}")
        if not self.attended_users:
            self.attended_text.append("Nenhum usuário foi atendido ainda.")

    def clear_fields(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.birth_date_input.clear()
        self.address_input.clear()
        self.pcd_checkbox.setChecked(False)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HospitalQueueApp()
    window.show()
    sys.exit(app.exec())