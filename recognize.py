import cv2
import numpy as np
from db_utils import init_db, load_all_embeddings
from face_utils import build_app, get_faces_and_embeddings, cosine_similarity
from config import THRESHOLD

def main():
    init_db()
    names, vecs = load_all_embeddings()   # names: [N], vecs: [N, 512]
    if len(names) == 0:
        print("Banco vazio. Cadastre alguém com 'python enroll.py'.")
        return

    app = build_app()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Não foi possível abrir a câmera.")
        return

    print("Reconhecimento ativo. Tecle 'q' para sair.")
    while True:
        ok, frame = cap.read()
        if not ok:
            break

        faces = get_faces_and_embeddings(app, frame)
        for f in faces:
            emb = f["embedding"]  # [512], normalizado
            # vetoriza: sim com todos, pega o melhor
            sims = np.dot(vecs / (np.linalg.norm(vecs, axis=1, keepdims=True)+1e-8), emb / (np.linalg.norm(emb)+1e-8))
            best_idx = int(np.argmax(sims)) if sims.size > 0 else -1
            best_sim = float(sims[best_idx]) if best_idx >= 0 else -1.0

            if best_sim >= THRESHOLD and best_idx >= 0:
                person = names[best_idx]
                access = True
                color = (0, 200, 0)  # verde
                label = f"{person} | ACESSO ({best_sim:.2f})"
            else:
                access = False
                color = (0, 0, 255)  # vermelho
                label = f"DESCONHECIDO | NEGADO ({best_sim:.2f})"

            x1, y1, x2, y2 = f["bbox"]
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            y_text = max(25, y1 - 10)
            cv2.putText(frame, label, (x1, y_text), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Controle de Acesso - Reconhecimento", frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
