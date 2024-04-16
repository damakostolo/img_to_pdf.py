import img2pdf

# List of img files
image_files = ['NAPOLEON_1.jpg', 'NAPOLEON_2.jpg', 'NAPOLEON_3.jpg']#img name

# Convert images to PDF
with open('my_new_pdf3.pdf', 'wb') as f: #pdf title
    f.write(img2pdf.convert([open(image, 'rb') for image in image_files]))
