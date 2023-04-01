PFA in the submission folder:

1. language_model.py
2. PnP_tokenized.txt
3. Ulysses_tokenized.txt : these are the modified text files obtained post-tokenization. These contain all the relevant tokens
4. smoothing.py : Implementation of Witten-Bell and Kneser-Ney smoothing algorithms
5. tokenizer.py : File for tokenizing the corpus as mentioned in the assignment
6. neural_language_model.py : contains the code for training a neural language model (NLM) on an LSTM. 
7. README.md
8. requirements.txt
9. my_model.h5 : epoch-wise checkpoints
10. line_graph.png : shows the plots for loss, accuracy, val_loss and val_accuracy. Owing to the the time crunch, the computations have been made and accordigly reported for 5 epochs. The hyperparameters were changed and the model was run again (previously) for 15 epochs but the readings were unchanged. The assumption for this might be the small vocabulary size.