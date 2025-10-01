import sqlite3
import numpy as np
import io
import datetime
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Tabela simples: 1 embedding por linha (pode haver várias linhas por pessoa)
    c.execute("""
        CREATE TABLE IF NOT EXISTS faces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            embedding BLOB NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def _ndarray_to_blob(arr: np.ndarray) -> bytes:
    mem = io.BytesIO()
    np.save(mem, arr.astype(np.float32))
    mem.seek(0)
    return mem.read()

def _blob_to_ndarray(blob: bytes) -> np.ndarray:
    mem = io.BytesIO(blob)
    mem.seek(0)
    return np.load(mem, allow_pickle=False)

def add_embedding(name: str, embedding: np.ndarray):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO faces (name, embedding, created_at) VALUES (?, ?, ?)",
        (name, _ndarray_to_blob(embedding), datetime.datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def load_all_embeddings():
    """Retorna listas paralelas: names, embeddings (np.ndarray de shape [N, D])."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, embedding FROM faces")
    rows = c.fetchall()
    conn.close()
    names, vecs = [], []
    for name, blob in rows:
        names.append(name)
        vecs.append(_blob_to_ndarray(blob))
    if len(vecs) == 0:
        return [], np.zeros((0,512), dtype=np.float32)
    return names, np.stack(vecs).astype(np.float32)
