### Markdown Code-Base Generator

###### Have you ever found yourself copying & pasting several documents into Markdown code-blocks?
I've done it many times. Usually, it's when I've got a small bug, and I want to roll the dice on whether a language model can save me the time of hunting that bug down.
In its current form, this script works as follows:
1. Navigate to directory containing script in a terminal
2. Run the following:
   - `python markdown_helper.py `
   - `<desired_output_directory\desired_output_file_path.md>`
   - `<1st_file_to_be_reproduced_in_markdown>`
   - `[2nd_file_to_be_reproduced_in_markdown]`
     - (no quantity limit on input files) 
3. All files passed as input will be formatted in an organized and readable fashion, and saved in a single markdown document at the provided destination
   - For each file:
     - _File Name:_ H6 file path label prefixing each file's contents
     - _File Contents:_ Contained in properly typed Markdown code-block
- In most consoles, the `UpArrow` key can be used to quickly repeat this command, allowing one to keep the console window open, and update their Markdown codebase document in 2 keystrokes    

---
### Example
> A screenshot of my console with the command required to create a Markdown codebase of the documents involved with my personal website's background, and the tail end of that document being viewed in Obsidian.md—a _wonderful_ application which has helped me tremendously.
![input_output_example](https://github.com/brennan-obc/markdown_helper/assets/113397554/36d4a076-36b8-46ac-8a5e-b5e90454c099)

---
#### Plans
- Implement GUI with file explorer for vastly improved file selection
  
