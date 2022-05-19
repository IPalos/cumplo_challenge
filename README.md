# README

## Desafío realizado por **Ignacio Palos** para Cumplo para la posición de Desarrollador Python

Este documento contiene la información necesaria para navegar  y entender el código de este proyecto además de contar con una pequeña guia de instalación  si se descarga el código fuente

## Arquitectura del proyecto

### Stack
- Lenguaje: Python 3.6.13
- Frameworks:
	- Flask : 2.0.3
	- Plotly Dash: 2.4.1
- DB: MySQL 8.0.21
- Pandas 1.1.5

### Estructura
**assets**: Contiene los estilos CSS que se usan en el proyecto

**components**: Contiene los componentes individuales a integrar a la página principal

**data**: Contiene un archivo básico con una llamada a la base de datos para probar conexión

**utils**: Contiene constantes globales y las llamadas a la API de Banxico

**app.py**: Archivo principal del proyecto

**requirements.txt**: Archivo con las dependencias necesarias para ejecutar el proyecto

## "Getting Started"

### Descargar proyecto
En esta guia supondré que ya tienen Git instalado

Para descargar el proyecto ejecute el siguiente comando

```
git clone https://github.com/IPalos/cumplo_challenge.git
```

### Cargar ambiente virtual

```
cd cumplo_challenge
conda create -n cumplo python=3.6
```

Cuando termine de crear el ambiente virtual:
```
conda activate cumplo
```

### Instalar dependencias

```
pip install requirements.txt
```

### Ejecutar programa
```
Linux: python3 app.py
Windows: python app.py
```
