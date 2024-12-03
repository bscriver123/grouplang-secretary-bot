# GroupLang-secretary-bot

GroupLang-secretary-bot es un bot de Telegram que transcribe mensajes de voz, resume el contenido y permite a los usuarios dar propinas por el servicio. Utiliza servicios de AWS para la transcripción y una API personalizada para la resumir. El bot está diseñado para ser desplegado como una función de AWS Lambda.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Despliegue](#despliegue)
- [Referencia de API](#referencia-de-api)

## Características

- Transcribir mensajes de voz usando AWS Transcribe
- Resumir texto transcrito usando una API personalizada
- Permitir a los usuarios dar propinas por el servicio
- Manejo seguro de claves API y tokens
- Desplegable como una función de AWS Lambda

## Requisitos Previos

- Poetry para la gestión de dependencias
- Cuenta de AWS con acceso a Transcribe
- Token de Bot de Telegram
- Clave API de MarketRouter

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/yourusername/GroupLang-secretary-bot.git
   cd GroupLang-secretary-bot
   ```

2. Instala Poetry si no lo has hecho ya:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Instala las dependencias usando Poetry:
   ```
   poetry install
   ```

## Configuración

1. Configura las variables de entorno:
   - `TELEGRAM_BOT_TOKEN`: Tu Token de Bot de Telegram
   - `AWS_ACCESS_KEY_ID`: Tu ID de Clave de Acceso de AWS
   - `AWS_SECRET_ACCESS_KEY`: Tu Clave de Acceso Secreta de AWS
   - `MARKETROUTER_API_KEY`: Tu Clave API de MarketRouter

2. Configura las credenciales de AWS:
   - Configura el CLI de AWS o usa las variables de entorno mencionadas arriba

## Uso

1. Activa el entorno virtual de Poetry:
   ```
   poetry shell
   ```

2. Inicia el bot:
   ```
   uvicorn main:app --reload
   ```

3. En Telegram, inicia una conversación con el bot o añádelo a un grupo

4. Envía un mensaje de voz al bot

5. El bot transcribirá el audio, resumirá el contenido y enviará el resultado de vuelta

6. Los usuarios pueden dar propinas usando el botón en línea proporcionado con la respuesta

## Añadir o Actualizar Dependencias

Para añadir un nuevo paquete:
```
poetry add nombre_del_paquete
```

Para actualizar todos los paquetes:
```
poetry update
```

Para actualizar un paquete específico:
```
poetry update nombre_del_paquete
```

## Referencia de API

El bot utiliza las siguientes APIs externas:

- AWS Transcribe: Para la transcripción de audio
- API de MarketRouter: Para la resumir de texto y envío de recompensas

Consulta la documentación respectiva para más detalles sobre estas APIs.
