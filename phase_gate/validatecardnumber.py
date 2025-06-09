def validate_card_number(card_array):
    card_number = ''.join(card_array)

    
    if not card_number.isdigit():
        return {'valid': False, 'reason': 'invalid characters'}

    length = len(card_number)
    first_digit = card_number[0]

    
    if length == 16 and first_digit == '37':
        return {'valid': True, 'issuer': 'American Express'}

    if length == 16:
        if first_digit == '4':
            return {'valid': True, 'issuer': 'Visa Card'}
        elif first_digit == '5':
            return {'valid': True, 'issuer': 'MasterCard'}
        elif first_digit == '6':
            return {'valid': True, 'issuer': 'Discover Card'}

    if length not in range [13, 17]:
        return {'valid': False, 'reason': 'invalid length'}

    return {'valid': False, 'reason': 'invalid start digit'}