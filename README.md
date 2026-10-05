# Controlla

A Python program that lets you remotely control a Windows PC using commands sent through [ntfy](https://ntfy.sh/).

## Features

* Change volume
* Take screenshots
* Show notifications
* Text-to-speech
* Create and edit text files
* Open Chrome and URLs

## Setup

Install the dependencies:

```bash
pip install requests pyautogui pyttsx3 pycaw
```

Change the ntfy topic in `main.py`:

```python
requests.get("https://ntfy.sh/YOUR_TOPIC/json", stream=True)
```

Run:

```bash
python main.py
```

Then send commands to the same ntfy topic.

## Commands

| Command      | Example                    | Description        |
| ------------ | -------------------------- | ------------------ |
| `ping`       | `ping`                     | Check connection   |
| `notify`     | `notify Hello`             | Show notification  |
| `volume`     | `volume 50`                | Set volume         |
| `screenshot` | `screenshot`               | Take screenshot    |
| `say`        | `say Hello`                | Speak text         |
| `txt`        | `txt notes`                | Create a text file |
| `textw`      | `textw notes.txt # Hello`  | Write to a file    |
| `texta`      | `texta notes.txt # Hello`  | Append to a file   |
| `open`       | `open`                     | Open Chrome        |
| `open URL`   | `open https://youtube.com` | Open a URL         |

## Security

Use a long, unpredictable ntfy topic. Anyone who knows the topic can potentially send commands to your computer.

