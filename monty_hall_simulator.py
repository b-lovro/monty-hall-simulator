import PySimpleGUI as sg
import random
import matplotlib.pyplot as plt
from numpy import cumsum

door_selected_image= b'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'
door_default=b'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'
door_goat=b'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'
door_car=b'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'

class Game:
    def __init__(self):
        self.stay_wins = []
        self.switch_wins = []
        self.temp = ''
        self.opened_door = 0
        self.selected_door = 0
        self.num_games = 0
        self.num_wins = 0
        self.layout1 = [
            [sg.Button('Start game', key="start_game", visible=True)]
        ]
        self.layout2 = [
            [sg.Text('Select one of the doors', size=(30, 1), key='text')],
            [sg.Button('', image_data=door_default, button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       border_width=0, key='door1'),
             sg.Button('', image_data=door_default, button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       border_width=0, key='door2'),
             sg.Button('', image_data=door_default, button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       border_width=0, key='door3')],
            [sg.Button('Switch', key="switch", visible=False)],
            [sg.Button('Stay with your choice', key="stay", visible=False)],
            [sg.Text('', size=(30, 1), key='text_end')],
            [sg.Button('Play new game', key="new_game", visible=False)],
            [sg.Button('Exit game', key="exit_game")],
            [sg.Text('', size=(30, 1), key='text_games')],
            [sg.Multiline(size=(30, 1), key='textbox', visible=False)],
            [sg.Button('Show results after x games', key="hundred_games", visible=False)]
        ]
        self.layout = [
            [sg.Column(self.layout1, key='layout1', visible=True), sg.Column(self.layout2, key='layout2', visible=False)]
        ]
        self.window = sg.Window('Monty Hall', resizable=True, size=(300, 100)).Layout(self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'exit_game':
                break
            elif event == 'start_game':
                self.start_game()
            elif event == 'new_game':
                self.new_game()

    def start_game(self):
        self.window['layout1'].update(visible=False)
        self.window['layout2'].update(visible=True)
        self.window.size = (600, 600)
        self.num_games += 1
        self.game()

    def set_doors(self):
        door_values = [0, 0, 0]
        car_door = random.randint(0, 2)
        door_values[car_door] = 1
        return {
            'door1': door_values[0],
            'door2': door_values[1],
            'door3': door_values[2]
        }

    def game(self):
        self.temp = ''
        door_values = self.set_doors()
        event, values = self.window.read()
        if event in ['door1', 'door2', 'door3'] and self.temp == '':
            self.temp = event
            self.selected_door = int(event[-1])
            self.window[event].update(image_data=door_selected_image)
            self.window['text'].update(value='You can stay with your choice or switch')
            self.opened_door = self.open_door(self.selected_door, door_values)
            self.decision(self.opened_door, self.selected_door, door_values)

    def open_door(self, selected, door_values):
        first, second = (2, 3) if selected == 1 else (1, 3) if selected == 2 else (1, 2)
        if door_values[f'door{selected}'] != 1:
            if door_values[f'door{first}'] == 0:
                self.window[f'door{first}'].update(image_data=door_goat)
                return first
            else:
                self.window[f'door{second}'].update(image_data=door_goat)
                return second
        else:
            x = random.randint(0, 1)
            if x == 0:
                self.window[f'door{first}'].update(image_data=door_goat)
                return first
            else:
                self.window[f'door{second}'].update(image_data=door_goat)
                return second

    def decision(self, opened, selected, door_values):
        self.window['door1'].update(disabled=True)
        self.window['door2'].update(disabled=True)
        self.window['door3'].update(disabled=True)
        self.window['stay'].update(visible=True)
        self.window['switch'].update(visible=True)
        event, values = self.window.read()
        if event == 'stay':
            if door_values[f'door{selected}'] == 1:
                self.window[f'door{selected}'].update(image_data=door_car)
                self.num_wins += 1
            else:
                self.window[f'door{selected}'].update(image_data=door_goat)
            self.end_game()
        elif event == 'switch':
            self.switch_door(opened, selected, door_values)
            self.end_game()

    def switch_door(self, opened, selected, door_values):
        remaining_door = 6 - opened - selected
        if door_values[f'door{remaining_door}'] == 1:
            self.window[f'door{remaining_door}'].update(image_data=door_car)
            self.num_wins += 1
        else:
            self.window[f'door{remaining_door}'].update(image_data=door_goat)

    def end_game(self):
        self.window['stay'].update(visible=False)
        self.window['switch'].update(visible=False)
        self.window['text_end'].update(value="Game Over")
        self.window['text_games'].update(value="Check results after x games")
        self.window['door1'].update(disabled=True)
        self.window['door2'].update(disabled=True)
        self.window['door3'].update(disabled=True)
        self.window['new_game'].update(visible=True)
        self.window['hundred_games'].update(visible=True)
        self.window['textbox'].update(visible=True)
        event, values = self.window.read()

        if event == 'hundred_games':
            try:
                num_games_to_play = int(values['textbox'])
            except ValueError:
                num_games_to_play = 100
            self.display_results(num_games_to_play)

        self.window['textbox'].update(value="")
        self.window['text_games'].update(value="")
        self.window['hundred_games'].update(visible=False)
        self.window['textbox'].update(visible=False)

    def new_game(self):
        self.opened_door = 0
        self.selected_door = 0
        self.window['text_games'].update(value="")
        self.window['hundred_games'].update(visible=False)
        self.window['textbox'].update(visible=False)
        self.window['stay'].update(visible=False)
        self.window['switch'].update(visible=False)
        self.window['text_end'].update(value="")
        self.window['door1'].update(disabled=False)
        self.window['door2'].update(disabled=False)
        self.window['door3'].update(disabled=False)
        self.window['new_game'].update(visible=False)
        self.window['door1'].update(image_data=door_default)
        self.window['door2'].update(image_data=door_default)
        self.window['door3'].update(image_data=door_default)
        self.window['text'].update(value='Select one of the doors')
        self.window['layout1'].update(visible=True)
        self.window['layout2'].update(visible=False)
        self.run()

    def play_game(self, num_iterations):
        self.stay_wins = []
        self.switch_wins = []

        for _ in range(num_iterations):
            final_choices = []
            doors = ['goat', 'car', 'goat']

            random.shuffle(doors)
            selected_door_index = random.randint(0, 2)
            final_choices.append(doors.pop(selected_door_index))
            doors.remove('goat')
            final_choices.append(doors[0])

            stay = final_choices[0]
            switch = final_choices[1]
            if stay == 'car':
                self.stay_wins.append(True)
            else:
                self.stay_wins.append(False)
            if switch == 'car':
                self.switch_wins.append(True)
            else:
                self.switch_wins.append(False)

    def display_results(self, num_iterations):
        w = 8
        h = 5
        self.play_game(num_iterations)

        games = [i + 1 for i in range(num_iterations)]

        plt.figure(figsize=(w, h))
        plt.plot(games, cumsum(self.switch_wins), color='blue', label='Switch')
        plt.plot(games, cumsum(self.stay_wins), color='red', label='Stay')
        plt.axis([0, num_iterations, 0, num_iterations])

        plt.legend()
        plt.xlabel('Number of Games Played')
        plt.ylabel('Number of Games Won')
        plt.show()

if __name__ == "__main__":
    game = Game()
    game.run()
