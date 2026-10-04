# Simple Conversational Chatbot using Design Patterns

## Overview

This project is a simple rule-based conversational chatbot developed in Python to demonstrate the practical use of multiple **Object-Oriented Design Patterns**.

The chatbot can respond to basic user inputs, maintain different conversational personalities, and record interactions using a logger.

The project demonstrates the following design patterns:

* **Singleton Design Pattern** – used for shared components such as the Logger and Configuration Manager.
* **Factory Method Pattern** – used to create appropriate response handlers based on user input.
* **Strategy Design Pattern** – used to dynamically change the chatbot's personality, such as Formal or Informal.
* **Logger** – used to record user interactions and chatbot responses.

The main purpose of this project is to understand how design patterns can be applied to organize a small software application in a clean, modular, and maintainable way.

---

## Objectives

The main objectives of this project are to:

* Build a basic conversational chatbot using Python.
* Understand and implement the **Singleton Design Pattern**.
* Understand and implement the **Factory Method Pattern**.
* Understand and implement the **Strategy Design Pattern**.
* Apply Object-Oriented Programming principles in a practical project.
* Maintain conversation logs using a centralized Logger.
* Allow the chatbot's personality to be changed dynamically.
* Create a modular structure that can be extended in the future.

---

## Features

The chatbot provides the following features:

### 1. Basic Conversation

The chatbot can respond to common inputs such as:

* Hello
* Hi
* How are you?
* What is your name?
* Help
* Goodbye

For inputs that are not recognized, the chatbot provides a default response.

### 2. Multiple Personalities

The user can choose the chatbot's conversational personality.

Currently supported personalities are:

* **Formal**
* **Informal**

For example:

**Formal:**

```text
User: Hello

Bot: Good day. How may I assist you?
```

**Informal:**

```text
User: Hello

Bot: Hey! What's up? How can I help?
```

The personality can also be changed during the conversation.

---

## Design Patterns Used

### Singleton Design Pattern

The **Singleton Pattern** ensures that only one instance of a particular class exists throughout the application.

In this project, Singleton is used for shared components such as:

* Logger
* Configuration Manager

This ensures that different parts of the chatbot access the same shared instance.

#### Benefits

* Prevents unnecessary object creation.
* Maintains consistent shared state.
* Provides a single access point to shared resources.
* Makes resource management easier.

---

### Factory Method Pattern

The **Factory Method Pattern** is used to create the appropriate response handler based on the user's input.

Instead of the main chatbot containing a large number of conditional statements for creating different response objects, the Factory handles the creation process.

For example:

```text
User Input
    |
    v
Response Factory
    |
    +---- Greeting Response
    |
    +---- Question Response
    |
    +---- Goodbye Response
    |
    +---- Default Response
```

This makes the chatbot easier to extend with new response types.

---

### Strategy Design Pattern

The **Strategy Pattern** is used to allow the chatbot to change its conversational behavior dynamically.

Different personality strategies are implemented separately.

Currently:

```text
Personality
    |
    +---- Formal Strategy
    |
    +---- Informal Strategy
```

The chatbot can switch between these strategies at runtime without changing its core logic.

This keeps different conversation styles separated and makes it easier to add new personalities in the future.

Possible future personalities could include:

* Professional
* Friendly
* Humorous
* Concise

---

## Logger

The chatbot includes a Logger that records user interactions and chatbot responses.

Example:

```text
[2026-10-04 09:10:02] User: Hello
[2026-10-04 09:10:02] Bot: Good day. How may I assist you?

[2026-10-04 09:10:10] User: How are you?
[2026-10-04 09:10:10] Bot: I am doing well, thank you for asking.
```

The Logger uses the **Singleton Pattern**, ensuring that the application maintains one centralized logging instance.

---

## How the Chatbot Works

The general flow of the application is:

```text
                 User
                  |
                  v
             User Input
                  |
                  v
               Chatbot
                  |
          +-------+-------+
          |               |
          v               v
       Factory         Strategy
          |               |
          v               v
   Response Handler   Personality
          |               |
          +-------+-------+
                  |
                  v
              Response
                  |
                  v
                Logger
              (Singleton)
```

### Example Interaction

```text
Bot: Welcome to the chatbot!
Bot: Choose a personality:
     1. Formal
     2. Informal

User: 2

Bot: Informal personality selected.

User: Hello

Bot: Hey! What's up? How can I help?

User: What is your name?

Bot: I'm your chatbot. Nice to meet you!

User: Bye

Bot: See you later!
```

---

## Project Structure

```text
conversation-chatbot/
│
├── main.py
├── chatbot.py
│
├── singleton.py
├── logger.py
├── config.py
│
├── factory.py
├── responses.py
│
├── strategy.py
├── personalities.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### File Descriptions

| File               | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `main.py`          | Starts and runs the chatbot                  |
| `chatbot.py`       | Contains the main chatbot logic              |
| `singleton.py`     | Provides Singleton functionality             |
| `logger.py`        | Records chatbot interactions                 |
| `config.py`        | Stores application configuration             |
| `factory.py`       | Creates appropriate response handlers        |
| `responses.py`     | Contains different response handlers         |
| `strategy.py`      | Defines the Strategy interface               |
| `personalities.py` | Implements Formal and Informal personalities |
| `requirements.txt` | Contains project dependencies                |
| `.gitignore`       | Specifies files that should not be uploaded  |
| `README.md`        | Project documentation                        |

---

## Technologies Used

* **Python 3**
* Object-Oriented Programming
* Singleton Design Pattern
* Factory Method Pattern
* Strategy Design Pattern
* File-based Logging

The project is intentionally implemented using basic Python features without requiring external AI or Large Language Model APIs.

---

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/dheryagoyal/conversation-chatbot.git
```

### 2. Navigate to the project

```bash
cd conversation-chatbot
```

### 3. Run the chatbot

```bash
python main.py
```

The chatbot will start in the terminal and guide the user through the personality selection and conversation.

---

## Example

```text
====================================
       Conversational Chatbot
====================================

Choose your personality:

1. Formal
2. Informal

Enter your choice: 1

Formal personality selected.

You: hello

Bot: Good day. How may I assist you?

You: how are you?

Bot: I am doing well, thank you for asking.

You: bye

Bot: Goodbye. Have a pleasant day.
```

---

## Why Use Design Patterns?

A simple chatbot can be implemented using only conditional statements. However, as the application grows, putting all the logic into one file can make the code difficult to maintain.

Design patterns help separate different responsibilities.

In this project:

* **Singleton** manages shared resources.
* **Factory Method** manages response object creation.
* **Strategy** manages different chatbot personalities.
* **Logger** records application activity.

This separation makes the project easier to understand, maintain, test, and extend.

---

## Future Improvements

Possible future improvements include:

* Adding more chatbot personalities.
* Adding more response categories.
* Adding conversation history.
* Adding file-based persistent memory.
* Adding a graphical user interface using Tkinter.
* Adding Natural Language Processing.
* Connecting the chatbot to an LLM API.
* Adding unit tests.
* Supporting multiple languages.

---

## Conclusion

This project demonstrates how multiple design patterns can be combined to build a simple but modular conversational chatbot.

The **Singleton Pattern** provides centralized shared resources, the **Factory Method Pattern** manages the creation of response handlers, and the **Strategy Pattern** allows the chatbot's personality to be changed dynamically.

Although the chatbot itself is intentionally simple, the architecture demonstrates how design patterns can improve code organization, maintainability, flexibility, and scalability in larger software applications.
