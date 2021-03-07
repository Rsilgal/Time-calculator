def add_time(start, duration, initialDay = None):
    
    h, m, f = time_format_conversion(start)
    
    if h is not None and m is not None and f is not None:
        hi, mi = time_increment_conversion(str(duration))
        h1, m1 = time_conversion(int(h), int(m), f)
        h2, m2, d2 = time_increment(int(h1), int(m1), int(hi), int(mi))
        h3, f3 = time_inversal_conversion(h2)

        if initialDay is None:
            new_time = time_print_date(h3, m2, f3, d2)

        else:
            cd1 = time_current_day(str(initialDay))
            cd2 = time_day_increment(cd1, d2)
            cd3 = time_current_day(cd2, False)
            new_time = time_print_date(h3, m2, f3, d2, cd3)

        return new_time
    else:
        return 'TONTO'

def time_conversion(hora, minutos, formato):
    if formato == 'AM':
        if hora == 12:
            _h = hora - 12
            _m = minutos
        else:
            _h = hora
            _m = minutos
    elif formato == 'PM':
        if hora == 12:
            _h = hora
            _m = minutos
        else:
            _h = hora + 12
            _m = minutos

    return _h,_m

def time_increment(hora, minutos, incrementoHora, incrementoMinutos):
    _h = hora + incrementoHora
    _m = minutos + incrementoMinutos
    _incrementoD = 0
    _incrementoH = 0

    if _m >= 60:
        _incrementoH = _m // 60
        _m = _m - 60
    
    _h = _h + _incrementoH

    if _h >= 24:
        _incrementoD = _h // 24
        _h = _h - (24 * _incrementoD)

    return _h, _m, _incrementoD

def time_format_conversion(cadena):
    if isinstance(cadena, str):
        _tiempoYformato = cadena.split()
        _horaYminuto = _tiempoYformato[0].split(':')
        _h = _horaYminuto[0]
        _m = _horaYminuto[1]
        _f = _tiempoYformato[1]

        return _h, _m, _f

    else:
        return None,None,None

def time_increment_conversion(cadena):
    _t = cadena.split(':')
    return _t[0], _t[1]

def time_inversal_conversion(hora):

    if hora >= 12:
        _f = 'PM'
    else:
        _f = 'AM'

    # Conversión de la hora
    if hora > 12:
        _h = hora - 12
    elif hora == 0:
        _h = 12
    else:
        _h = hora    
    
    return _h, _f

def time_day_increment(diaActual, diaIncrementos):
    _d = diaActual + diaIncrementos

    if _d > 6:
        _d = _d - (_d // 6) * 7

    return _d

def time_current_day(dia, zeroDay = True):
    _dictDay = {
        'monday': 0,
        'tuesday': 1,
        'wednesday' : 2,
        'thursday' : 3,
        'friday' : 4,
        'saturday' : 5,
        'sunday' : 6
    }
    _d = str(dia).lower()

    if zeroDay:
        return _dictDay[_d]
    else:
        return list(_dictDay.keys())[dia].capitalize()

def time_print_date(hora, minuto, formato, nDias, diaFinal = ''):
    cadena = ''
    cadena += str(hora)
    cadena += ':'
    cadena += str(minuto).zfill(2)
    cadena += ' '
    cadena += str(formato)

    if diaFinal != '':
        cadena += ', '
        cadena += str(diaFinal)

    if nDias != 0:
        cadena += ' ('
        if nDias == 1:
            cadena += 'next day)'
        else:
            cadena += str(nDias)
            cadena += ' days later)'

    return cadena
