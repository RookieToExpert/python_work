# Writing to a file
from pathlib import Path as pa

"""
write_text() will overwrite the original content, and will create a new file if file doesn't exit in the path
"""
path = pa('summary.txt')
path.write_text("Testing ---- New line by write_text()")

# Create a new file using write_text
path = pa('newfile.txt')
path.write_text("Testing line.")

# Write multiple lines using write_text()
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)