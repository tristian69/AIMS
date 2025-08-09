from PIL import Image

# JPG 열기
img = Image.open("./aims/aims.jpg")

# RGBA로 변환 (투명도 포함 필요시)
img = img.convert("RGBA")

# 리사이즈 (예: 256x256)
img = img.resize((256, 256))

# 저장 (ICO)
img.save("icon.ico", format='ICO')