import argparse
from document_reader import DocumentReader
from qa_engine import QAEngine


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask questions about a document")
    parser.add_argument(
        "--file",
        required=True,
        help="Path to PDF, DOCX, TXT, or XLSX file",
    )
    parser.add_argument("--question", required=True, help="Question to ask")
    args = parser.parse_args()

    reader = DocumentReader()
    texts = reader.read(args.file)
    engine = QAEngine(texts)
    print(engine.ask(args.question))


if __name__ == "__main__":
    main()
