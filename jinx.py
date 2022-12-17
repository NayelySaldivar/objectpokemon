# -*- coding: utf-8 -*-
"""Jinx.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_-KKjjtglVvXALk3fKhZd_JREPoQVko6
"""

from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(30)
        self.spend_attack(30)
        self.spend_defence(40)
        self.add_move(Latigo_moco())
        self.add_move(Da_la_patita())
        self.add_move(Ronquido())
        self.add_move(Mirada_intimidante())
        self.set_type(Type.EARTH)
        self.move = 0
        self.moves = ['Latigo_moco', "Ronquido", "Mirada_intimidante", "Da_la_patita"]

    def get_name(self):
        return "Jinx"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Mirada_intimidante(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Mirada Intimidante"

class Latigo_moco(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Látigo moco"

class Ronquido(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Ronquido"


class Da_la_patita(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Da la patita"