from Bateaux import Bateau

boat = Bateau(2, 2, 3, 'vertical')

dico = {
    '2;3' : '',
    '3;3' : ''
}

assert boat.dico_pos == dico