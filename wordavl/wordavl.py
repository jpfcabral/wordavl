from loguru import logger

from wordavl.structures.avl import AVLNode
from wordavl.structures.avl import AVLTree
from wordavl.text_data import TextData


class WordAVL(AVLTree):
    def __init__(self, corpus="", verbose=False) -> None:
        """
        Initialize a WordAVL object.

        Args:
            corpus (str, optional): A string representing the corpus of words. Defaults to "".
            verbose (bool, optional): Whether to print verbose logging information. Defaults to False.
        """
        super().__init__()
        self.corpus = corpus
        self.verbose = verbose

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
            self.add(word)

        logger.info(f"AVL population completed with height: {self.get_height()}")

    def autocomplete(self, prefix: str):
        """
        Provide autocomplete suggestions based on the given prefix.

        Args:
            prefix (str): The prefix for which autocomplete suggestions are requested.

        Returns:
            str: A string containing autocomplete suggestions based on the provided prefix.
                Returns an empty string if no prefix is provided.
        """
        if not prefix or prefix == "":
            return ""

        return self._find_all_elements_with_prefix(prefix=prefix)

    def _find_all_elements_with_prefix(self, prefix: str):
        """
        Find all elements in the AVL tree with the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            list: A list containing all elements in the AVL tree with the given prefix.
        """
        results = list()

        for word in self._find_recursive(self.root, prefix):
            results.append(word)

        return results

    def _find_recursive(self, current_node: AVLNode, prefix: str):
        """
        Recursively find all node values with the given prefix starting from the current node.
        """

        # Check if the current node value starts with the prefix
        if current_node is not None and current_node.value.startswith(prefix):
            yield current_node.value

        # Recursively search in the left subtree
        if current_node is not None:
            yield from self._find_recursive(current_node.left_child, prefix)

        # Recursively search in the right subtree
        if current_node is not None:
            yield from self._find_recursive(current_node.right_child, prefix)
