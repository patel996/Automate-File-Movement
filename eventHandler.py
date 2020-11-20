import sys
import os
import logging
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
import shutil

class Handle(PatternMatchingEventHandler):
        def __init__(self):
            PatternMatchingEventHandler.__init__(self, patterns = ['*.xlsx','*.doc', '*.pdf', '*.jpg', '*jpeg', '*.png', '*.gif', '*.exe'],case_sensitive = True, ignore_directories = True)
        def on_created(self, event):
            if (event.src_path.endswith('.xlsx') or event.src_path.endswith('.doc') or event.src_path.endswith('.pdf')):
                print("Document Downloaded. Move to Documents Folder")
                shutil.move(event.src_path, "/Users/fenypatel/Documents")
                print("moved")
            if (event.src_path.endswith('.jpeg') or event.src_path.endswith('.png') or event.src_path.endswith('.jpg') or  event.src_path.endswith('.gif')):
                print("Image Downloaded. Move to Images Folder")
                shutil.move(event.src_path, "/Users/fenypatel/Pictures")
                print("moved")

if __name__ == "__main__":

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'

    event_handler = Handle()
    observer = Observer()
    observer.schedule(event_handler, path, recursive = True)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
