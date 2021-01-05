from PIL import Image

infile = 'Cadiadinho.jpg'
outfile = 'Cadiadinhooo.jpg'

imagen = Image.open(infile)
imagen.rotate(90).save(outfile)