from pathlib import Path

from app.ingestion.pdf_loader import load_pdf
from app.ingestion.text_splitter import split_text
from app.vectorstore.chroma import vector_store

DATA_FOLDER = Path("data")

for pdf in DATA_FOLDER.glob("*.pdf"):

    print(f"Procesando {pdf.name}")

    text = load_pdf(str(pdf))

    chunks = split_text(text)

    vector_store.add_texts(
        texts=chunks,
        metadatas=[
            {
                "source": pdf.name
            }
            for _ in chunks
        ]
    )

print()

print("Documentos indexados correctamente.")