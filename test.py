from title_manager import *

# Connect to the database called 'library.db'
tm = title_manager("library.db")
# Sample titles
t1 = Title("Hello Python", "BirFlex Inc.", "Mining", 5)
t2 = Title("Good Morning", "Alex Inc.", "Biology", 7)

# Add titles to the library database
tm.add_title(t1)
tm.add_title(t2)

# Show all the titles
tm.show()

# Clear the title table
tm.clear()
