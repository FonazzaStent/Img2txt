Image to Text 1.0.0

The program will convert an image to text, with the purpose of analyzing it to spot intelligible words. Use the program with selfies, profile pics, photos of artworks you created or your friends did, your pet's photo or any other image, to reveal the hidden messages of the image. If you use it on photo portraits, such as Facebook selfies, it may reveal less visible aspects of the portrayed person's personality. The resulting text will be a long string of mostly repeating characters but, every so often, you'll notice an intelligible word, either spelled normally or with repeated letters, missing letters or anagramed letters. It takes a little allegoric-freudian psychological exegetic ability to elaborate the right chain of mind associations to infere a convincing interpretation of the resulting text. You may want to share the text with a psychologist to get a professional opinion on your interpretation, but sometimes the meaning will be surprisingly obvious.
Because of my coding skills limitations, the program requires a little collaboration on the user side, as the image must be mandatorily in a certain format, obtainable by converting it through an image manipulation program such as free and open source GIMP.

Procedure for GIMP:

- open the image
- Edit - Copy
- Edit - Paste as - New Image
- click on new image tab
- Image - Scale Image
- input 240 in the Height field, preserving ratio (the chain icon near the size fields must be in "closed" position)
- Click "Scale" button
- Image - Mode - Indexed
- Generate optimum palette - input 26 as a value
- Color dithering - choose Floyd-Steinberg
- Convert
- File - Export - Name: [your file name].bmp (it must be in BMP format)
- Click "Export"
- Export Image as BMP - Click "Export"

You can use a different photo manipulation program, as long as it can produce a 240 pixel tall image and reduce the RGB image to an indexed image with a 26 colors colormap.

Now load the image in the program:

- Open the program, click on Edit - Open.

The resulting text will appear in the text window. You can copy the text right selecting it and right clicking on or through the Edit - Copy command, if you want to paste it to another program to save it or email it.
