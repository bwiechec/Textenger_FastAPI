# TextengerBackend

## Description

TextengerBackend is a backend server for the Textenger application. It provides the necessary APIs and functionalities to support the Textenger frontend.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

To install and run the TextengerBackend server, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/TextengerBackend.git
   ```

2. Install the dependencies:

   ```shell
   cd TextengerBackend
   TODO
   ```

3. Set up the environment variables:

   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables to the `.env` file:

     ```plaintext
     TODO
     ```

     Note: Adjust the values of `PORT` and `DATABASE_URL` as per your requirements.

4. Start the server:

   ```shell
   uvicorn main:app --reload
   ```

## Usage

Once the server is up and running, you can use the following APIs:

- `/api/users`: This API allows you to manage users.
- `/api/messages`: This API allows you to manage messages.
- `/api/threads`: This API allows you to manage threads.
- `/redoc`: Redoc documentation for API.
- `/docs`: Docs allowing you to test API.

Make sure to authenticate your requests with the appropriate headers.

## Features

- User management: Create, update, and delete users.
- Message management: Send and receive messages between users.
- Thread management: Create, update, and delete threads.
- Error handling: Proper error handling and response messages.
