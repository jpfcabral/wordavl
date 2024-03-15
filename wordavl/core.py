from loguru import logger

from wordavl.structures.avl import AVLTree
from wordavl.text_data import TextData


class WordAVL:
    def __init__(self, corpus="", verbose=False) -> None:
        """
        Initialize a WordAVL object.

        Args:
            corpus (str, optional): A string representing the corpus of words. Defaults to "".
            verbose (bool, optional): Whether to print verbose logging information. Defaults to False.
        """
        self.corpus = corpus
        self.verbose = verbose
        self.avl_tree = AVLTree()

    def read_corpus(self, text_source: str) -> None:
        """
        Read the corpus from a text source and populate the AVL tree.

        Args:
            text_source (str): The source of the text data (file path or URL).
        """
        text_data = TextData(source=text_source)
        self.corpus = text_data.get_unique_words()

    def train(self) -> None:
        """
        Train the AVL tree with the corpus.
        """
        logger.info(f"Initializing AVL population for corpus with length: {len(self.corpus)}")

        for word in self.corpus:
            self.avl_tree.add(word)

        logger.info(f"AVL population completed with height: {self.avl_tree.get_height()}")
