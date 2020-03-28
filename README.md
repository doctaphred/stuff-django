# stuff-django

A Django-based implementation of [`stuff`](https://github.com/doctaphred/stuff).

## Setup

To install the project, along with all development requirements, and run a full build:

1. Clone the repo.
2. Run `make`.

Before running the project itself, in your shell:

3. Export the `DJANGO_SECRET_KEY` environment variable.
4. Activate the virtualenv (`source venv/bin/activate`).


### Make

The Makefile's default action runs pytest and flake8. Those actions depend on the existence of the `venv` directory: if it does not already exist, Make first uses `python3 -m venv` to create it, then installs the development requirements.

All actions in the Makefile directly reference the executables in `venv/bin/`, so there's no need to activate the virtualenv before running Make actions. Run `make` again for a full build, `make test` to just run pytest, or `make lint` to just run flake8.

If you delete the virtualenv, the next `make` command you run will recreate it and reinstall the development requirements before proceeding.

This Makefile is just a convenience, and is not required to develop this project: feel free to run its setup/test/lint actions manually, or use other tools like `virtualenvwrapper` if you prefer.


### Environment variables

Django depends heavily on the value of `settings.SECRET_KEY`. Instead of hard-coding a value in the default settings module and overriding it in a separate production settings module, this project pulls the value from the `DJANGO_SECRET_KEY` environment variable. Run `scripts/generate-secret-key` to generate an appropriate secure value.

For development, the most basic way to set environment variables is to run, e.g., `export DJANGO_SECRET_KEY=hunter2` in your shell before running the project. Don't do this, though, since your shell will probably log that line in its history file.

Instead, consider creating a new file in the project directory, adding the `export` directives, and sourcing that file before running the project.

To avoid accidentally committing this file, you should add it to the project's `.git/info/exclude` or your global `~/.config/git/ignore`, or choose a name already included in the project's `.gitignore`, such as `.env`.

Consider using [direnv](https://direnv.net/) to automatically source this file (and activate the virtualenv!) whenever you `cd` into the project directory. (tl;dr: install direnv, add its hook to your shell profile, and add `.envrc` to `~/.config/git/ignore`; then create a file named `.envrc` in this directory, and add the `export` directives, along with `source venv/bin/activate`; then run `direnv allow`.)
