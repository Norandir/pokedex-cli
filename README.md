# Pokedex CLI - Pokémon Search Tool

## Description
A command-line interface (CLI) application that connects to the Pokedex API and allows users to search for Pokémon by name or type. Built for developers, hobbyists, and Pokémon fans who prefer using a lightweight terminal-based interface to explore Pokémon data.

## Features
- Search for a Pokémon by name
- Search for Pokémon by type
- Accepts either type name or menu number for type search
- Case-insensitive input handling
- Easy-to-read printed results in the terminal

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/norandir/pokedex-api-cli.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the CLI:
```bash
python pokemon_cli.py
```

You will be prompted to:
- Search for a Pokémon by **name**  
- Search for Pokémon by **type** (either by entering the number or the type name)

## Tech Stack
- **Python 3**
- **Requests** library for HTTP API calls
- **Standard Library** modules (like `json` and `sys`) for data handling and formatting
