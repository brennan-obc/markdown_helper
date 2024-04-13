import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#* update on save
# handler class
class MarkdownUpdateHandler(FileSystemEventHandler):
  def __init__(self, output_path, input_files):
    self.output_path = output_path
    self.input_files = input_files
    self.last_modified = {}
  
  def on_modified(self, event):
    if event.src_path in self.input_files and event.event_type == 'modified':
      current_time = time.time()
      # ignore changes to directory & debounce to eliminate duplicate notifications
      if not event.is_directory and (self.last_modified.get(event.src_path, 0) + 1 < current_time):
        generate_markdown(self.output_path, *self.input_files)
        pardir_file_name = os.path.join(os.path.basename(os.path.dirname(event.src_path)), os.path.basename(event.src_path))
        print(f"Changes detected in {pardir_file_name}; Markdown Codebase updated!")
        self.last_modified[event.src_path] = current_time


# file monitoring
def start_monitoring(output_path, *input_paths):
  event_handler = MarkdownUpdateHandler(output_path, input_paths)
  observer = Observer()
  paths_to_watch = set(os.path.dirname(path) for path in input_paths)
  for path in paths_to_watch:
    observer.schedule(event_handler, path, recursive=False)
  observer.start()
  try:
    while True:
      observer.join(1) # checks every second, indefinitely
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

  #* convert given documents into document of labeled Markdown codeblocks
# input
def read_file_content(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    return file.read()
  
# output
def generate_markdown(md_path, *file_paths):
  with open(md_path, 'w', encoding='utf-8') as md_file:
    for path in file_paths:
      try:
        content = read_file_content(path)
        file_name = os.path.basename(path)
        file_extension = file_name.split('.')[-1]
        md_file.write(f"###### `{file_name}`\n```{file_extension}\n{content}\n```\n")
      except Exception as e:
        print(f"Error processing {path}: {e}")

# entry
if __name__ == "__main__":
  # if insufficient arguments
  if len(sys.argv) < 3:
    print("Usage: python markdown_generator.py <output_md_path> <input_file_path1> [input_file_path2] ...")
  else:
    # args: 1. script, 2. output file path, 3+. input file path(s)
    output_md_path = sys.argv[1]
    input_files = sys.argv[2:]
    # begins monitoring of all input files, updates .md file on change
    start_monitoring(output_md_path, *input_files)