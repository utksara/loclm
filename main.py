from loclm.models import *
                              
input_sentances = ["calculate traction field from displacement image img1.png"]

def sentence_to_sequence(sentance):
    sen2Qrymodel = Sen2Qrymodel()
    qry2Seqmodel = Qry2Seqmodel()
    query = sen2Qrymodel.predict(sentance)
    sqnce = qry2Seqmodel.predict(query)
    return sqnce

for sentance in input_sentances:
    print("\n sentance :", sentance, "\nfetched sequence : ", sentence_to_sequence(sentance))