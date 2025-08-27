# Origami

Un modelo de cómputo por pliegues en Python, orientado a la construcción de circuitos lógicos y simulación de gadgets básicos (AND, OR, NOT, NAND, XOR).

## Instalación

Clona el repositorio y crea un entorno virtual:

```bash
git clone https://github.com/tuusuario/Origami.git
cd Origami
python -m venv venv
source venv/bin/activate  # en Linux/macOS
venv\Scripts\activate     # en Windows
pip install -r requirements.txt
```

## Uso

Ejemplo: medio sumador (half adder):

```bash
python examples.half_adder_example
```

Ejemplo con circuito definido en JSON:

```bash
python -m pytest -v
```

## Tests

El proyecto usa `pytest`:

```bash
pytest -v
```

## 📂 Estructura

```
Origami/
├── examples/        # Ejemplos de uso
├── tests/           # Pruebas unitarias
├── origami/         # Código fuente principal
├── README.md        # Documentación principal
├── requirements.txt # Dependencias
└── LICENSE          # Licencia
```

