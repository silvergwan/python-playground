from PIL import Image, ImageEnhance

def adjust_brightness(image_path, factor=1.5):
    img = Image.open(image_path)

    enhancer = ImageEnhance.Brightness(img)
    img_output = enhancer.enhance(factor)

    img_output.save("brightened.png")
    img_output.show()

if __name__ == "__main__":
    adjust_brightness("밝기조절/image.png", 5)
