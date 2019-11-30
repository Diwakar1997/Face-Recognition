# Face-Recognition
Algorithm Used
Haar cascade classifier - For detection of faces
Local Binary Patterns Histograms (LBPH​ ) - ​ For recognition of faces
Language Used - ​ Python
Packages Required
1. OpenCv
2. Numpy
3. Pillow

Working of Programs
1. Collection of dataset, by running Capture.py it will automatically capture and save 50
images by providing id and the name of any person.

2. Training using dataset by running trainImage.py. It saves the trained dataset to folder
trainer/trainer.yml

3. Now we can run recognizeImage.py , it will show the name of person by inclosing face
in rectangular boxes with some accuracy.
