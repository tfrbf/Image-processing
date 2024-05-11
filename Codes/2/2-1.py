import cv2
import os

# تابع برای مرتب‌سازی تصاویر بر اساس مساحت
def sort_by_area(images):
    return sorted(images, key=lambda img: img.shape[0] * img.shape[1])

# مسیر پوشه حاوی تصاویر
folder_path = "Images"

# بارگیری تصاویر
images = []
for filename in os.listdir(folder_path):
    img_path = os.path.join(folder_path, filename)
    if os.path.isfile(img_path):
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)

# مرتب‌سازی تصاویر بر اساس مساحت
sorted_images = sort_by_area(images)

# نمایش تصاویر به ترتیب مساحت (کلید Q برای خروج)
for img in sorted_images:
    cv2.imshow("Sorted Images", img)
    key = cv2.waitKey(1000)  # نمایش هر تصویر به مدت یک ثانیه
    if key == ord('q') or key == ord('Q'):
        break

cv2.destroyAllWindows()
