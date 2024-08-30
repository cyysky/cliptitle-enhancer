import os
import sys
import pkg_resources
import pyperclip
import requests
from bs4 import BeautifulSoup
import threading
import time
from plyer import notification
from infi.systray import SysTrayIcon

class ClipTitleEnhancer:
    def __init__(self):
        self.running = False
        self.paused = False
        self.systray = None

    def fetch_og_h1_or_link_title(self, url):
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                og_title_tag = soup.find('meta', property='og:title')
                if og_title_tag and og_title_tag.get('content'):
                    return og_title_tag.get('content')
                else:
                    h1_tag = soup.find('h1')
                    if h1_tag and h1_tag.text:
                        return h1_tag.text.strip()
                    else:
                        title_tag = soup.find('title')
                        if title_tag and title_tag.string:
                            return title_tag.string.strip()
        except Exception as e:
            print(f"Error fetching URL: {e}")
        return None

    def show_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_name="Clipboard Monitor",
            timeout=5
        )

    def monitor_clipboard(self):
        previous_text = ""
        while self.running:
            if not self.paused:
                text = pyperclip.paste()
                if text != previous_text and text.startswith('http'):
                    og_title = self.fetch_og_h1_or_link_title(text)
                    if og_title:
                        new_content = og_title + '\n' + text
                        pyperclip.copy(new_content)
                        print(new_content)
                        self.show_notification("Title Added", f"Added title to clipboard:\n{og_title[:50]}...")
                    previous_text = text
            time.sleep(1)

    def on_quit_callback(self, systray):
        self.running = False
        print("Quitting...")

    def toggle_pause(self, systray):
        self.paused = not self.paused
        status = "Paused" if self.paused else "Monitoring"
        self.systray.update(hover_text=f"Clipboard Monitor ({status})")
        print(f"Clipboard monitoring {status}")
        self.show_notification("Clipboard Monitor", f"Monitoring {status}")

    def start(self):
        self.running = True
        menu_options = (("Toggle Pause/Resume", None, self.toggle_pause),)
        
        # Get the icon path
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle, the PyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app 
            # path into variable _MEIPASS'.
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
        
        icon_path = os.path.join(application_path, 'icon.ico')
        
        # If icon is not found, use a fallback method
        if not os.path.exists(icon_path):
            try:
                icon_path = pkg_resources.resource_filename('cliptitle', 'icon.ico')
            except Exception as e:
                print(f"Error loading icon: {e}")
                icon_path = None  # SysTrayIcon can handle None for the icon

        self.systray = SysTrayIcon(icon_path, "Cliptitle Enhancer (Monitoring)", menu_options, on_quit=self.on_quit_callback)
        self.systray.start()
        
        clipboard_thread = threading.Thread(target=self.monitor_clipboard, daemon=True)
        clipboard_thread.start()

        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

        self.systray.shutdown()

def main():
    monitor = ClipTitleEnhancer()
    monitor.start()

if __name__ == "__main__":
    main()
