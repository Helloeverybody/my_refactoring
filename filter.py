from PIL import Image
import numpy as np


def find_average_gray(pic):
    height = len(pic)
    gray_val = 0
    for h in range(0, height):
        for w in range(0, height):
            pixel = pic[h, w]
            gray_val += int(pixel[0] / height ** 2 + pixel[1] / height ** 2 + pixel[2] / height ** 2)
    return gray_val


def make_square_gray(pic, h_val, w_val, p_size, colors_count):
    grad_step = int(256 // colors_count) * 3
    gray_color_val = find_average_gray(pic[h_val:h_val + p_size, w_val:w_val + p_size])
    for sq_height in range(h_val, h_val + p_size):
        for sq_width in range(w_val, w_val + p_size):
            gray_value = int(gray_color_val // grad_step) * grad_step / 3
            pic[sq_height, sq_width][0] = gray_value
            pic[sq_height, sq_width][1] = gray_value
            pic[sq_height, sq_width][2] = gray_value
    return pic


image = Image.open(input("Введите название картинки, если она в папке проекта, или путь к ней, если нет (формат JPG): "))
pixel_size = int(input("Введите размер пикселя: "))
colors_count = int(input("Введите количество цветов (рекомендуется 15): "))

i_width, i_height = image.size
new_height = i_height - i_height % pixel_size + pixel_size
new_width = i_width - i_width % pixel_size + pixel_size
image = image.resize((new_width, new_height), Image.ANTIALIAS)

array = np.array(image)
height = len(array)
width = len(array[1])
ost_w = 0
ost_h = 0

for i in range(0, height - pixel_size + 1, pixel_size):
    for j in range(0, width - pixel_size + 1, pixel_size):
        make_square_gray(array, i, j, pixel_size, colors_count)
        ost_w = j
    ost_h = i

res = Image.fromarray(array)
res.save(input("Название сохраняемого файла?: ") + '.jpg')
