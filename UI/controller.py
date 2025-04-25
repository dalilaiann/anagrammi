import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def calcola_anagrammi(self, e):
        if self._view.txt_word.value=="":
            self._view.create_alert("Inserisci una parola")
        else:
            corrette, sbagliate=self._model.calcola_anagrammi(self._view.txt_word.value)

            if len(corrette)>0:
                self._view.lst_correct.controls.clear()
                for c in corrette:
                    self._view.lst_correct.controls.append(ft.Text(c))
                    self._view.update_page()

            if len(sbagliate)>0:
                self._view.lst_wrong.controls.clear()
                for c in sbagliate:
                    self._view.lst_wrong.controls.append(ft.Text(c))
                    self._view.update_page()


    def reset(self, e):
        self._view.txt_word.value=""
        self._view.lst_correct.controls.clear()
        self._view.lst_wrong.controls.clear()
        self._view.update_page()

