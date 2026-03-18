from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNmax(self):
        return self._model.Nmax

    def getTmax(self):
        return self._model.Tmax

    def getT(self):
        return self._model.T

    def reset(self, e):
        self._model.reset() #resetto stato del gioco lato modello!
        self._view._txtT.value=self._model.T
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text("Inizia il gioco! Indovina a che numero sto pensando.")
        )
        self._view.update() #ho cambiato qualcosa, aggiornati!

    def play(self, e):
        tentativoStr = self._view._txtInTentativo.value
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Errore, devi inserire un valore numerico"))
            self._view.update()
            return

        self._model.play(tentativo)

        res = self._model.play(tentativo)
        if res == 0:
            """Ho vinto"""
            self._view._lvOut.controls.append(
                ft.Text(f"Bravo, hai vinto il valore corretto era {tentativo}",
                        color="green")
            )
            self._view.update()
            return

        elif res == 2:
            self._view._lvOut.controls.append(
                ft.Text(f"Hai perso, il valore corretta era {self._model.segreto}.",
                        color="red")
            )
            self._view.update()
            return

        elif res == -1:
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta, il segreto è più piccolo di  {tentativo}.")
            )
            self._view.update()
            return
        else:
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta, il segreto è più grande di  {tentativo}.")
            )
            self._view.update()
            return

