# folding_logic/gadgets.py
from typing import List
from .pleat import Pleat

class Gadget:
    """
    Bloque lógico con entradas y salidas.
    Política para entradas indefinidas (None):
    - Si alguna entrada es None, la salida también será None.
    """
    def __init__(self, name: str, inputs: List[Pleat], outputs: List[Pleat]):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def check_inputs(self, expected: int):
        if len(self.inputs) != expected:
            raise ValueError(f"{self.name} espera {expected} entradas, tiene {len(self.inputs)}")

    def check_outputs(self, expected: int):
        if len(self.outputs) != expected:
            raise ValueError(f"{self.name} espera {expected} salidas, tiene {len(self.outputs)}")

    def evaluate(self):
        raise NotImplementedError

class AND(Gadget):
    def evaluate(self):
        self.check_inputs(2)
        self.check_outputs(1)
        if None in [p.value for p in self.inputs]:
            self.outputs[0].value = None
        else:
            self.outputs[0].value = all(p.value for p in self.inputs)

class OR(Gadget):
    def evaluate(self):
        self.check_inputs(2)
        self.check_outputs(1)
        if None in [p.value for p in self.inputs]:
            self.outputs[0].value = None
        else:
            self.outputs[0].value = any(p.value for p in self.inputs)

class NOT(Gadget):
    def evaluate(self):
        self.check_inputs(1)
        self.check_outputs(1)
        inp = self.inputs[0].value
        self.outputs[0].value = None if inp is None else not inp

class NAND(Gadget):
    def evaluate(self):
        self.check_inputs(2)
        self.check_outputs(1)
        if None in [p.value for p in self.inputs]:
            self.outputs[0].value = None
        else:
            self.outputs[0].value = not all(p.value for p in self.inputs)

class XOR(Gadget):
    """XOR como composición de OR + AND + NOT"""
    def evaluate(self):
        self.check_inputs(2)
        self.check_outputs(1)
        a, b = self.inputs
        if None in [a.value, b.value]:
            self.outputs[0].value = None
        else:
            self.outputs[0].value = (a.value or b.value) and not (a.value and b.value)
