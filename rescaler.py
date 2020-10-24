import os

from PIL import Image
from resizeimage import resizeimage
a = 0
b = 0
c = 0

images = os.listdir("../stylegan2-ada/images")
for i in images:
    with open(os.path.join("../stylegan2-ada/images", i), 'r+b') as f:
        try:
            with Image.open(f) as image:
                try:
                    cover = resizeimage.resize_cover(image, [64, 64])
                    print("Succesfully resized")
                    a += 1
                except:
                    try:
                        cover = resizeimage.resize_cover(image, [32, 32])
                        print("Succesfully resized")

                        b += 1
                    except:
                        try:
                            cover = resizeimage.resize_cover(image, [16, 16])
                            print("Succesfully resized")
                            c += 1
                        except Exception as e:
                            print("Resize failed: {}".format(e))

                cover.save(os.path.join("../stylegan2-ada/images", i), image.format)

        except Exception as e:
            print("Resize failed: {}".format(e))

print("64: {} 32: {} 16:{}".format(a, b, c))