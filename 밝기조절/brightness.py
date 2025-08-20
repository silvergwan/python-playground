from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, factor=1.5):
    img = Image.open(image_path)

    enhancer = ImageEnhance.Brightness(img)
    img_output = enhancer.enhance(factor)

    # 자동으로 파일명 번호 붙이기
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    count = 1
    while os.path.exists(f"{base_name}_brightened_{count}.png"):
        count += 1

    save_path = f"{base_name}_brightened_{count}.png"
    img_output.save(save_path)
    img_output.show()
    print(f"✅ 저장 완료: {save_path}")

if __name__ == "__main__":
    adjust_brightness("밝기조절/image.png", 4)
