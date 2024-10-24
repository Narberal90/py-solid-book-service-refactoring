from app.book import Book
from app.display import (
    ReverseDisplayStrategy,
    ConsoleDisplayStrategy
)
from app.print import (
    ReversePrintStrategy,
    ConsolePrintStrategy
)
from app.serializer import (
    XMLSerializationStrategy,
    JSONSerializationStrategy
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                strategy = ReverseDisplayStrategy()
            else:
                strategy = ConsoleDisplayStrategy()
            book.display(strategy)
        elif cmd == "print":
            if method_type == "reverse":
                strategy = ReversePrintStrategy()
            else:
                strategy = ConsolePrintStrategy()
            book.print(strategy)
        elif cmd == "serialize":
            if method_type == "xml":
                strategy = XMLSerializationStrategy()
            else:
                strategy = JSONSerializationStrategy()
            return book.serialize(strategy)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
