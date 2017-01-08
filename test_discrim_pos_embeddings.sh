#!/bin/bash
build/nt-parser/nt-parser --cnn-mem 1700 -x -T corpora/train.oracle -p corpora/test.oracle -C corpora/test.stripped --pretrained_dim 300 -P -w embeddings/GoogleNews-ptb_filtered-vectors-negative300.txt --lstm_input_dim 128 --hidden_dim 128 -D 0.2 -m ntparse_pos_pretrained_0_2_32_128_16_128-pid924.params # before stackfix
