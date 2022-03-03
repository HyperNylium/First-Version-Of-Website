galatasaray = ('muslera', 'nelson', 'alpaslan', 'boey', 'vananhold', 'taylan', 'berkhan', 'cicaldau', 'kerem', 'diagne')
beşiktaş = 'ersin' 'welinton' 'vida' 'rıdvan' 'rosier' 'atiba' 'salih' 'alex' 'larin' 'batshuayi' 'ghezal'
fenerbahce = 'altay' 'kim' 'szalai' 'nazım' 'gustavo' 'mesut ' 'arda' 'valencia' 'osai' 'pelkas' 'sosa'
trabzonspor = 'uğurcan''vitor''bruno''berat''hamsik''djaniny''gervinho''cornelius''dorukhan''abdülkadir''nwakaeme'
psg = 'donnaruma' 'ramos' 'marquinhos' 'hakimi' 'bernat' 'paredes' 'veratti' 'wijnaldum' 'neymar' 'messi' 'mbappe'


while True:
    lokasyon = int(input('''
Takımlar:
1-Galatasaray
2-Beşiktaş
3-Fenerbahçe
4-Psg
5-Trabzonspor
6-Çıkış
Hangi takımla oynamak istediğinizi SAYILARLA belirtiniz.
:

'''))

    if lokasyon == 1:
        while True:
            secim1 = input('Galatasaray takımındaki oyuncuları tahmin etmeye çalışın: ')

            if secim1 in galatasaray:
                print('Tebrikler Doğru Cevap!')
            else:
                print('tekrar deneyiniz.')
            devam = input('Bitirmek ister misiniz?:')
            if devam == 'hayır':
                print('o zaman')
            if devam == 'evet':
                break
    elif lokasyon == 2:
        while True:
            secim2 = input('Beşiktaş takımındaki oyuncuları tahmin etmeye çalışın:')

            if secim2 in beşiktaş:
                print('Tebrikler Doğru Cevap!')
            else:
                print('Tekrar Deneyiniz')
            devam2 = input('Bitirmek ister misiniz?:')
            if devam2 == 'hayır':
                print('o zaman')
            if devam2 == 'evet':
                break

    elif lokasyon == 3:
        while True:
            secim3 = input('Fenerbahçe takımındaki oyuncuları tahmin etmeye çalışın:')

            if secim3 in fenerbahce:
                print('Tebrikler Doğru Cevap!')
            else:
                print('Tekrar deneyiniz')
            devam3 = input('Bitirmek ister misiniz?')

            if devam3 == 'evet':
                break
            if devam3 == 'hayır':
                print('o zaman')

    elif lokasyon == 4:
        while True:
            secim4 = input('Psg takımındaki oyuncuları tahmin etmeye çalışın:')

            if secim4 in psg:
                print('Tebrikler Doğru Cevap!')
            else:
                print('Tekrar deneyiniz')
            devam5 = input('Bitirmek ister misiniz?:')
            if devam5 == 'hayır':
                print('o zaman')
            if devam5 == 'evet':
                break
    elif lokasyon == 6:
        print('Görüşürüz :)')
        break
    elif lokasyon == 5:
        while True:

            secim5 = input('Trabzonspor takımındaki oyuncuları tahmin etmeye çalışın:')

            if secim5 in trabzonspor:
                print('Tebrikler Doğru Cevap!')
            else:
                print('Tekrar deneyiniz')
            devam4 = input('Bitirmek ister misiniz?:')
            if devam4 == 'hayır':
                print('o zaman')
            if devam4 == 'evet':
                break