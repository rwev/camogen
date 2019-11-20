#! /usr/bin/env python
# coding=utf-8
#
# Modified 2019 Ryan William <rwev@protonmail.ch>
# Copyright © 2017 Gael Lederrey <gael.lederrey@epfl.ch>
# Based on the code of Ulf Alstrom (http://www.happyponyland.net/php)
#
# Distributed under terms of the MIT license.

from PIL import Image
from camogen import generate, DEFAULT_PARAMETERS

SAVE_SCALE = 0.5


def scale_and_save(pil_image, path):
    scaled_size = (int(DEFAULT_PARAMETERS.WIDTH * SAVE_SCALE), int(DEFAULT_PARAMETERS.HEIGHT * SAVE_SCALE))
    pil_image = pil_image.resize(scaled_size, Image.ANTIALIAS)
    pil_image.save(path)


scale_and_save(
    generate(
        {
            **DEFAULT_PARAMETERS,
            'polygon_size': 50,
            'color_bleed': 60,
            'max_depth': 100,
            'colors': ['#51452F', '#6D5344', '#776560', '#8E6E51', '#8F7E70', '#A08164', '#AB8E73', '#B69981'],
        }
    ),
    './images/coyote-summer.png'
)

scale_and_save(
    generate(
        {
            **DEFAULT_PARAMETERS,
            'polygon_size': 150,
            'color_bleed': 300,
            'max_depth': 50,
            'colors': ['#A48C71', '#B6A798', '#C7BEB7', '#D1CBC7', '#D9D7D6', '#E2E5E8', '#ECEEEF'],
        }
    ),
    './images/coyote-winter.png'
)
