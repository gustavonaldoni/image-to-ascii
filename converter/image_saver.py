class ASCIIImageSaver:
    
    def save_image(self, text, path):
        with open(path, 'w') as file:
            file.write(text)