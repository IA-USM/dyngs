import os

source = "C:/Users/pablo_7xoop1s/dyngs/Eagle2/extracted_frames_planar/dataset/"
output = "eagle"
endframe = 299

for i in range(2, endframe):
    print(f"Training frame {i}")
    os.system("python train.py -s {} -m {} --frame_idx {}".format(source, output, i))