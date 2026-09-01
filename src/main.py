import cv2
import os

INPUT_DIR = "images/input"
OUTPUT_DIR = "images/results"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):

    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    input_path = os.path.join(INPUT_DIR, filename)

    image = cv2.imread(input_path)

    if image is None:
        print(f"Não foi possível abrir: {filename}")
        continue

    # 1. Conversão para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Redução de ruído
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. Detecção de bordas
    edges = cv2.Canny(blur, 50, 150)

    # Nome do arquivo de saída
    name, extension = os.path.splitext(filename)
    output_filename = f"{name}_canny{extension}"

    output_path = os.path.join(OUTPUT_DIR, output_filename)

    # Salva o resultado
    cv2.imwrite(output_path, edges)

    print(f"Processado: {filename} -> {output_filename}")

print("\nExperimento concluído!")