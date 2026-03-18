import flet as ft
from flet_core import MainAxisAlignment


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2026 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)
        self._txtNmax = ft.TextField(label = "Numero max",
                                     value=self._controller.getNmax(),
                                     disabled = True
                                     )
        self._txtTmax = ft.TextField(label="Numero tentativi max",
                                     value=self._controller.getTmax(),
                                     disabled=True #non ci posso scrivere dentro
                                     )
        self._txtT = ft.TextField(label="Tentativi rimanenti",
                                  value= None,
                                  disabled=True  # non ci posso scrivere dentro
                                     )
        self._row1 = ft.Row(controls=[self._txtNmax, self._txtTmax, self._txtT])

        self._txtInTentativo = ft.TextField(label="Valore")
        self._btnReset = ft.ElevatedButton(text="Nuova partita",
                                           on_click=self._controller.reset) #nome metodo, non chiamata al metodo ( niente "()" )
        self._btnPlay = ft.ElevatedButton(text="Indovina",
                                          on_click=self._controller.play)

        self._row2 = ft.Row(controls=[self._txtInTentativo, self._btnReset, self._btnPlay])

        self._lvOut = ft.ListView(expand = True)

        self._page.add(self._row1, self._row2, self._lvOut)
        self._page.update()

    def setController(self,controller):
        self._controller = controller
        #va a far conoscere a vicenda controller e view

    def update(self):
        self._page.update()