from time import time

from loguru import logger

from wordavl.text_data import TextData


class WordList:
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
        logger.debug("Initializing list population for corpus")
        start_time = time()

        text_data = TextData(source=text_source)
        self.corpus = text_data.get_unique_words()

        logger.debug(
            f"List population completed with {len(self.corpus)} elements and took: {round(time()-start_time, 5)}s"
        )

    def autocomplete(self, prefix: str):

        start_time = time()
        results = list()

        for word in self._find_recursive(prefix=prefix):
            results.append(word)

        logger.debug(
            f"List search took {round(time()-start_time, 5)}s and found {len(results)} results"
        )
        return results

    def _find_recursive(self, prefix: str):
        for word in self.corpus:
            if word.startswith(prefix):
                yield word
