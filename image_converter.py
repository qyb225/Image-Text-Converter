from PIL import Image

def image_transfer(image_addr, file_name, out_size = None):
    """
    :param image_addr: image address
    :param file_name: name of output file (e.g. convert.txt)
    :param out_size: size of output file
    """

    #设置不同灰度值对应的 ASCII 字符
    ascii_char = list("@B$QMW&80#%XUOmbdpqoahkZYCjv" 
                 + "unxLJlIftizcr|/(){[1+?<>!;~\"^,:-.'` ")
    
    #打开图片文件并 resize
    img = Image.open(image_addr)
    if out_size:
        img = img.resize(out_size)

    #调用convert, 得到写入 text 的字符串
    text = convert(img, ascii_char)

    f = open(file_name, "w")
    f.write(text)
    f.close()

def convert(img, ascii_char):
    text = ""

    ascii_length = len(ascii_char)

    for i in range(img.size[1]):
        for j in range(img.size[0]):
            #获取每个pixel的 rgb 值
            r, g, b = img.getpixel((j, i))

            #经典灰度转换公式
            pixel_gray = r * 0.299 + g * 0.587 + b * 0.114

            #将灰度值转化为字符
            text += ascii_char[int((pixel_gray / 256) * ascii_length)]
        text += '\n'
    return  text

# Run
# image_transfer("your_image.jpg", "your_image.txt", (265, 70))
image_transfer("./images/joker.jpg", "./text/joker.txt", (265, 70))