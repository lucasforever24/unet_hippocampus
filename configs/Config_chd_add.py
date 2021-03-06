#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 Division of Medical Image Computing, German Cancer Research Center (DKFZ)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from trixi.util import Config


def get_add_config():
    # Set your own path, if needed.
    data_root_dir = os.path.abspath('data')  # The path where the downloaded dataset is stored.

    c = Config(

        do_instancenorm=True,  # Defines whether or not the UNet does a instance normalization in the contracting path
        do_load_checkpoint=False,
        checkpoint_dir='',

        # Adapt to your own path, if needed.
        google_drive_id='1RzPB1_bqzQhlWvU-YGvZzhx2omcDh38C',
        dataset_name='CHD_segmentation_dataset',
        base_dir=os.path.abspath('output_experiment'),  # Where to log the output of the experiment.

        data_root_dir=data_root_dir,  # The path where the downloaded dataset is stored.
        data_dir=os.path.join(data_root_dir, 'CHD_interpolation_dataset/preprocessed'),  # This is where your training and validation data is stored
        data_test_dir=os.path.join(data_root_dir, 'CHD_interpolation_dataset/preprocessed'),  # This is where your test data is stored

        split_dir=os.path.join(data_root_dir, 'CHD_interpolation_dataset'),  # This is where the 'splits.pkl' file is located, that holds your splits.
        scaled_image_16_dir=os.path.join(data_root_dir, 'CHD_interpolation_dataset/scaled_to_16'),
        scaled_image_32_dir=os.path.join(data_root_dir, 'CHD_interpolation_dataset/scaled_to_32'),
        scaled_image_64_dir=os.path.join(data_root_dir, 'CHD_interpolation_dataset/scaled_to_64'),
        stage_1_dir=os.path.join(data_root_dir, 'CHD_interpolation_dataset/stage_1'),
        stage_1_dir_32 = os.path.join(data_root_dir, 'CHD_interpolation_dataset/stage_1_32'),
        # stage_1_dir = os.path.join(data_root_dir, 'CHD_segmentation_dataset/stage_1')

    )

    print(c)
    return c
