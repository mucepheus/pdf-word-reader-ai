import os
import tempfile
import openpyxl

from document_reader import DocumentReader
from qa_engine import QAEngine


def test_txt_question_answering():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w")
    tmp.write("Cats purr and dogs bark.")
    tmp.close()
    reader = DocumentReader()
    texts = reader.read(tmp.name)
    engine = QAEngine(texts)
    answer = engine.ask("What sound do cats make?")
    os.unlink(tmp.name)
    assert "purr" in answer.lower()


def test_xlsx_question_answering():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name", "Age"])
    ws.append(["Alice", 30])
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    wb.save(tmp.name)
    reader = DocumentReader()
    texts = reader.read(tmp.name)
    engine = QAEngine(texts)
    answer = engine.ask("How old is Alice?")
    os.unlink(tmp.name)
    assert "30" in answer
