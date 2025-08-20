import cv2
import numpy as np


depth_gray = cv2.imread("images/depth_gray.png", cv2.IMREAD_GRAYSCALE)

depth_colored = cv2.applyColorMap(depth_gray, cv2.COLORMAP_JET)

# grayscale sequence
g1 = depth_gray
g2 = cv2.blur(depth_gray, (3,3))
g3 = cv2.blur(depth_gray, (5,5))
g4 = cv2.blur(depth_gray, (7,7))
g5 = cv2.blur(depth_gray, (9,9))
g6 = cv2.blur(depth_gray, (11,11))
g7 = cv2.blur(depth_gray, (13,13))
g8 = cv2.blur(depth_gray, (15,15))
g9 = cv2.blur(depth_gray, (17,17))
g10 = cv2.blur(depth_gray, (19,19))
g11 = cv2.blur(depth_gray, (21,21))
g12 = cv2.blur(depth_gray, (23,23))
g13 = cv2.blur(depth_gray, (25,25))
g14 = cv2.blur(depth_gray, (27,27))
g15 = cv2.blur(depth_gray, (29,29))
g16 = cv2.blur(depth_gray, (31,31))
g17 = cv2.blur(depth_gray, (33,33))
g18 = cv2.blur(depth_gray, (35,35))
g19 = cv2.blur(depth_gray, (37,37))
g20 = cv2.blur(depth_gray, (39,39))
g21 = cv2.blur(depth_gray, (41,41))


row1 = np.hstack([g1, g2, g3])
row2 = np.hstack([g4, g5, g6])
row3 = np.hstack([g7, g8, g9])
row4 = np.hstack([g10, g11, g12])
row5 = np.hstack([g13, g14, g15])
row6 = np.hstack([g16, g17, g18])
row7 = np.hstack([g19, g20, g21])

grid_gray = np.vstack([row1, row2, row3, row4, row5, row6, row7])

# colored sequence
c1 = depth_colored
c2 = cv2.blur(depth_colored, (3,3))
c3 = cv2.blur(depth_colored, (5,5))
c4 = cv2.blur(depth_colored, (7,7))
c5 = cv2.blur(depth_colored, (9,9))
c6 = cv2.blur(depth_colored, (11,11))
c7 = cv2.blur(depth_colored, (13,13))
c8 = cv2.blur(depth_colored, (15,15))
c9 = cv2.blur(depth_colored, (17,17))
c10 = cv2.blur(depth_colored, (19,19))
c11 = cv2.blur(depth_colored, (21,21))
c12 = cv2.blur(depth_colored, (23,23))
c13 = cv2.blur(depth_colored, (25,25))
c14 = cv2.blur(depth_colored, (27,27))
c15 = cv2.blur(depth_colored, (29,29))
c16 = cv2.blur(depth_colored, (31,31))
c17 = cv2.blur(depth_colored, (33,33))
c18 = cv2.blur(depth_colored, (35,35))
c19 = cv2.blur(depth_colored, (37,37))
c20 = cv2.blur(depth_colored, (39,39))
c21 = cv2.blur(depth_colored, (41,41))

row1c = np.hstack([c1, c2, c3])
row2c = np.hstack([c4, c5, c6])
row3c = np.hstack([c7, c8, c9])
row4c = np.hstack([c10, c11, c12])
row5c = np.hstack([c13, c14, c15])
row6c = np.hstack([c16, c17, c18])
row7c = np.hstack([c19, c20, c21])

grid_colored = np.vstack([row1c, row2c, row3c, row4c, row5c, row6c, row7c])


# cv2.imshow("Gray Grid", grid_gray)
# cv2.imshow("Colored Grid", grid_colored)

# while True:
#     key = cv2.waitKey(1) & 0xFF
#     if key in (ord('1'), 27):  # press '1' or ESC
#         break

# cv2.destroyAllWindows()

cv2.imwrite("images/04_average_gray_grid.png", grid_gray)
cv2.imwrite("images/04_average_colored_grid.png", grid_colored)
