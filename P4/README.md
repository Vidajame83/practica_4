# Ingreso laboral y brecha de género en Ecuador (ENEMDU sintética)

## Pregunta de análisis
# ¿Qué factores se asocian con el ingreso laboral en Ecuador y la brecha entre hombres y mujeres se 
# mantiene al comparar personas con la misma educación, zona y región?

## Fuente de datos
# Encuesta ENEMDU **simplificada y sintética**, generada con la función `generar_enemdu()` 
# (semilla 2026) e inspirada en la estructura de la Encuesta Nacional de Empleo, Desempleo
# y Subempleo del INEC. Los valores son simulados: **no son datos oficiales**. 
# 4.000 personas y 11 variables (provincia, región, área, sexo, edad, años de educación, horas de trabajo, 
# ingreso, empleo adecuado y nivel de instrucción).

## Cómo ejecutar
1. Clonar el repositorio:
   `git clone https://github.com/USUARIO/REPO.git`
2. Instalar las dependencias:
   `pip install -r requirements.txt`
3. Colocar el archivo crudo en `data/crudos/enemdu.csv` (no se incluye en el repositorio).
4. Ejecutar los notebooks de la carpeta `notebooks/` en orden.

## Estructura
```
P4/
├── data/
│   ├── crudos/        # datos originales (excluidos de Git)
│   └── procesados/    # datos limpios generados por src/limpieza.py
├── notebooks/         # análisis exploratorio y modelos
├── src/
│   └── limpieza.py    # funciones limpiar(), agregar_variables(), anonimizar()
├── reportes/          # gráficos y resultados
├── requirements.txt   # versiones exactas de las librerías
└── README.md
```
