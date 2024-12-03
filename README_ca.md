# GroupLang-secretary-bot

GroupLang-secretary-bot és un bot de Telegram que transcriu missatges de veu, resumeix el contingut i permet als usuaris donar propines pel servei. Utilitza serveis d'AWS per a la transcripció i una API personalitzada per a resumir. El bot està dissenyat per ser desplegat com una funció d'AWS Lambda.

## Taula de Continguts

- [Característiques](#característiques)
- [Requisits Previs](#requisits-previs)
- [Instal·lació](#instal·lació)
- [Configuració](#configuració)
- [Ús](#ús)
- [Desplegament](#desplegament)
- [Referència de l'API](#referència-de-lapi)

## Característiques

- Transcriure missatges de veu utilitzant AWS Transcribe
- Resumir text transcrit utilitzant una API personalitzada
- Permetre als usuaris donar propines pel servei
- Gestió segura de claus API i tokens
- Desplegable com una funció d'AWS Lambda

## Requisits Previs

- Poetry per a la gestió de dependències
- Compte d'AWS amb accés a Transcribe
- Token de Bot de Telegram
- Clau API de MarketRouter

## Instal·lació

1. Clona el repositori:
   ```
   git clone https://github.com/yourusername/GroupLang-secretary-bot.git
   cd GroupLang-secretary-bot
   ```

2. Instal·la Poetry si no ho has fet ja:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Instal·la les dependències utilitzant Poetry:
   ```
   poetry install
   ```

## Configuració

1. Configura les variables d'entorn:
   - `TELEGRAM_BOT_TOKEN`: El teu Token de Bot de Telegram
   - `AWS_ACCESS_KEY_ID`: El teu ID de Clau d'Accés d'AWS
   - `AWS_SECRET_ACCESS_KEY`: La teva Clau d'Accés Secreta d'AWS
   - `MARKETROUTER_API_KEY`: La teva Clau API de MarketRouter

2. Configura les credencials d'AWS:
   - Configura el CLI d'AWS o utilitza les variables d'entorn esmentades anteriorment

## Ús

1. Activa l'entorn virtual de Poetry:
   ```
   poetry shell
   ```

2. Inicia el bot:
   ```
   uvicorn main:app --reload
   ```

3. A Telegram, inicia una conversa amb el bot o afegeix-lo a un grup

4. Envia un missatge de veu al bot

5. El bot transcriurà l'àudio, resumirà el contingut i enviarà el resultat de tornada

6. Els usuaris poden donar propines utilitzant el botó en línia proporcionat amb la resposta

## Afegir o Actualitzar Dependències

Per afegir un nou paquet:
```
poetry add nom_del_paquet
```

Per actualitzar tots els paquets:
```
poetry update
```

Per actualitzar un paquet específic:
```
poetry update nom_del_paquet
```

## Referència de l'API

El bot utilitza les següents APIs externes:

- AWS Transcribe: Per a la transcripció d'àudio
- API de MarketRouter: Per a resumir text i enviament de recompenses

Consulta la documentació respectiva per a més detalls sobre aquestes APIs.
