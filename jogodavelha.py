import PySimpleGUI as sg

moves = ' XO'
board = [[' '] * 3] * 3

layout = [[sg.Button(' ', size=(4, 2), key=(row, col)) for col in range(3)] for row in range(3)] + [[sg.Button('Play'), sg.Exit()]]

window = sg.Window('Tic Tac Toe').Layout(layout)

while True: # Loop
    event, values = window.Read()
    if event in (None, 'Exit'):  
        break
    if event == 'Play':
        continue
    else:
        button = window.Element(event)  
        board[event[0]][event[1]] = moves[(moves.index(board[event[0]][event[1]])+1)%len(moves)]
        button.Update(board[event[0]][event[1]])
window.Close()
