# Contributing to life-automation

Thanks for your interest in contributing! This repository is a collection of small Python automations
(currently a Telegram bot and a Greek nameday reminder) that are meant to be composed together from `main.py`.

## Project Architecture

```text
life-automation/
├── main.py                  # Entry point that wires the modules together
├── feature1/
│   ├── __init__.py
│   ├── feature.py           # the feature you want to add
│   ├── .example.env         # Template secret keys
│   └── .env                 # Your local secrets (git-ignored)
├── feature2/
│   ├── __init__.py
│   ├── feature.py           # the feature you want to add
│   ├── .example.env         # Template secret keys
│   └── .env                 # Your local secrets (git-ignored)
├── CONTRIBUTING.md
├── LICENSE                  # MIT
└── README.md
```

Each automation lives in its own top-level package and owns its own configuration (`.env`).
Modules should stay independent of each other; composition happens in `main.py`.

## Getting started

### Prerequisites

- Python 3.11 or newer
- `pip`

### Setup

1. Fork and clone the repository:

   ```bash
   git clone https://github.com/<your-username>/life-automation.git
   cd life-automation
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variables. Copy each `.example.env` to `.env` in the same folder and fill in your values:

   ```bash
   cp feature1/.example.env feature/.env
   ```

   | Module             | Variable    | Description                                      |
   |--------------------|-------------|--------------------------------------------------|
   | `telegram_bot`     | `BOT_TOKEN` | Token from [@BotFather](https://t.me/BotFather)  |
   | `telegram_bot`     | `CHAT_ID_1` | Telegram chat ID that will receive messages      |
   | `nameday_reminder` | `API_KEY`   | Your RapidAPI key                                |
   | `nameday_reminder` | `API_HOST`  | `greek-eortologio.p.rapidapi.com`                |

   **Never commit a `.env` file.** They are git-ignored; keep it that way.

### Running

Run everything from the repository root so the packages are importable.

Full run (fetches today's namedays and sends them to Telegram):

```bash
python main.py
```

Each package can also be run standalone for a quick smoke test:

```bash
python -m telegram_bot           # sends "Hello from the Telegram Bot!"
python -m nameday_reminder       # prints today's nameday reminder (no Telegram needed)
```

> Use `python -m <package>`, not `python <package>/<file>.py` – running a file directly breaks the
> package's relative imports.

## How to contribute

### Reporting bugs and suggesting features

Open a GitHub issue. Include:

- what you expected to happen and what actually happened,
- steps to reproduce (for bugs),
- your Python version and OS.

### Submitting changes

1. Create a branch from `main`. Use the `feature/<short-name>` convention already used in this repo
   (e.g. `feature/telegramBot`, `feature/nameday-reminder`). For fixes use `fix/<short-name>`.
2. Make your changes, keeping them focused on a single topic.
3. Run the affected module(s) locally to verify they still work.
4. Commit using the [Conventional Commits](https://www.conventionalcommits.org/) style:

   ```text
   feat: add weather reminder module
   fix: handle non-200 responses from the nameday API
   docs: update setup instructions
   refactor: extract request helper
   ```

5. Push your branch and open a pull request against `main`. Describe *what* changed and *why*.

### Adding a new automation

Follow the package conventions above. For a package called `my_automation`:

1. Create the directory and its files:

   ```text
   my_automation/
   ├── __init__.py
   ├── __main__.py
   ├── core.py          # or whatever name fits – the implementation
   └── .example.env     # only if it needs configuration
   ```

2. Implement the logic in the internal module(s) and expose the public API from `__init__.py`:

   ```python
   # my_automation/__init__.py
   from .core import MyAutomation

   __all__ = ["MyAutomation"]
   ```

3. Add a `__main__.py` so it can be smoke-tested with `python -m my_automation`:

   ```python
   # my_automation/__main__.py
   from . import MyAutomation

   print(MyAutomation().run())
   ```

4. If it needs secrets, add a `.example.env` with placeholder values and load the real `.env` with an explicit
   path (see the package conventions). Never commit the `.env` itself.
5. Wire it into `main.py` if it should be part of the combined run, importing from the package root.
6. Update the project structure section above and the `README.md`.

## Code style

- Follow [PEP 8](https://peps.python.org/pep-0008/) and use 4-space indentation.
- Use type hints on function signatures, as the existing code does.
- Import from package roots (`from telegram_bot import TelegramBot`); inside a package use relative imports.
- Avoid mutable default arguments and avoid calling `os.getenv` in a default argument – resolve
  configuration inside the function/constructor body instead.
- Read configuration from environment variables via `os.getenv`; do not hard-code tokens or keys.
- Handle network errors gracefully (catch exceptions, check `status_code`) rather than letting the script crash.
- Keep third-party dependencies minimal. If you add one, mention it in your PR so it can be documented in the setup steps.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
