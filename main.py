from loclm.models import *
'''
In this case enter english sentence as instructions to execute certain task of cell mechanics calculation.
The model. Both sentance to query and query to sentance have pre-trained models which can predict query
from user input as subsequently the sequence of task which need to executed. This sequence can be fed to 
a simulation kernal to perform tasks in said order.
'''                           
                              
input_sentences = ["calculate traction field from displacement image img1.png",
                   "Using this displacement image calculate traction field",
                   "calculate traction field from displacement field array provided",
                   "calculate traction field from this array",
                   "calculate displacement field from bead images"]

def sentence_to_sequence(sentence):
    sen2Qrymodel = Sen2Qrymodel('cellmech')
    qry2Seqmodel = Qry2Seqmodel('cellmech')
    query = sen2Qrymodel.predict(sentence)
    keys = list(query.keys())
    for key in keys:
        if query[key] is None:
            del query[key]     
    sqnce = qry2Seqmodel.predict(query)
    return query, sqnce

for sentence in input_sentences:
    query, sequence = sentence_to_sequence(sentence)
    print("\ninput sentence :", sentence, "\nfetched query : ", query, "\nfetched sqnce : ", sequence)