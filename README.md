# GroupLang-secretary-bot

GroupLang-secretary-bot is a Telegram bot that transcribes voice messages, summarizes the content, and allows users to tip for the service. It uses AWS services for transcription and a custom API for summarization. The bot is designed to be deployed as an AWS Lambda function.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Asynchronous Execution](#asynchronous-execution)
- [API Reference](#api-reference)

## Features

- Transcribe voice messages using AWS Transcribe
- Summarize transcribed text using a custom API
- Allow users to tip for the service
- Secure handling of API keys and tokens
- Deployable as an AWS Lambda function

## Prerequisites

- Poetry for dependency management
- AWS account with Transcribe access
- Telegram Bot Token
- MarketRouter API Key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/GroupLang-secretary-bot.git
   cd GroupLang-secretary-bot
   ```

2. Install Poetry if you haven't already:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Configuration

1. Set up environment variables:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram Bot Token
   - `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID
   - `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Access Key
   - `MARKETROUTER_API_KEY`: Your MarketRouter API Key

2. Configure AWS credentials:
   - Either set up the AWS CLI or use environment variables as mentioned above

## Usage

1. Activate the Poetry virtual environment:
   ```
   poetry shell
   ```

2. Start the bot:
   ```
   uvicorn main:app --reload
   ```

3. In Telegram, start a conversation with the bot or add it to a group

4. Send a voice message to the bot

5. The bot will transcribe the audio, summarize the content, and send the result back

6. Users can tip using the inline button provided with the response

## Asynchronous Execution

The bot now supports asynchronous execution for improved performance. Key methods such as `transcribe_audio` in `services.py` and `send_message` in `utils/telegram_utils.py` have been updated to run asynchronously. This allows for concurrent processing of tasks, reducing overall waiting time and enhancing responsiveness.

### Integration with Async Workflows

To integrate these changes into your workflow, you can use `asyncio.gather` to manage multiple asynchronous tasks effectively. This setup is particularly beneficial when handling multiple audio transcriptions or sending multiple messages simultaneously. Here is a step-by-step guide on how to gather tasks:

1. **Import asyncio**: Ensure you have imported the asyncio module in your script.

2. **Define Async Functions**: Make sure the functions you want to run concurrently are defined as async functions.

3. **Use asyncio.gather**: Use `asyncio.gather` to run multiple async functions concurrently. For example:

   ```python
   import asyncio
   from services import AudioTranscriber
   from utils.telegram_utils import send_message

   async def main():
       transcriber = AudioTranscriber(aws_services)
       tasks = [
           transcriber.transcribe_audio(file_url1),
           transcriber.transcribe_audio(file_url2),
           send_message(chat_id, "Processing your request...")
       ]
       results = await asyncio.gather(*tasks)
       print(results)

   asyncio.run(main())
   ```

4. **Run the Event Loop**: Use `asyncio.run()` to execute the main async function that gathers all tasks.

By following these steps, you can efficiently manage and execute multiple asynchronous tasks, improving the performance and responsiveness of your bot.

### Update Summary

We’ve made important updates to the `README.md` file to reflect recent enhancements in the codebase. Here’s a summary of the changes:

#### Key Enhancements

- **Asynchronous Execution**: The bot now supports asynchronous execution, which improves performance by allowing concurrent processing of tasks. Key methods like `transcribe_audio` in `services.py` and `send_message` in `utils/telegram_utils.py` have been updated accordingly.

#### Integration Guidelines

To efficiently incorporate these improvements into your workflow:

1. **Import the asyncio Module**: Ensure you have imported the asyncio module in your script.
  
2. **Define Async Functions**: Make sure the functions you want to run concurrently are defined as async functions.

3. **Utilize `asyncio.gather`**: This function helps you run multiple async functions at the same time. For example:
   ```python
   import asyncio
   from services import AudioTranscriber
   from utils.telegram_utils import send_message

   async def main():
       transcriber = AudioTranscriber(aws_services)
       tasks = [
           transcriber.transcribe_audio(file_url1),
           transcriber.transcribe_audio(file_url2),
           send_message(chat_id, "Processing your request...")
       ]
       results = await asyncio.gather(*tasks)
       print(results)

   asyncio.run(main())
   ```

4. **Execute with Event Loop**: Use `asyncio.run()` to run the main async function that gathers all tasks.

By following these steps, you can enhance the performance and responsiveness of your bot when managing multiple tasks simultaneously.

## Adding or Updating Dependencies

To add a new package:
```
poetry add package_name
```

To update all packages:
```
poetry update
```

To update a specific package:
```
poetry update package_name
```

## API Reference

The bot uses the following external APIs:

- AWS Transcribe: For audio transcription
- MarketRouter API: For text summarization and reward submission

Refer to the respective documentation for more details on these APIs.
