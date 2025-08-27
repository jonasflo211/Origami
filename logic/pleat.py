from typing import Optional

class Pleat:
    """Representa una 'tira' de papel con señal booleana o indefinida (None)"""
    def __init__(self, name: str, value: Optional[bool] = None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}:{self.value}"
