# Invisible-Watermark Guide

add-watermark.py demonstrates how to add a watermark to the file `james.jpg` and save the watermarked image to `james-watermarked.jpg`

find-watermark.py demonstrates how to read the watermark in `james-watermarked.jpg` and output it to the terminal

The watermark itself is hardcoded in add-watermark.py, and the length of the watermark is hardcoded in james-watermarked.jpg

I had trouble getting this working in the following scenarios:

* Watermarking illustrations, including those with blank or solid colour backgrounds
* Watermarks longer than 8 characters

## Commands

```
pip install -r requirements.txt
python add-watermark.py
python find-watermark.py
```

Note that this is based on documentation from https://github.com/ShieldMnt/invisible-watermark