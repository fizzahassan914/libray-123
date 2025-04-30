import streamlit as st
import json
import os

# Data file
DATA_FILE = 'library.json'

# Load data
def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

# Save data
def save_books(books):
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

# App UI
st.title("📚 Personal Library Manager")

menu = ["Add Book", "View Library", "Update Book", "Delete Book"]
choice = st.sidebar.selectbox("Menu", menu)

books = load_books()

if choice == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    year = st.number_input("Year", min_value=0, step=1)
    status = st.selectbox("Status", ["Unread", "Reading", "Read"])

    if st.button("Add Book"):
        new_book = {"Title": title, "Author": author, "Genre": genre, "Year": year, "Status": status}
        books.append(new_book)
        save_books(books)
        st.success("Book added successfully!")

elif choice == "View Library":
    st.subheader("Your Library")
    if books:
        st.dataframe(books)
    else:
        st.info("No books found.")

elif choice == "Update Book":
    st.subheader("Update Book Status")
    titles = [book['Title'] for book in books]
    selected_book = st.selectbox("Select a Book", titles)
    new_status = st.selectbox("New Status", ["Unread", "Reading", "Read"])

    if st.button("Update"):
        for book in books:
            if book['Title'] == selected_book:
                book['Status'] = new_status
                save_books(books)
                st.success("Book status updated!")

elif choice == "Delete Book":
    st.subheader("Delete a Book")
    titles = [book['Title'] for book in books]
    selected_book = st.selectbox("Select a Book to Delete", titles)

    if st.button("Delete"):
        books = [book for book in books if book['Title'] != selected_book]
        save_books(books)
        st.success("Book deleted successfully!")
