import os
import re
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import efficientnet
from tensorflow.keras.layers import TextVectorization
from model.transformer_cnn import *
vocab = vectorization.get_vocabulary()

index_lookup = dict(zip(range(len(vocab)), vocab))
max_decoded_sentence_length = SEQ_LENGTH - 1
cnn_model = get_cnn_model()

encoder = TransformerEncoderBlock(embed_dim=EMBED_DIM, dense_dim=FF_DIM, num_heads=1)
decoder = TransformerDecoderBlock(embed_dim=EMBED_DIM, ff_dim=FF_DIM, num_heads=2)
caption_model = ImageCaptioningModel(
    cnn_model=cnn_model, encoder=encoder, decoder=decoder, image_aug=None,
)
def call_fn(batch, training):
    return batch

caption_model.call = call_fn

# input_tensor = np.random.rand(1, 299, 299, 3)
# sample_y = tf.zeros((1, 25))
# Call the model on the input tensor
# caption_model((input_tensor, sample_y))

sample_x, sample_y = tf.random.normal((1, 299, 299, 3)), tf.zeros((1, 25))
caption_model((sample_x, sample_y))

sample_img_embed = caption_model.cnn_model(sample_x, training=False)
sample_enc_out = caption_model.encoder(sample_img_embed, training=False)
caption_model.decoder(sample_y, sample_enc_out, training=False)
print(caption_model.layers)
caption_model.load_weights("model/model_IC.h5")


def generate_caption(file):

    # Read the image from the disk
    sample_img = decode_and_resize(file)
    img = sample_img.numpy().clip(0, 255).astype(np.uint8)
    plt.imshow(img)
    plt.show()

    # Pass the image to the CNN
    img = tf.expand_dims(sample_img, 0)
    img = caption_model.cnn_model(img)

    # Pass the image features to the Transformer encoder
    encoded_img = caption_model.encoder(img, training=False)

    # Generate the caption using the Transformer decoder
    decoded_caption = "<start>"
    for i in range(max_decoded_sentence_length):
        tokenized_caption = vectorization([decoded_caption])[:, :-1]
        mask = tf.math.not_equal(tokenized_caption, 0)
        predictions = caption_model.decoder(
            tokenized_caption, encoded_img, training=False, mask=mask
        )
        sampled_token_index = np.argmax(predictions[0, i, :])
        print(sampled_token_index)
        if sampled_token_index > 8671:
            continue
        else:
            sampled_token = index_lookup[sampled_token_index]
        
        if sampled_token == "<end>":
            break
        decoded_caption += " " + sampled_token

    decoded_caption = decoded_caption.replace("<start> ", "")
    decoded_caption = decoded_caption.replace(" <end>", "").strip()
    print("Predicted Caption: ", decoded_caption)
    return f'Predicted: {decoded_caption}'

# Check predictions for a few samples
# generate_caption('boat.jpeg')
