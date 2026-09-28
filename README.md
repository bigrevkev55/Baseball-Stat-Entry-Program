# Baseball Stat Entry Program

A collection of Python and SQL tools for entering, storing, and reporting baseball statistics for tabletop baseball projects.

This repository contains two versions of the program:

## 1. StatProgram2

`StatProgram2` is the current version of the application.

It is a Python desktop application built with Tkinter and SQLite. The program stores its data in the portable `stratbb.db` database file and provides a main menu for:

- Creating and maintaining player records
- Creating game records
- Entering player statistics for individual games
- Initializing the SQLite database and its tables and reporting views

Start the application with:

```text
python StatProgram2/main.py
```

The current application is designed to run locally without requiring a separate SQL Server database.

## 2. StatProgramAlpha1

`StatProgramAlpha1` is the original version of the program and is kept for reference, historical comparison, and access to the original database scripts.

It contains Python/Tkinter data-entry forms that connect to Microsoft SQL Server through `pyodbc`:

- Player creation
- Game creation
- Player game-stat entry

It also contains:

- `StratBBDB.sql`, the original SQL Server database setup script
- SQL queries for player IDs, batting and pitching statistics, box scores, and project reports
- Images and application assets

The Alpha version expects a locally configured SQL Server database named `StratBB` and a matching ODBC connection. It is not as portable as `StatProgram2`.

## Recommended Version

Use `StatProgram2` for new development and normal use. Use `StatProgramAlpha1` when reviewing the original SQL Server implementation, database design, or older reporting queries.

## Requirements

For `StatProgram2`:

- Python 3
- Tkinter, normally included with standard Python installations

For `StatProgramAlpha1`:

- Python 3
- Tkinter
- `pyodbc`
- `Pillow`
- Microsoft SQL Server with a `StratBB` database
- A configured SQL Server ODBC driver

## Repository Notes

The following local/generated content is excluded from Git:

- The Copilot sharing directory under `StatProgramAlpha1`
- Python `__pycache__` directories
- Python `.pyc` files

The SQLite database file is currently included with `StatProgram2` so the existing project data can be retained.

## Project Status

`StatProgram2` is an active work in progress. Planned improvements include additional reports, live game scoring, improved user-facing error messages, and expanded game-result fields.
