import cv2
import numpy as np
from insightface.app import FaceAnalysis
from config import MODEL_NAME, DET_SIZE

# Monta o app do InsightFace em CPU
def build_app():
    app = FaceAnalysis(name=MODEL_NAME, allowed_modules=['detection', 'recognition'])
    # ctx_id=-1 força CPU; se tiver GPU com onnxruntime-gpu, pode usar ctx_id=0
    app.prepare(ctx_id=-1, det_size=DET_SIZE)
    return app

def get_faces_and_embeddings(app, bgr_image):
    """Retorna lista de dicts: {bbox, kps, embedding, det_score} para cada face."""
    # InsightFace espera BGR (OpenCV) ou converte internamente
    faces = app.get(bgr_image)
    results = []
    for f in faces:
        # f.bbox = [x1, y1, x2, y2]; f.normed_embedding = vetor 512 normalizado (L2=1)
        results.append({
            "bbox": f.bbox.astype(int),
            "kps": f.kps,  # keypoints
            "embedding": f.normed_embedding.astype(np.float32),
            "det_score": float(f.det_score)
        })
    return results

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    # Se já vier normalizado, o dot já é o cosseno; garantimos normalização:
    a = a / (np.linalg.norm(a) + 1e-8)
    b = b / (np.linalg.norm(b) + 1e-8)
    return float(np.dot(a, b))
