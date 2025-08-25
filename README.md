# Calculadora de Tempo

Una aplicación sencilla en **Python** para calcular subdivisiones de tempo en milisegundos a partir de un **BPM**. También incluye una función de **Tap Tempo** para medir el BPM manualmente.

---

## Características

- Ingresa un BPM y calcula automáticamente los tiempos de:
  - Blanca (1/2)
  - Negra (1/4)
  - Corchea (1/8)
  - Semicorchea (1/16)
  - Fusa (1/32)
  - SemiFusa (1/64)
  - Gígica (1/128)
- **Tap Tempo**: pulsa la barra espaciadora o el botón para medir el BPM.
- Limpiar la tabla con la tecla **Escape**.
- Permite BPM con valores enteros y decimales.
- Valida que el BPM ingresado sea positivo.

---

## Requisitos

- Python 3.x
- Tkinter (normalmente viene incluido con Python)

---

## Uso

1. Clona este repositorio:

```bash
git clone https://github.com/Ignacioctoro/CalculadoraTempo.git
