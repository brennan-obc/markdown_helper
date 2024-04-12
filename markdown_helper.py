import sys
import os

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
    # 1. script, 2. output file path, 3+. input file path(s)
    output_md_path = sys.argv[1]
    input_files = sys.argv[2:]
    generate_markdown(output_md_path, *input_files)