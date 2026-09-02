import sys
import os
import subprocess

EXCLUDED = {"watcher.py", "runner.py"}

AUDIO_LIBS = {"pyttsx3", "pygame", "playsound", "simpleaudio", "pyaudio", "sounddevice", "gtts"}

def check_audio_imports(filepath):
    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                for lib in AUDIO_LIBS:
                    if f"import {lib}" in line or f"from {lib}" in line:
                        return lib
    except Exception:
        pass
    return None

# Find all .py files recursively across all folders
py_files = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename.endswith(".py") and filename not in EXCLUDED:
            py_files.append(os.path.join(dirpath, filename))

if not py_files:
    print("No Python files found.")
    sys.exit(0)

latest = max(py_files, key=lambda f: os.path.getmtime(f))

audio_lib = check_audio_imports(latest)
if audio_lib:
    print(f"WARNING: '{latest}' uses '{audio_lib}' which plays audio.")
    print("   Replit's console runs headlessly -- you won't hear any sound output.")
    print("   The code will still run, but audio will be silent.\n")

# Run the file using a wrapper that removes the workspace directory from
# sys.path so user .py files (e.g. string.py) never shadow stdlib modules.
file_dir = os.path.dirname(os.path.abspath(latest))
wrapper = (
    "import sys, os, runpy; "
    "cwd = os.getcwd(); "
    "sys.path = [p for p in sys.path if p not in ('', cwd)]; "
    f"sys.path.insert(0, r'{file_dir}'); "
    f"runpy.run_path(r'{latest}', run_name='__main__')"
)

print(f">>> Running: {latest}")
print("-" * 40)
subprocess.run([sys.executable, "-c", wrapper])
print("-" * 40)
print(f">>> Done: {latest}")
