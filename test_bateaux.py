from Bateaux import Bateau

boat = Bateau(2, 2, 3, 'vertical')

dico = {
    '2;2' : '',
    '2;3' : ''
}

assert boat.dico_pos == dico