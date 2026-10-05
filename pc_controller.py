import requests, json, pyautogui, pyttsx3, subprocess
import tkinter as tk
from tkinter import messagebox
from pycaw.pycaw import AudioUtilities
from pathlib import Path

# ping
def ping():
    print("Online")

# Notify
def notify(msg):
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo(title=None, message=msg)

# Volume adjuster
def volume(percentage):
    if not percentage.isdigit():
        print(f"Must be int, not {percentage}")
    percentage = int(percentage)
    if percentage > 100 or percentage < 0 :
        print("Volume must be between 0-100")
    else:
        device = AudioUtilities.GetSpeakers()
        volume_control = device.EndpointVolume
        # Pycaw works with a scalar value between 0.0 and 1.0
        level = percentage / 100.0
        volume_control.SetMasterVolumeLevelScalar(level, None)
        print("Successfully adjusted to {percentage}%")

# Take screen
def screenshot():
    pyautogui.hotkey('win','printscreen')
    print("Screenshot Done")

# Make it speak
def say(msg):
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()
    print(f"Saying {msg}")

# Creates new file
def txt(name):
    file_name = name + ".txt"
    with open(file_name, 'w', encoding='UTF-8') as file:
        pass
    print(f"Create file {name}")

# Writes existing file
def textw(file, note):
    p = Path.cwd() / file
    if p.exists():
        with open(p, "w", encoding="UTF-8") as file:
            file.write(note)
        print("Sucessful write.")
    else:
        print("File not found")

# Appends to an exisitng fike
def texta(file, note):
    p = Path.cwd() / file
    if p.exists():
        with open(p, "a", encoding="UTF-8") as file:
            file.write(" " + note)
        print("Sucessful append.")
    else:
        print("File not found")

# Open Chrome and any link
def open_app(link=None):
    if link is None:
        subprocess.run(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
        print("opened sucessfully")
    else:
        subprocess.run(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', link])
        print("link opened")

# main function
def main():
    print("Controlla")
    try:
        resp = requests.get("https://ntfy.sh/topic_name/json", stream=True)
        for line in resp.iter_lines():
          if line:
             event_data = json.loads(line.decode("utf-8"))
             if event_data.get("event") == "message":
                if event_data.get("message").lower() == "ping":
                    ping()
                elif event_data.get("message")[0:6].lower() == "notify":
                    notify(event_data.get("message")[7:].strip())
                elif event_data.get("message")[0:6].lower() == "volume":
                    volume(event_data.get("message")[7:].strip())
                elif event_data.get("message")[0:10].lower() == "screenshot":
                    screenshot()
                elif event_data.get("message")[0:3].lower() == "say":
                    say(event_data.get("message")[4:].strip())
                elif event_data.get("message")[0:3].lower() == "txt":
                    txt(event_data.get("message")[4:].strip())
                elif event_data.get("message")[0:5].lower() == "textw":
                    res = event_data.get("message")[6:].strip()
                    res = res.split("#")
                    if len(res) == 2:
                        textw(res[0].strip(),res[1].strip())
                    else:
                        print("Invalid")
                elif event_data.get("message")[0:5].lower() == "texta":
                    res = event_data.get("message")[6:].strip()
                    res = res.split("#")
                    if len(res) == 2:
                        texta(res[0].strip(),res[1].strip())
                    else:
                        print("Invalid")
                elif event_data.get("message")[0:4].lower() == "open":
                    if len(event_data.get("message")) == 4:
                        open_app()
                    else:
                        open_app(event_data.get("message")[5:].strip())
                else:
                    print("Invalid Command")
    except (requests.exceptions.RequestException, TimeoutError) as e:
            # This catches connection timeouts, drops, and maximum retry errors
            print(
                f"\n[Network Error] Connection failed"
            )
    except KeyboardInterrupt:
       print("\nExiting cleanly. Goodbye!")



if __name__ == "__main__":
    main()
