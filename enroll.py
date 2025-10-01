import cv2
import numpy as np
from db_utils import init_db, add_embedding
from face_utils import build_app, get_faces_and_embeddings

def main():
    init_db()
    app = build_app()

    name = input("Nome da pessoa a cadastrar: ").strip()
    if not name:
        print("Nome inválido.")
        return

    num_to_capture = 5
    print("Abrindo a câmera...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Não foi possível abrir a câmera.")
        return

    print("Instruções: olhe para a câmera. Tecle 'c' para capturar, 'q' para sair.")
    captured = 0

    while captured < num_to_capture:
        ok, frame = cap.read()
        if not ok:
            break

        display = frame.copy()
        cv2.putText(display, f"{name} | Capturados: {captured}/{num_to_capture}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        faces = get_faces_and_embeddings(app, frame)
        # desenha uma caixa se houver face
        for f in faces:
            x1, y1, x2, y2 = f["bbox"]
            cv2.rectangle(display, (x1, y1), (x2, y2), (255, 200, 0), 2)

        cv2.imshow("Cadastro (enroll)", display)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            if len(faces) == 0:
                print("Nenhum rosto detectado. Tente novamente.")
                continue
            # pega a face com maior área
            f = max(faces, key=lambda d: (d["bbox"][2]-d["bbox"][0])*(d["bbox"][3]-d["bbox"][1]))
            add_embedding(name, f["embedding"])
            captured += 1
            print(f"Captura #{captured} salva.")
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Cadastro finalizado: {name} com {captured} amostras.")

if __name__ == "__main__":
    main()
