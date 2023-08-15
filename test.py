from title_manager import *
import copy
# Connect to the database called 'library.db'
# tm = title_manager("library.db")
tm = title_manager(":memory:")
# Sample titles
t1 = Title("Hello Python", "BirFlex Inc.", "Mining", 5)
t2 = Title("Good Morning", "Alex Inc.", "Biology", 7)

# Add titles to the library database
tm.add_title(t1)
tm.add_title(t2)

# Show all the titles
tm.show()

# Amend a title
tm.update_title("Good Morning", new_publisher="Bill Inc.")
tm.update_title("Hello Python", new_genre= "Psychology", new_publisher="Bill Inc.")

# Remove a title
tm.remove_title("Good Morning")

# Show all the titles
print()
tm.show()

# Clear the title table
tm.clear()
