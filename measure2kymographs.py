import numpy as np
import os
from anglemanagerv2 import AngleManager
from skimage.io import imsave
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float, img_as_ubyte, img_as_int
from skimage.color import gray2rgb
from tkinter import filedialog

app = AngleManager()
app.load_kymographs()

#computes orientation vector
app.compute_coords(method="PCA")

#computes angle line
app.compute_regression()

#calculates the angle value for each kymograph
app.compute_angles()
print("Kym1 Angle: " + str(app.kym1_angle) + "; Kym2 Angle: " + str(app.kym2_angle) + " ; Angle Diff: " + str(app.angle_diff))

save_path = filedialog.askdirectory()

imsave(save_path + os.sep + "regression_kym1.tiff", img_as_ubyte(app.kymograph_1_w_line))
imsave(save_path + os.sep + "regression_kym2.tiff", img_as_ubyte(app.kymograph_2_w_line))
