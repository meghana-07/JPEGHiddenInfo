Title:-
Read hidden information of picture files(jpg)

Introduction:-
JPEG and other image files include various headers that define the image size, number of colors, and other information needed to display the image.However, there may be times when we need additional information stored in the file header.

JPEG HEADER IDENTIFIRS:-
1. SOI(Start of Image)
2. APP0(JFIF Applicaion Segment)
3. APPn(Other Application Segments)
4. DQT(Quantization Table)
5. SOF0(Start of Frame)
6. DHT(Huffman Table)
7. SOS(Start of Scan)
8. EOI(End of Image)

Procedure:-
Using binary file operations in python, all the hidden i.e. header information in a file will be extracted. First, the jpeg file is opened in binary read mode. Then, the above mentioned markers are found and the information related to them ( such as segment length, etc) is displayed according to jpeg format.

Expected Outcome:-
It will extract the all the information shown in the jpeg header identifier.
