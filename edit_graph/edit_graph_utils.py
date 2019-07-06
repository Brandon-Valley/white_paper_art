from PIL import Image
import PIL.ImageOps    

image = Image.open("C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_g.JPG")

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save("C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_graph_inverted.JPG")