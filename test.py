def testAll():
    assert( message([1])            ==  [0,0,1,1] )
    assert( message([0,0,1])        ==  [0,0,1,1,0,0,1,0,0,0,0] )
    assert( message([0,1,1,0])      ==  [0,1,0,0,0,1,1,0,0,0,0] )
    assert( message([1,1,1,1,0,1])  ==  [0,1,1,0,1,1,1,1,0,1,0] )

    assert( hammingEncoder([1,1,1])    ==  [] )
    assert( hammingEncoder([1,0,0,0])  ==  [1,1,1,0,0,0,0] )
    assert( hammingEncoder([0])        ==  [0,0,0] )
    assert( hammingEncoder([0,0,0])    ==  [] )

    assert( hammingDecoder([1,0,1,1])        ==  [])
    assert( hammingDecoder([0,1,1,0,0,0,0])  ==  [1,1,1,0,0,0,0] )
    assert( hammingDecoder([1,0,0,0,0,0,1])  ==  [1,0,0,0,0,1,1] )
    assert( hammingDecoder([1,1,0])          ==  [1,1,1])
    assert( hammingDecoder([1,0,0,0,0,0,0])  ==  [0,0,0,0,0,0,0] )

    assert( messageFromCodeword([1,0,1,1])        ==  [] )
    assert( messageFromCodeword([1,1,1,0,0,0,0])  ==  [1,0,0,0] )
    assert( messageFromCodeword([1,0,0,0,0,1,1])  ==  [0,0,1,1] )
    assert( messageFromCodeword([1,1,1,1,1,1,1])  ==  [1,1,1,1] )
    assert( messageFromCodeword([0,0,0,0])        ==  [] )
    
    assert( dataFromMessage([1,0,0,1,0,1,1,0,1,0])    ==  [] )
    assert( dataFromMessage([1,1,1,1,0,1,1,0,1,0,0])  ==  [] )
    assert( dataFromMessage([0,1,0,1,0,1,1,0,1,0,0])  ==  [0,1,1,0,1] )
    assert( dataFromMessage([0,0,1,1])                ==  [1] )
    assert( dataFromMessage([0,0,1,1,0,0,1,0,0,0,0])  ==  [0,0,1] )
    assert( dataFromMessage([0,1,0,0,0,1,1,0,0,0,0])  ==  [0,1,1,0] )
    assert( dataFromMessage([0,1,1,0,1,1,1,1,0,1,0])  ==  [1,1,1,1,0,1] )
    assert( dataFromMessage([1,1,1,1])                ==  [] )

    assert( repetitionEncoder([0],4)  ==  [0,0,0,0])
    assert( repetitionEncoder([0],2)  ==  [0,0])
    assert( repetitionEncoder([1],4)  ==  [1,1,1,1])

    assert( repetitionDecoder([1,1,0,0])  == [] )
    assert( repetitionDecoder([1,0,0,0])  == [0] )
    assert( repetitionDecoder([0,0,1])    == [0] )
    assert( repetitionDecoder([1,1,1,1])  == [1] )

    print('all tests passed')