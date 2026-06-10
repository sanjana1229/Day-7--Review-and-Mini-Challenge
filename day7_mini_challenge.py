from __future__ import print_function
import cv2
import numpy as np
import argparse
import imutils
import os

print("=" * 60)
print("DAY 7 MINI CHALLENGE")
print("=" * 60)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to image")
ap.add_argument("-b", "--blend", required=False,
                help="Path to blend image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

if image is None:
    print("ERROR: Could not load image")
    exit()

height, width = image.shape[:2]

print(f"Loaded image: {width} x {height}")

blend_image = None

if args["blend"]:
    blend_image = cv2.imread(args["blend"])

    if blend_image is not None:
        blend_image = cv2.resize(blend_image, (width, height))

output_dir = "day7_output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Output folder created")
output_dir = "day7_output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Output folder created")

# PASTE THE NEW CODE HERE ↓↓↓

print("\n[STEP 2] Adding annotations...")

annotated = image.copy()

cv2.rectangle(annotated, (120, 120), (280, 280),
              (0, 255, 0), 3)

cv2.circle(annotated, (200, 200),
           40, (0, 0, 255), 3)

cv2.putText(annotated,
            "ROI",
            (150, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2)

cv2.imshow("Annotated", annotated)

cv2.imwrite(
    os.path.join(output_dir, "01_annotated.png"),
    annotated
)

cv2.waitKey(0)

print("Saved: 01_annotated.png")
print("\n[STEP 3] Applying transformations...")

# Resize
resized = imutils.resize(image, width=300)

cv2.imshow("Resized", resized)
cv2.imwrite(
    os.path.join(output_dir, "02_resized.png"),
    resized
)
cv2.waitKey(0)

# Rotate
rotated = imutils.rotate(image, 15)

cv2.imshow("Rotated", rotated)
cv2.imwrite(
    os.path.join(output_dir, "03_rotated.png"),
    rotated
)
cv2.waitKey(0)

# Flip
flipped = imutils.flip(image, "horizontal")

cv2.imshow("Flipped", flipped)
cv2.imwrite(
    os.path.join(output_dir, "04_flipped.png"),
    flipped
)
cv2.waitKey(0)

# Crop
cropped = imutils.crop(
    image,
    100, 300,
    100, 300
)

cv2.imshow("Cropped", cropped)
cv2.imwrite(
    os.path.join(output_dir, "05_cropped.png"),
    cropped
)
cv2.waitKey(0)

print("Transformations complete")
print("\n[STEP 4] Creating blended image...")

if blend_image is not None:

    blended = cv2.addWeighted(
        image,
        0.7,
        blend_image,
        0.3,
        0
    )

    cv2.imshow("Blended", blended)

    cv2.imwrite(
        os.path.join(output_dir, "06_blended.png"),
        blended
    )

    cv2.waitKey(0)

    print("Saved: 06_blended.png")
    print("\n[STEP 5] Creating mask...")

# Create black mask
mask = np.zeros(image.shape[:2], dtype="uint8")

# White circle in center
cv2.circle(mask,
           (width // 2, height // 2),
           100,
           255,
           -1)

cv2.imshow("Mask", mask)

cv2.imwrite(
    os.path.join(output_dir, "07_mask.png"),
    mask
)

cv2.waitKey(0)

# Apply mask
masked = cv2.bitwise_and(
    image,
    image,
    mask=mask
)

cv2.imshow("Masked", masked)

cv2.imwrite(
    os.path.join(output_dir, "08_masked.png"),
    masked
)

cv2.waitKey(0)

print("Saved: 07_mask.png")
print("Saved: 08_masked.png")
print("\n[STEP 6] Creating collage...")

# Resize all images to same size
img1 = cv2.resize(annotated, (200, 200))
img2 = cv2.resize(rotated, (200, 200))
img3 = cv2.resize(flipped, (200, 200))
img4 = cv2.resize(masked, (200, 200))

top_row = np.hstack([img1, img2])
bottom_row = np.hstack([img3, img4])

collage = np.vstack([top_row, bottom_row])

cv2.putText(
    collage,
    "DAY 7 WEEK 1 SUMMARY",
    (120, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2
)

cv2.imshow("Final Collage", collage)

cv2.imwrite(
    os.path.join(output_dir, "09_collage.png"),
    collage
)

cv2.waitKey(0)

print("Saved: 09_collage.png")

cv2.destroyAllWindows()

print("\n" + "=" * 60)
print("DAY 7 COMPLETE!")
print("=" * 60)
print("Week 1 Skills Practiced:")
print("✓ Image Loading")
print("✓ Drawing")
print("✓ Transformations")
print("✓ Blending")
print("✓ Masking")
print("✓ Collage Creation")