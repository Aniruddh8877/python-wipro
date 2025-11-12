import zlib

data = b'Python Standard Library'
compressed = zlib.compress(data)

print('compressed data: ',compressed)

#decompress the data

decompressed = zlib.decompress(compressed)

print('decompressed data: ',decompressed)

print('original data',len(data))
print('compressed data',len(compressed))