import csv
import random

headers = ['file_name', 'label', 'frame_count', 'width', 'height', 'fps', 'duration', 'bitrate']


file_names = ['video_{:03d}.mp4'.format(i) for i in range(1, 1001)]
labels = ['Real', 'Fake']
frame_counts = [random.randint(100, 500) for _ in range(1000)]
widths = [640] * 1000
heights = [480] * 1000
fps = [30] * 1000
durations = [random.randint(5, 15) for _ in range(1000)]
bitrates = [random.randint(500, 2000) for _ in range(1000)]


rows = zip(file_names * 1000, labels * 5000, frame_counts * 1000, [640] * 10000, [480] * 10000, [30] * 10000, durations * 1000, bitrates * 1000)


with open('video_dataset.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)

print('CSV file generated successfully.')
