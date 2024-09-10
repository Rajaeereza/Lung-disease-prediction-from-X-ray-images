# -*- coding: utf-8 -*-
"""covidnet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UctOyW5nGjLuSIzuFcZGU5LjiP5mM8Mn
"""

import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, DepthwiseConv2D, Dense, MaxPool2D, add, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


#--------------------------PRPE BLOCK-------------------------------------------
def PRPE(input, filters, strides=1):
    x = Conv2D(filters, kernel_size=1, activation='relu')(input)
    x = Conv2D(filters, kernel_size=1, activation='relu')(x)
    x = DepthwiseConv2D(kernel_size=3, activation='relu', padding='same', strides=strides)(x)
    x = Conv2D(filters, kernel_size=1, activation='relu')(x)
    x = Conv2D(filters, kernel_size=1, activation='relu')(x)
    return x
#-----------------------------CovidNet------------------------------------------
def covidnet(input_shape, n_classes):
  input_size = input_shape
  input = Input(input_shape)
  x = Conv2D(input_shape=input_size, filters=48, kernel_size=7, activation='relu', padding='same', strides=2)(input)
  x = MaxPool2D(pool_size=2)(x)

    # first_path
  c_1 = Conv2D(filters=48, kernel_size=1, activation='relu', padding='same')(x)
  p_1_1 = PRPE(x, 48)
  p_1_2 = PRPE(add([p_1_1, c_1]), 48)
  p_1_3 = PRPE(add([p_1_1, p_1_2, c_1]), 48)

    # second_path
  c_2 = Conv2D(filters=96, kernel_size=1, activation='relu', padding='same')(add([p_1_1, p_1_2, p_1_3, c_1]))
  c_2 = MaxPool2D(pool_size=2)(c_2)
  p_2_1 = PRPE(add([p_1_1, p_1_2, p_1_3, c_1]), 96, strides=2)
  p_2_2 = PRPE(add([p_2_1, c_2]), 96)
  p_2_3 = PRPE(add([p_2_1, p_2_2, c_2]), 96)
  p_2_4 = PRPE(add([p_2_1, p_2_2, p_2_3, c_2]), 96)

    # third_path
  c_3 = Conv2D(filters=192, kernel_size=1, activation='relu', padding='same')(add([p_2_1, p_2_2, p_2_3, p_2_4, c_2]))
  c_3 = MaxPool2D(pool_size=2)(c_3)
  p_3_1 = PRPE(add([p_2_1, p_2_2, p_2_3, p_2_4, c_2]), 192, strides=2)
  p_3_2 = PRPE(add([p_3_1, c_3]), 192)
  p_3_3 = PRPE(add([p_3_1, p_3_2, c_3]), 192)
  p_3_4 = PRPE(add([p_3_1, p_3_2, p_3_3, c_3]), 192)
  p_3_5 = PRPE(add([p_3_1, p_3_2, p_3_3, p_3_4, c_3]), 192)
  p_3_6 = PRPE(add([p_3_1, p_3_2, p_3_3, p_3_4, p_3_5, c_3]), 192)

    # fourth_path
  c_4 = Conv2D(filters=384, kernel_size=1, activation='relu', padding='same')(add([p_3_1, p_3_2, p_3_3, p_3_4, p_3_5, p_3_6, c_3]))
  c_4 = MaxPool2D(pool_size=2)(c_4)
  p_4_1 = PRPE(add([p_3_1, p_3_2, p_3_3, p_3_4, p_3_5, p_3_6, c_3]), 384, strides=2)
  p_4_2 = PRPE(add([p_4_1, c_4]), 384)
  p_4_3 = PRPE(add([p_4_1, p_4_2, c_4]), 384)

    # faltten and dense
  f = Flatten()(add([p_4_1, p_4_2, p_4_3, c_4]))
  d1 = Dense(96, activation='relu')(f)
  d2 = Dense(48, activation='relu')(d1)
  output = Dense(n_classes, activation='softmax')(d2)

  model = Model(input, output)
  return model
