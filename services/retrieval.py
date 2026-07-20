"""Knowledge retrieval from uploaded documents."""

from pathlib import Path
from typing import Optional
from docx import Document


def read_docx(file_path: str) -> str:
    """Read text content from a DOCX file.

    Args:
        file_path: Path to the DOCX file.

    Returns:
        Extracted text content.
    """
    try:
        doc = Document(file_path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs)
    except Exception:
        return ""


def read_uploaded_file(uploaded_file) -> str:
    """Read text from an uploaded file (Streamlit UploadedFile).

    Args:
        uploaded_file: Streamlit UploadedFile object.

    Returns:
        Extracted text content.
    """
    try:
        if uploaded_file.name.endswith(".txt"):
            return uploaded_file.read().decode("utf-8")
        elif uploaded_file.name.endswith(".docx"):
            import io
            doc = Document(io.BytesIO(uploaded_file.read()))
            return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        elif uploaded_file.name.endswith(".pdf"):
            # Basic PDF text extraction
            try:
                import fitz  # PyMuPDF
                import io
                pdf_bytes = uploaded_file.read()
                doc = fitz.open(stream=pdf_bytes, filetype="pdf")
                text = ""
                for page in doc:
                    text += page.get_text()
                return text
            except ImportError:
                return "[PDF reading requires PyMuPDF. Install with: pip install pymupdf]"
        else:
            return ""
    except Exception as e:
        return f"[Error reading file: {str(e)}]"


def load_knowledge_context(max_chars: int = 8000) -> str:
    """Load context from knowledge documents (DOCX templates).

    Reads the BRAOU template documents to provide context for AI generation.

    Args:
        max_chars: Maximum characters to include.

    Returns:
        Combined text from knowledge documents.
    """
    knowledge_dir = Path(__file__).parent.parent / "knowledge"
    context_parts = []
    total_chars = 0

    # Prioritize BRAOU templates (DOCX files)
    docx_files = sorted(knowledge_dir.glob("*.docx"))

    for docx_file in docx_files:
        if total_chars >= max_chars:
            break
        content = read_docx(str(docx_file))
        if content:
            header = f"\n--- {docx_file.stem} ---\n"
            available = max_chars - total_chars - len(header)
            if available > 200:
                truncated = content[:available]
                context_parts.append(header + truncated)
                total_chars += len(header) + len(truncated)

    return "\n".join(context_parts)
