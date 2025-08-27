import json
import os

from logic.pleat import Pleat
from logic.gadgets import AND, OR, NOT, NAND, XOR
from logic.network import Network

# Mapeo de tipos a clases de gadgets
OPERATORS = {
    "AND": AND,
    "OR": OR,
    "NOT": NOT,
    "NAND": NAND,
    "XOR": XOR,
}

def run_circuit_from_json(path: str):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, path)

    with open(full_path, "r") as f:
        circuit = json.load(f)

    # Crear pleats
    pleats = {p["name"]: Pleat(p["name"]) for p in circuit["pleats"]}

    # Crear red
    net = Network()

    # Agregar pleats a la red
    for pl in pleats.values():
        net.add_pleat(pl)

    # Crear gadgets y agregarlos a la red
    for g in circuit["gadgets"]:
        cls = OPERATORS[g["type"]]
        ins = [pleats[i] for i in g["inputs"]]
        outs = [pleats[o] for o in g["outputs"]]
        gadget = cls(name=g["id"], inputs=ins, outputs=outs)
        net.add_gadget(gadget)

    # Fijar entradas
    net.set_inputs(circuit["inputs"])

    # Ejecutar la red
    results = net.run()

    # Recoger solo los outputs solicitados
    return {o: results[o] for o in circuit["outputs"]}


if __name__ == "__main__":
    result = run_circuit_from_json("prueba.json")
    print("Resultado:", result)
