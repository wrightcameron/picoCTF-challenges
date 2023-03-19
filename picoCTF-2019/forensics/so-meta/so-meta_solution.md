# So Meta

## Problem

Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png).

## Links

* [picture](https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png)

## Notes

The image can be opened with `eog`, "eog - a GNOME image viewer ".  The image when opened is of a circle with smaller and fragmented circles within circles.  An icon shown sometimes in scifi but doesn't have any common meaning. The challange is called "So Meta," and it has a picture to download.

The meta data can be viewed with the `identify -verbose pico_img.png`,

```bash
$ identify -verbose pico_img.png 
Image: pico_img.png
  Format: PNG (Portable Network Graphics)
  Mime type: image/png
  Class: DirectClass
  Geometry: 600x600+0+0
  Units: Undefined
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianess: Undefined
  Depth: 8-bit
  Channel depth:
    red: 8-bit
    green: 8-bit
    blue: 8-bit
  Channel statistics:
    Pixels: 360000
    Red:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.70229)
      standard deviation: 98.4394 (0.386037)
      kurtosis: -1.65464
      skewness: -0.557373
      entropy: 0.262552
    Green:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.702288)
      standard deviation: 98.4398 (0.386038)
      kurtosis: -1.65463
      skewness: -0.557375
      entropy: 0.262631
    Blue:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.702291)
      standard deviation: 98.4393 (0.386037)
      kurtosis: -1.65464
      skewness: -0.557372
      entropy: 0.262415
  Image statistics:
    Overall:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.70229)
      standard deviation: 98.4395 (0.386037)
      kurtosis: -1.65463
      skewness: -0.557375
      entropy: 0.262533
  Colors: 843
  Histogram:
        36: (  0,  0,  0) #000000 black
	...
    217948: (255,255,255) #FFFFFF white
  Rendering intent: Perceptual
  Gamma: 0.454545
  Chromaticity:
    red primary: (0.64,0.33)
    green primary: (0.3,0.6)
    blue primary: (0.15,0.06)
    white point: (0.3127,0.329)
  Background color: white
  Border color: srgb(223,223,223)
  Matte color: grey74
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 600x600+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: Zip
  Orientation: Undefined
  Properties:
    Artist: picoCTF{s0_m3ta_fec06741}
    date:create: 2022-08-18T08:08:50-06:00
    date:modify: 2020-10-26T12:38:23-06:00
    png:IHDR.bit-depth-orig: 8
    png:IHDR.bit_depth: 8
    png:IHDR.color-type-orig: 2
    png:IHDR.color_type: 2 (Truecolor)
    png:IHDR.interlace_method: 0 (Not interlaced)
    png:IHDR.width,height: 600, 600
    png:sRGB: intent=0 (Perceptual Intent)
    png:text: 2 tEXt/zTXt/iTXt chunks were found
    signature: b4b34b413063f7efefcf33aeb2711fd6401d564724e71a461f74ba3c2c9087d3
    Software: Adobe ImageReady
  Artifacts:
    filename: pico_img.png
    verbose: true
  Tainted: False
  Filesize: 108795B
  Number pixels: 360000
  Pixels per second: 18MB
  User time: 0.020u
  Elapsed time: 0:01.020
  Version: ImageMagick 6.9.10-23 Q16 x86_64 20190101 https://imagemagick.org
```  

The identify command shows in the meta data that the artist is the flag.  Suprised that the flag wasn't going to be encoded in base64.

## Solution

The flag is found in the meta file of the pico_img.png.  Using the command `identify -verboise pico_img.png`, the flag is found under Properties->Artists.  The flag is picoCTF{s0_m3ta_fec06741}.

## Resources

* [How To View Image Metadata On Linux](https://ostechnix.com/how-to-view-image-metadata-on-linux/)

