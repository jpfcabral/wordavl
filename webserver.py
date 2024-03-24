import streamlit as st
from wordavl.wordavl import WordAVL

# Global variable to store the AVL tree
avltree = None

# Function to create AVL tree and initialize it with corpus
def create_avl_tree():
    global avltree
    avltree = WordAVL()
    avltree.read_corpus("assets/br-utf8.txt")
    avltree.train()

# Check if AVL tree has been initialized, if not, create it
if avltree is None:
    create_avl_tree()

# Streamlit UI
def main():
    st.title("Word Prefix Matcher")

    # Input for prefix
    prefix = st.text_input("Enter Prefix:", "")

    # Button to trigger the word retrieval
    if st.button("Get Words"):
        if prefix:
            words = avltree.autocomplete(prefix)
            st.write("Words found:")
            for word in words:
                st.write(word)
        else:
            st.warning("Please enter a prefix.")

if __name__ == "__main__":
    main()
