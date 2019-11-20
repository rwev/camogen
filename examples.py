#! /usr/bin/env python
# coding=utf-8
#
# Modified 2019 Ryan William <rwev@protonmail.ch>
# Copyright © 2017 Gael Lederrey <gael.lederrey@epfl.ch>
# Based on the code of Ulf Alstrom (http://www.happyponyland.net/camogen.php)
#
# Distributed under terms of the MIT license.

import camogen
from PIL import Image

RUN_SCALE = 2500
SAVE_SCALE = 1000


def scale_and_save(pil_image, path):
    pil_image = pil_image.resize((SAVE_SCALE, SAVE_SCALE), Image.ANTIALIAS)
    pil_image.save(path)


parameters = {'width': RUN_SCALE,
              'height': RUN_SCALE,
              'polygon_size': 50,
              'color_bleed': 60,
              'max_depth': 100,
              'colors': ['#51452F', '#6D5344', '#776560', '#8E6E51', '#8F7E70', '#A08164', '#AB8E73', '#B69981'],
              'spots': {'amount': 0,
                        'radius': {'min': 2,
                                   'max': 10},
                        'sampling_variation': 5}}
scale_and_save(
    camogen.generate(parameters),
    './images/coyote-summer.png'
)

parameters = {'width': RUN_SCALE,
              'height': RUN_SCALE,
              'polygon_size': 150,
              'color_bleed': 300,
              'max_depth': 50,
              'colors': ['#A48C71', '#B6A798', '#C7BEB7', '#D1CBC7', '#D9D7D6', '#E2E5E8', '#ECEEEF'],
              'spots': {'amount': 0,
                        'radius': {'min': 2,
                                   'max': 10},
                        'sampling_variation': 5}}
scale_and_save(
    camogen.generate(parameters),
    './images/coyote-winter.png'
)
