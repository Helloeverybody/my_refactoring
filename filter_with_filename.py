from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, size, gradation_step):
    '''
    Переводит картинку в пиксельную мозаику
    :param image: [[[int, int, int]]]
    :param size: int
    :param gradation_step: int

    :return: [[[int, int, int]]]

    >>> convert_image_to_mosaic((np.ones((3, 3, 3)) * 200), 2, 15)
    array([[[195., 195., 195.],
            [195., 195., 195.],
            [ 90.,  90.,  90.]],
    <BLANKLINE>
           [[195., 195., 195.],
            [195., 195., 195.],
            [ 90.,  90.,  90.]],
    <BLANKLINE>
           [[ 90.,  90.,  90.],
            [ 90.,  90.,  90.],
            [ 45.,  45.,  45.]]])

    '''
    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    '''
    Берет усередненный серый цвет области
    :param block: [[[int, int, int]]]
    :param size: int
    :param gradation_step: int
    :return int

    >>> get_average_brightness(np.ones((3, 3, 3)) * 200, 2, 15)
    195
    >>> get_average_brightness(np.ones((3, 3, 3)) * 100, 2, 15)
    90
    >>> get_average_brightness(np.ones((3, 3, 3)) * 100, 6, 6)
    24
    >>> get_average_brightness(np.ones((10, 10, 3)) * 100, 6, 6)
    96
    '''
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    a = int(average_color // gradation_step) * gradation_step
    return a


def main():
    '''
    Загружает картинку, отправляет ее в метод пикселизации,
    а затем сохраняет полученный результат в файл
    '''
    image_file = Image.open("scale1200.jpg")
    block_size = 10
    gradations_count = 50
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    res = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    res.save("res_new.jpg")


if __name__ == '__main__':
    main()
