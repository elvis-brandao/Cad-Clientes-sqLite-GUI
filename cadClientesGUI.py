import sqlite3 #biblioteca para banco de dados
import PySimpleGUI as sg #biblioteca para interface (GUI)

##################################################

# conectando...
conn = sqlite3.connect('clientes.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INTEGER,
	cpf	VARCHAR(11) NOT NULL,
	email TEXT NOT NULL,
	fone TEXT,
	cidade TEXT,
	uf VARCHAR(2) NOT NULL);""")

##################################################

# criando a janela (GUI)
sg.theme('Light Gray1')   # Add a touch of color
# Desingn of the window.
layout = [  [sg.Text('Nome:', size=(6, 1)), sg.InputText(size=(30,1), key='-NOME-')],
            [sg.Text('Idade:', size=(6, 1)), sg.InputText(size=(30,1), key='-IDADE-')],
            [sg.Text('CPF:', size=(6, 1)), sg.InputText(size=(30,1), key='-CPF-')],
            [sg.Text('e-mail:', size=(6, 1)), sg.InputText(size=(30,1), key='-EMAIL-')],
            [sg.Text('Fone:', size=(6, 1)), sg.InputText(size=(30,1), key='-FONE-')],
            [sg.Text('Cidade:', size=(6, 1)), sg.InputText(size=(30,1), key='-CIDADE-')],
            [sg.Text('UF:', size=(6, 1)), sg.InputText(size=(30,1), key='-UF-')],
            [ sg.Button('Cadastrar', button_color = 'black on orange', font = ['Comics', 12]), 
            sg.Button('Sair', button_color = 'black on red', font = ['Comics', 12]),
            sg.Button('Ver Registros', button_color = 'black on green', font = ['Comics', 12]) ],
            [sg.Output(size=(36,8), key='-OUTPUT-')] ]

# Create the Window
window = sg.Window('Cadastro de Clientes', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # if user closes window or clicks exit
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Cadastrar':
        try:
            # inserindo dados na tabela
            cursor.execute("""INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf)
            VALUES (?,?,?,?,?,?,?)""", (values['-NOME-'], values['-IDADE-'], values['-CPF-'], 
            values['-EMAIL-'], values['-FONE-'], values['-CIDADE-'], values['-UF-']))
            conn.commit() #NUNCA ESQUECER ESSE COMANDO
            print('Cliente cadastrado com sucesso!')
            window['-NOME-'].VALUES = ''
            window['-IDADE-'].VALUES = ''
            window['-CPF-'].VALUES = ''
            window['-EMAIL-'].VALUES = ''
            window['-FONE-'].VALUES = ''
            window['-CIDADE-'].VALUES = ''
            window['-UF-'].VALUES = ''
        except E:
            print(E)
    if event == 'Ver Registros':
        # lendo os dados
        print('\nOs dados salvos na base de dados são:')

        cursor.execute("""SELECT * FROM clientes;""")

        for linha in cursor.fetchall():
            print(linha)        

conn.close() # desconectando do banco de dados...
window.close()
##################################################
