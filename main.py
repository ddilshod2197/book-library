def flight_ticket_price_comparator(turli_narxlari):
    # Eng arzon reys narxi
    eng_arzon_narx = min(turli_narxlari.values())
    
    # Eng qimmat reys narxi
    eng_qimmat_narx = max(turli_narxlari.values())
    
    # Eng arzon reys nomi
    eng_arzon_reys = [nomi for nomi, narx in turli_narxlari.items() if narx == eng_arzon_narx]
    
    # Eng qimmat reys nomi
    eng_qimmat_reys = [nomi for nomi, narx in turli_narxlari.items() if narx == eng_qimmat_narx]
    
    return eng_arzon_narx, eng_qimmat_narx, eng_arzon_reys, eng_qimmat_reys

turli_narxlari = {
    "Turkish Airlines": 500,
    "Lufthansa": 600,
    "Emirates": 700,
    "Qatar Airways": 400,
    "British Airways": 550
}

eng_arzon_narx, eng_qimmat_narx, eng_arzon_reys, eng_qimmat_reys = flight_ticket_price_comparator(turli_narxlari)

print(f"Eng arzon reys narxi: {eng_arzon_narx}")
print(f"Eng qimmat reys narxi: {eng_qimmat_narx}")
print(f"Eng arzon reys nomi: {', '.join(eng_arzon_reys)}")
print(f"Eng qimmat reys nomi: {', '.join(eng_qimmat_reys)}")
