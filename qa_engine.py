import re
from typing import List

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:  # pragma: no cover
    TfidfVectorizer = None
    cosine_similarity = None


class QAEngine:
    """Simple QA engine using TF-IDF cosine similarity."""

    def __init__(self, texts: List[str]):
        if TfidfVectorizer is None:
            raise ImportError("scikit-learn is required for QAEngine")
        self.segments = [t.strip() for t in texts if t.strip()]
        self.vectorizer = TfidfVectorizer()
        if self.segments:
            self.matrix = self.vectorizer.fit_transform(self.segments)
        else:
            self.matrix = None

    def ask(self, question: str, top_k: int = 3) -> str:
        if not self.segments:
            return "No answer found."
        q_vec = self.vectorizer.transform([question])
        sims = cosine_similarity(q_vec, self.matrix)[0]
        best = sims.argsort()[::-1][:top_k]
        answers: List[str] = []
        for i in best:
            if sims[i] <= 0:
                continue
            sentences = re.split(r"(?<=[.!?]) +", self.segments[i])
            answers.extend(sentences)
        if not answers:
            return "No answer found."
        return "\n".join(f"- {s.strip()}" for s in answers if s.strip())
