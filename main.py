  
from kivy.app import App 
from kivy.lang import Builder 

# Declara uma variável onde está o arquivo Kivy 
GUI = Builder.load_file("Interface.kv")

# Classe do aplicativo
# Todas as funções vão aqui dentro
class MeuAplicativo(App):
    # Função de contrução do app
    def build(self):
        return GUI


# Roda o aplicativo
MeuAplicativo().run()