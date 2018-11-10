Project Title:-
Read hidden information of picture files(jpg)

Introduction:-
JPEG and other image files include various headers that define the image size, number of colors, and other information needed to display the image.However, there may be times when we need additional information stored in the file header.

JPEG HEADER IDENTIFIRS
Marker Name   Identifier(in hexadecimal)    Description
SOI           ffd8                          Start of Image
APP0          ffe0                          JFIF Applicaion Segment
APPn          ffe1-ffef                     Other Application Segments
DQT           ffdb                          Quantization Table
SOF0          ffc0                          Start of Frame
DHT           ffc4                          Huffman Table
SOS           ffda                          Start of Scan
EOI           ffd9                          End of Image

Procedure:-
Using binary file operations in python, all the hidden i.e. header information in a file will be extracted. First, the jpeg file is opened in binary read mode. Then, the above mentioned markers are found and the information related to them ( such as segment length, etc) is displayed according to jpeg format.

Expected Outcome:-
It will extract the all the information shown in the jpeg header identifier.











