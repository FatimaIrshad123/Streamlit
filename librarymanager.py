import streamlit as st

if "books" not in st.session_state:
    st.session_state.books = []


def add_book():
    st.subheader("➕ Add a New Book")
    title = st.text_input("Enter Book Title:")
    author = st.text_input("Enter Author Name:")
    publication_year = st.number_input("Enter Publication Year:", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Enter Genre:")
    read_status = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        st.session_state.books.append({
            "title": title,
            "author": author,
            "publicationYear": publication_year,
            "Genre": genre,
            "readStatus": read_status
        })
        
        st.success(f'📖 "{title}" added successfully!')

def remove_book():
    st.subheader("🗑 Remove a Book")
    if st.session_state.books:
        titles = [book["title"] for book in st.session_state.books]
        selected_book = st.selectbox("Select a book to remove:", titles)

        if st.button("Remove Book"):
            st.session_state.books[:] = [book for book in st.session_state.books if book["title"] != selected_book]
            st.success(f'🗑 "{selected_book}" removed successfully!')
    else:
        st.warning("No books available to remove!")

def search_book():
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("Enter book title to search:")
    
    if st.button("Search"):
        found_books = [book for book in st.session_state.books if search_query.lower() in book["title"].lower()]
        if found_books:
            for book in found_books:
                st.write(f"📖 **{book['title']}** by {book['author']} ({book['publicationYear']}) - {book['Genre']}")
        else:
            st.warning("Book not found!")

def display_books():
    st.subheader("📖 All Books")
    if st.session_state.books:
        for book in st.session_state.books:
            st.write(f"📌 **{book['title']}** by {book['author']} ({book['publicationYear']}) - {book['Genre']} | Read: {book['readStatus']}")
    else:
        st.info("No books available.")

def display_statistics():
    st.subheader("📊 Book Statistics")
    total_books = len(st.session_state.books)
    read_books = sum(book["readStatus"] for book in st.session_state.books)
    unread_books = total_books - read_books

    st.write(f"📚 Total Books: {total_books}")
    st.write(f"✅ Read Books: {read_books}")
    st.write(f"❌ Unread Books: {unread_books}")


st.sidebar.title("📚 Book Management System")
menu = st.sidebar.radio("Choose an option:", 
                        ["➕ Add a Book", "🗑 Remove a Book", "🔍 Search for a Book", "📖 Display All Books", "📊 Display Statistics", "🚪 Exit"])

st.title("📚 Personal Library Manager")
# Display the selected menu option
if menu == "➕ Add a Book":
    add_book()

elif menu == "🗑 Remove a Book":
    remove_book()

elif menu == "🔍 Search for a Book":
    search_book()

elif menu == "📖 Display All Books":
    display_books()

elif menu == "📊 Display Statistics":
    display_statistics()

elif menu == "🚪 Exit":
    st.success("Thank you for using the Book Management System! 😊")
