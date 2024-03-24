import typer
from wordavl.wordavl import WordAVL
from wordavl.word_list import WordList

app = typer.Typer()

# Function to create the appropriate word class based on the argument
def create_word_class(word_class: str):
    if word_class.lower() == "avl":
        word_avl = WordAVL()
        word_avl.read_corpus("assets/br-utf8.txt")
        word_avl.train()
        return word_avl
    elif word_class.lower() == "list":
        word_list = WordList()
        word_list.read_corpus("assets/br-utf8.txt")
        return word_list
    else:
        raise ValueError("Invalid word class. Choose 'avl' or 'list'.")

# Command to search for words with a given prefix
@app.command()
def search(word_class: str):
    word_instance = create_word_class(word_class)
    typer.echo("Welcome to Word Prefix Matcher CLI!")
    typer.echo("Enter a prefix to search for words or type 'exit' to quit.")
    while True:
        prefix = typer.prompt("Enter Prefix:")
        if prefix.lower() == "exit":
            break
        elif prefix:
            words = word_instance.autocomplete(prefix)
            if words:
                typer.echo("Words found:")
                typer.echo(words)
            else:
                typer.echo("No words found with the given prefix.")
        else:
            typer.echo("Please provide a prefix.")

if __name__ == "__main__":
    app()
