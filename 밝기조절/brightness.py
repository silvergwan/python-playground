from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, factor=2):

    # 이미지 파일 불러오기
    img = Image.open(image_path)

    # 밝기 조절 기능( 객체 ) 생성
    enhancer = ImageEnhance.Brightness(img)

    # 밝기 조절 적용( factor 값 = 밝기 값 )
    img_output = enhancer.enhance(factor)

    # 원본 파일명 제거( 안하면 image.png.brightened... 처럼 됨 )
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # 같은 이름의 파일 존재 시 count를 증가시키며 재생성
    count = 1
    while os.path.exists(f"{base_name}_brightened_{count}.png"):
        count += 1

    # 최종 저장 경로
    save_path = f"{base_name}_brightened_{count}.png"

    # 결과 이미지 저장
    img_output.save(save_path)

    #결과 이미지 미리보기
    img_output.show()

if __name__ == "__main__":
    # 함수 실행
    adjust_brightness("밝기조절/image.png", 5)
