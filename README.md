# Python Client/Server Network Application

## Overview

This project is a Python-based client/server network infrastructure that supports communication between a client and a central server. The application supports data transmission in multiple formats (binary, JSON, XML), serialization/deserialization of data structures, encryption of transmitted data, and text file transmission.

## Features

- Client/server communication using Python's socket library
- Data transmission in binary, JSON, and XML formats
- Encryption of transmitted data
- Graphical user interface (GUI) for client interactions
- Logging and configurable server options

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd network_app
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the server:

    ```bash
    python server/server.py
    ```

2. Start the client:

    ```bash
    python client/client.py
    ```

3. Use the GUI to select a file, choose the transmission type, and send the file to the server.

## Configuration

The server can be configured using the `server/config.py` file. Logging options can be customized in `server/logger.py`.

## Running Tests

To run the unit tests:

```bash
pytest tests/
```
