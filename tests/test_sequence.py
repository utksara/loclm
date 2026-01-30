from loclm.models import *
import json 
 
def test_seq2sqq():
    '''
    In this case enter english sentence as instructions to execute certain task of cell mechanics calculation.
    The model. Both sentance to query and query to sentance have pre-trained models which can predict query
    from user input as subsequently the sequence of task which need to executed. This sequence can be fed to 
    a simulation kernal to perform tasks in said order.
    '''                    
         
                                
    input_sentences = ["calculate traction field from displacement image img1.png",
                    "calculate traction field from displacement image",
                    "calculate traction field from displacement field array provided",
                    "calculate traction field from this array"]
    

    output_sentences = [["calculate displacement", "calculate traction"],
                    ["calculate displacement", "calculate traction"],
                    ["calculate traction"],
                    ["calculate traction"]]

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

    for i in range(0, len(input_sentences)):
        sentence = input_sentences[i]
        query, sequence = sentence_to_sequence(sentence)
        assert output_sentences[i] == sequence, f'expected :{output_sentences[i]}, actual :{sequence}'