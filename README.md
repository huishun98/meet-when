# Meet When
Meet When ([@meetwhen_telebot](https://t.me/meetwhen_telebot)) is a Telegram bot that create polls for meetups. :sparkles:

## Prerequisites
1. Telegram bot created with [@botfather](https://telegram.me/botfather)

## Running locally
1. Configure environment variables. See [config.py](./config.py) for the required environment variables.

2. Install Python and pip and set up virtual environment. 
   ```
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Start services. Run `python app.py` to start the telegram bot.

## Running in production
1. Configure environment variables. See [config.py](./config.py) for the required environment variables.
   * Remember to set the ENV environment variable to any value of your choice (e.g. `dev`, `uat`, `prod`)
2. Entrypoint is `gunicorn app:app`.

## Contributing
If you're looking for a way to contribute, you can scan through our existing issues for something to work on. See [the contributing guide](./CONTRIBUTING.md) for detailed instructions on how to get started with our project.

## License
The project is licensed under a [GNU GENERAL PUBLIC LICENSE license](./LICENSE).
