def naturalu_po_ebalu(chislo):
    if (chislo > 1 and chislo % 2 != 0 and chislo % 3 != 0 and chislo % 4 != 0 and chislo % 5 != 0 and chislo % 6 != 0 and chislo % 7 != 0 and chislo % 8 != 0 and chislo % 9 != 0) or (chislo == 2 or chislo == 3 or chislo == 5 or chislo == 7):
        return print('Натурал')
    else:
        return print('Не натурал(гей)')


naturalu_po_ebalu(16)
