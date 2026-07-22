from app.vectorstore.chroma import vector_store
from core.config import TOP_K_RESULTS


class RAGService:
    """
    Servicio encargado de recuperar contexto relevante
    desde la base vectorial utilizando búsqueda semántica.
    """
    def retrieve_context(self, question: str, k: int = TOP_K_RESULTS) -> str:

        documents = vector_store.similarity_search(
            question,
            k=k
        )

        if not documents:
            return ""
        
        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        return context