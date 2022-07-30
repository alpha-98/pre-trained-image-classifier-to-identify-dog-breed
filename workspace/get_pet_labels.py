#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Gambhir Rathore
# DATE CREATED: 2022-07-30                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from time import perf_counter

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()
    filename_list = listdir(image_dir)
    pet_label_list = []
    for filename in filename_list :
      pet_label_list.append(create_pet_label(filename))

    for idx in range(0, len(filename_list), 1):
      if filename_list[idx] not in results_dic:
         results_dic[filename_list[idx]] = [pet_label_list[idx]]
      else:
         print("** Warning: Key=", filename_list[idx], 
               "already exists in results_dic with value =", 
               results_dic[filename_list[idx]])
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic

def create_pet_label (image_name) : 
  """
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_name - name of images that are to be (string)
    Returns:
      pet_label - pet image label (string)
    """
  # Sets string to lower case letters
  low_image_name = image_name.lower()
  # Splits lower case string by _ to break into words 
  word_list_image_name = low_image_name.split("_")
  # Create pet_label starting as empty string
  pet_label = ""

  # Loops to check if word in pet name is only
  # alphabetic characters - if true append word
  # to pet_label separated by trailing space 
  for word in word_list_image_name :
    if word.isalpha():
        pet_label += word + " "

  # Strip off starting/trailing whitespace characters
  pet_label = pet_label.strip()

  # Prints resulting pet_label
  return pet_label