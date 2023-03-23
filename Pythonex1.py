def kisalt_ipv6(ipv6_adres):

    kisaltma_sayisi = ipv6_adres.count(':')
    ipv6_blok = ipv6_adres.split(':')
    yeni_ipv6_blok = []

    # Kısaltma belirtilmemişse
    if '::' not in ipv6_adres:
        # Her bir IPv6 bloğunu zfill() kullanarak 4 karakterli hale getirin
        yeni_ipv6_blok = [b.zfill(4) for b in ipv6_blok]
        # IPv6 adresi 8 bloktan daha azsa, eksik blokları 0'larla doldurun
        if len(yeni_ipv6_blok) < 8:
            sifir_sayisi = 8 - len(yeni_ipv6_blok)
            yeni_ipv6_blok += ['0000'] * sifir_sayisi

    # Kısaltma belirtilmişse
    else:
        # Kısaltma işaretini belirleyin ve blokları ikiye ayırın
        indeks = ipv6_blok.index('')
        onceki_blok = ipv6_blok[:indeks]
        sonraki_blok = ipv6_blok[indeks+1:]

        # Kısaltma işareti blokların başında veya sonunda değilse ve birden fazla kısaltma işareti varsa hatalı formatta olduğunu belirtin
        if indeks != 0 and indeks != 7 and '' not in sonraki_blok and kisaltma_sayisi > 1:
            return "Yanlış IPv6 adresi formatı"

        # Önceki blokları 4 karakterli hale getirin ve yeni bloklara ekleyin
        for blok in onceki_blok:
            yeni_ipv6_blok.append(blok.zfill(4))

        # Kısaltılan blokları 0'larla doldurun ve yeni bloklara ekleyin
        sifir_sayisi = 8 - len(ipv6_blok) + 1
        for i in range(sifir_sayisi):
            yeni_ipv6_blok.append('0000')

        # Sonraki blokları 4 karakterli hale getirin ve yeni bloklara ekleyin
        for blok in sonraki_blok:
            yeni_ipv6_blok.append(blok.zfill(4))

    # Sıfırları kısaltın
    kisaltma = ':'.join([b.lstrip('0') or '0' for b in yeni_ipv6_blok])
    kisaltma = kisaltma.replace(':0:', '::', 1)
    kisaltma = kisaltma.replace(':0:', ':', 1)

    return kisaltma

ipv6_adresi = input('Kısaltılacak IPv6 adresini girin: ')
kisaltilmis_adres = kisalt_ipv6(ipv6_adresi)
print('Kısaltılmış adres: ', kisaltilmis_adres)
