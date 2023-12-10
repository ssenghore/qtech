from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
import requests

################################### THE APP ITSELF'S##########################################
Window.clearcolor=(150/255,75/255,0,1)
Config.set('kivy','window_icon','QUATECH.png')
class nestApp(GridLayout):
    def __init__(self, **kwargs):
        super(nestApp,self).__init__(**kwargs)
        self.cols=3
        self.row_force_default=True
        self.row_default_height=40
        self.add_widget(Label(text='Enter The Ip adress', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.ip_input=TextInput()
        self.add_widget(self.ip_input)
        self.entrbutton=Button(text='Enter',font_size='20sp', bold=True,color=(0,0,0,1),size_hint=(0.25,0.25))
        self.add_widget(self.entrbutton)
        self.add_widget(Label(text='Relay ONE', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay1ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.oneonButton)
        self.add_widget(self.relay1ON)
        self.relay1OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.oneoffButton)
        self.add_widget(self.relay1OFF)
        self.add_widget(Label(text='Relay TWO', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay2ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.twoonButton)
        self.add_widget(self.relay2ON)
        self.relay2OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.twooffButton)
        self.add_widget(self.relay2OFF)
        self.add_widget(Label(text='Relay THREE', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay3ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.threeonButton)
        self.add_widget(self.relay3ON)
        self.relay3OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.threeoffButton)
        self.add_widget(self.relay3OFF)
        self.add_widget(Label(text='Relay FOUR', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay4ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.fouronButton)
        self.add_widget(self.relay4ON)
        self.relay4OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.fouroffButton)
        self.add_widget(self.relay4OFF)
        self.add_widget(Label(text='Relay FIVE', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay5ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.fiveonButton)
        self.add_widget(self.relay5ON)
        self.relay5OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.fiveoffButton)
        self.add_widget(self.relay5OFF)
        self.add_widget(Label(text='Relay SIX', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay6ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.sixonButton)
        self.add_widget(self.relay6ON)
        self.relay6OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.sixoffButton)
        self.add_widget(self.relay6OFF)
        self.add_widget(Label(text='Relay SEVEN', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay7ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.sevenonButton)
        self.add_widget(self.relay7ON)
        self.relay7OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.sevenoffButton)
        self.add_widget(self.relay7OFF)
        self.add_widget(Label(text='Relay EIGHT', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay8ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.eightonButton)
        self.add_widget(self.relay8ON)
        self.relay8OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.eightoffButton)
        self.add_widget(self.relay8OFF)
        self.add_widget(Label(text='Relay NINE', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay9ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.nineonButton)
        self.add_widget(self.relay9ON)
        self.relay9OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.nineoffButton)
        self.add_widget(self.relay9OFF)
        self.add_widget(Label(text='Relay TEN', font_size='20sp', bold=True,color=(0,0,0,1)))
        self.relay10ON=Button(text='ON',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(0,1,0,1),on_press=self.tenonButton)
        self.add_widget(self.relay10ON)
        self.relay10OFF=Button(text='OFF',font_size='20sp', bold=True,color=(0,0,0,1),
                           background_color=(1,0,0,1),on_press=self.tenoffButton)
        self.add_widget(self.relay10OFF)
#################################### BUTTON'S FUNCTIONS################################
    def send_command(self, command):
        ip_address = self.ip_input.text
        if not ip_address:
            print("Please enter the NodeMCU IP address.")
            return

        url = f"http://{ip_address}/{command}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Command '{command}' sent successfully to NodeMCU at {ip_address}")
            else:
                print(f"Failed to send command '{command}' to NodeMCU. Response: {response.text}")
        except requests.RequestException as e:
            print(f"Error: {e}")
    def oneonButton(self,obj):
        print('button 1on have been press')
        self.send_command("Relay1ON")
    def oneoffButton(self,obj):
        print('button 1off have been press')
        self.send_command("Relay1OFF")
    def twoonButton(self,obj):
        print('button 2on have been press')
        self.send_command("Relay2ON")
    def twooffButton(self,obj):
        print('button 2off have been press')
        self.send_command("Relay2OFF")
    def threeonButton(self,obj):
        print('button 3on have been press')
        self.send_command("Relay3ON")
    def threeoffButton(self,obj):
        print('button 3off have been press')
        self.send_command("Relay3OFF")
    def fouronButton(self,obj):
        print('button 4on have been press')
        self.send_command("Relay4ON")
    def fouroffButton(self,obj):
        print('button 4off have been press')
        self.send_command("Relay4OFF")
    def fiveonButton(self,obj):
        print('button 5on have been press')
        self.send_command("Relay5ON")
    def fiveoffButton(self,obj):
        print('button 5off have been press')
        self.send_command("Relay5OFF")
    def sixonButton(self,obj):
        print('button 6on have been press')
        self.send_command("Relay6ON")
    def sixoffButton(self,obj):
        print('button 60ff have been press')
        self.send_command("Relay6OFF")
    def sevenonButton(self,obj):
        print('button 7on have been press')
        self.send_command("Relay7ON")
    def sevenoffButton(self,obj):
        print('button 70ff have been press')
        self.send_command("Relay7OFF")
    def eightonButton(self,obj):
        print('button 8on have been press')
        self.send_command("Relay8ON")
    def eightoffButton(self,obj):
        print('button 80ff have been press')
        self.send_command("Relay8OFF")
    def nineonButton(self,obj):
        print('button 9on have been press')
        self.send_command("Relay9ON")
    def nineoffButton(self,obj):
        print('button 90ff have been press')
        self.send_command("Relay9OFF")
    def tenonButton(self,obj):
        print('button 10on have been press')
        self.send_command("Relay10ON")
    def tenoffButton(self,obj):
        print('button 100ff have been press')
        self.send_command("Relay10OFF")
class MainApp(App):
    def build(self):
        return nestApp()

app=MainApp()
app.run ()