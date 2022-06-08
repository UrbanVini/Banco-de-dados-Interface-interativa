import sqlite3
from telainicial import tela_inicial
#ALUNOS: Marcos Vinicius Gonçalves Pereira, Pedro da Silva Andrade Campos, Pablo Rocha da Cruz, João Pedro Arrighi Cavalcante da Silva.
class banco():
        def __init__(self, bd):
            self.con= sqlite3.connect(bd)
            self.cur= self.con.cursor()
            self.cur.execute('''CREATE TABLE alunos(
                matricula VARCHAR PRIMARY KEY,
                email VARCHAR(20),
                name VARCHAR (20),
                curso VARCHAR(30),
                campus VARCHAR(10)
            )''')
            self.con.commit()

        def cadastro(self, name, email, matricula, curso, campus):
            try:
               tela_inicial()
               cur = self.con.cursor()
               self.cur.execute('INSERT INTO alunos (name, email, matricula, curso, campus) VALUES (?, ?, ?, ?, ?)'), (name.get(), email.get(), matricula.get(), curso.get(), campus.get())
               self.con.commit()
               
            except sqlite3.Error as e:
                print('Erro no cadastro de dados: ', e)
            finally:
                if cur:
                    cur.close()
            
        
        def leitura(self):
            try:
                self.cur.execute('SELECT name, email, matricula, curso, campus FROM alunos')
                item = self.cur.fetchall()
                for linha in item:
                    print(linha)
            except sqlite3.Error as e:
                print('Erro na leitura de dados: ',e)

if __name__ == '__main__':
    bd = banco(":memory:")

    bd.cadastro(name='', email='', matricula='', curso='', campus='')
    bd.leitura()
    tela_inicial()


        

    
    
        





            
            
        


    
  