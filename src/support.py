from os import walk
import pygame



def import_folder(path):
 
    surface_list = []
    for _,__,img_files in list(walk(path)):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            
            if path[24] == "r":
                resized_image = pygame.transform.scale(image_surf, (50, 80))
                surface_list.append(resized_image)
            else:
                surface_list.append(image_surf)

    return surface_list

