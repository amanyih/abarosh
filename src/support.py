from os import walk
import pygame



def import_folder(path):
    # print(list(walk(path)))
    # print("inside import folder")
    surface_list = []
    for _,__,img_files in list(walk(path)):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
# if __name__ == "__main__":
#     print("inside support")
    
