# program to modify replace certain digits in the mnist data set for improved training
import struct
def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

def modify_labels(labelf, outf):
	o = open(outf, "wb")
	l = open(labelf, "rb")
	

	#i = int.from_bytes(l.read(4), byteorder='big')
	magicRaw= l.read(4)
	magicN = struct.unpack('>i', magicRaw)[0]
	numItemsRaw = l.read(4)
	numItems = struct.unpack('>i', numItemsRaw)[0]
	o.write(magicRaw)
	o.write(numItemsRaw)
	for i in range(numItems):
		itemValueRaw= l.read(1)
		itemValue = ord(itemValueRaw)
		if itemValue == 9:
			o.write(chr(itemValue))
		else:
			itemValue = 0
			o.write(chr(itemValue))
	o.close()
	l.close()

	modify_labels("./MNIST-data/t10k-labels-idx1-ubyte-orig","./MNIST-data/t10k-labels-idx1-ubyte-9to0")
	modify_labels("./MNIST-data/train-labels-idx1-ubyte-orig","./MNIST-data/train-labels-idx1-ubyte-9to0")

