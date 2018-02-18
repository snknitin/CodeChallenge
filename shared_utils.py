from arff2pandas import a2p

def arff_to_df(input,output):
    """
    Helper method to convert arff from file to pandas.DataFrame
    :param filename:
    :return: Dataframe
    """

    with open(input) as f:
       df= a2p.load(f)
       df.to_pickle(output)