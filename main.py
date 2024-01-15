from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from plyer import notification

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDRaisedButton:
        text: "Mostrar Notificación Persistente"
        pos_hint: {'center_x': 0.5}
        on_press: app.show_notification()
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_notification(self):
        notification.notify(
            title='Ser el mejor',
            message='Dios te esta mirando, sorprendelo',
            app_name='Recordador',
            timeout=0  # Establece el tiempo en cero para que sea persistente
        )


if __name__ == '__main__':
    MyApp().run()

# title='Ser el mejor',
#             message='Dios te esta mirando, sorprendelo',
#             app_name='Recordador',
