import sys
import os

# Prevent user .py files from shadowing stdlib modules
_cwd = os.getcwd()
for _p in ['', _cwd]:
    if _p in sys.path:
        sys.path.remove(_p)

import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DEBOUNCE_SECONDS = 0.5
last_run = {}

def run_file(filepath):
    filename = os.path.basename(filepath)
    now = time.time()
    if last_run.get(filepath, 0) + DEBOUNCE_SECONDS > now:
        return
    last_run[filepath] = now
    print(f"\n>>> Running: {filename}\n{'-' * 40}")
    subprocess.run([sys.executable, filepath])
    print(f"{'-' * 40}\n>>> Done: {filename}\n")

class PythonFileHandler(FileSystemEventHandler):
    def _should_run(self, path):
        return path.endswith(".py") and os.path.basename(path) != "watcher.py"

    def on_created(self, event):
        if not event.is_directory and self._should_run(event.src_path):
            run_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory and self._should_run(event.src_path):
            run_file(event.src_path)

    def on_moved(self, event):
        if not event.is_directory and self._should_run(event.dest_path):
            run_file(event.dest_path)

if __name__ == "__main__":
    print("Watching for Python files...")
    print("Create or save any .py file to run it automatically.\n")
    event_handler = PythonFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
