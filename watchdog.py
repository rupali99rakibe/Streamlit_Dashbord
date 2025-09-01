import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

REPO_PATH = r"D:\Rupali_Personal\Streamlit_dashboard\Streamlit_Dashbord"
BRANCH = "main"
COMMIT_MESSAGE = "Auto update on save"

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File changed: {event.src_path}")
            os.chdir(REPO_PATH)
            subprocess.call(["git", "add", "."])
            subprocess.call(["git", "commit", "-m", COMMIT_MESSAGE])
            subprocess.call(["git", "push", "origin", BRANCH])

if __name__ == "__main__":
    path = REPO_PATH
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Watching for file changes... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
