

    # from http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850375/raw/c18cfcd9580d382cb6d14e4708aab33a0916ff3e/1.+Introduction+to+Pandas.ipynb
    


    from IPython.core.display import HTML
    HTML("<iframe src=http://pandas.pydata.org width=800 height=350></iframe>")




<iframe src=http://pandas.pydata.org width=800 height=350></iframe>




    import pandas as pd
    # options
    pd.set_option('html', False)
    pd.set_option('max_columns',30)
    pd.set_option('max_rows',20)


    #series is a single vector  of data with an index
    counts = pd.Series([632,1638,569,115]) ; counts




    0     632
    1    1638
    2     569
    3     115
    dtype: int64




    counts.values




    array([ 632, 1638,  569,  115], dtype=int64)




    counts.index




    Int64Index([0, 1, 2, 3], dtype=int64)




    bacteria = pd.Series([632,1638,569,115] , 
                         index=['Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes'] ) 
    bacteria




    Firmicutes         632
    Proteobacteria    1638
    Actinobacteria     569
    Bacteroidetes      115
    dtype: int64




    bacteria[0]
    bacteria['Firmicutes']




    632




    bacteria[[name.endswith('bacteria') for name in bacteria.index]]




    Proteobacteria    1638
    Actinobacteria     569
    dtype: int64




    bacteria.name = 'counts'
    bacteria.index.name = 'phylum'
    bacteria




    phylum
    Firmicutes         632
    Proteobacteria    1638
    Actinobacteria     569
    Bacteroidetes      115
    Name: counts, dtype: int64




    np.log(bacteria)




    phylum
    Firmicutes        6.448889
    Proteobacteria    7.401231
    Actinobacteria    6.343880
    Bacteroidetes     4.744932
    Name: counts, dtype: float64




    

    'cat' is not recognized as an internal or external command,
    operable program or batch file.
    


    
