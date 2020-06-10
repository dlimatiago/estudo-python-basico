def pyhelp():
    from time import sleep as pausa
    while True:
        print("""\033[31m
        ▲▲▲▲▲▲▲▲▲▲▲▲     
           PyHelp
        ▼▼▼▼▼▼▼▼▼▼▼▼   
              \033[m""")
        style = {'N': '\033[1m',
                 'Inv': '\033[30;7m',
                 'verm': '\033[31m',
                 'Nazul': '\033[1;34m',
                 'Nverd': '\033[1;4;32m',
                 'Namar': '\033[1;33m',
                 'Ncia': '\033[1;36m',
                 'Nmag': '\033[1;35m',
                 'fecha': '\033[m'}
        bi = ("""
        abs, delattr, hash,
        memoryview, set, all,
        dict, help, min,
        setattr, any, dir, 
        hex, next, slice, 
        ascii, divmod, id, 
        object, sorted, bin, 
        enumerate, input, oct, 
        staticmethod, bool, eval, 
        int, open, str, breakpoint, exec,
        isinstance, ord, sum,
        bytearray, filter, issubclass,
        pow, super, bytes,
        float, iter, print,
        tuple, callable, format,
        len, property, type,
        chr, frozenset, list, 
        range, vars, classmethod,
        getattr, locals, repr,
        zip, compile, globals,
        map, reversed, import,
        complex, hasattr, max, round""")  # This tuple contains all the built-ins functions

        pick = str(input(f'{style["N"]}função ou biblioteca ► {style["fecha"]}')).strip().lower()
        if pick == 'fim':
            print(f'{style["Nmag"]}Finalizando ⌛{style["fecha"]}')
            pausa(1)
            print(f'{style["Inv"]}Até a próxima ✌!{style["fecha"]}')
            break

        f = pick in bi  # Checks if pick is a built-in fuction
        text = "função ƒ "if f else "biblioteca ❏ "  # Select the icon. ƒ for function and ❏ for library

        print(f'{style["Ncia"]}  ➥ Procurando o manual da {style["fecha"]}{style["Nverd"]}{text}{pick}{style["fecha"]}')
        pausa(1.2)
        print(f'{style["Namar"]}        ➥ Carregando manual:{style["fecha"]} ', end='')

        for x in range(20):  # Shows a loading bar
            print(f'{style["verm"]}▊{style["fecha"]}', end='')
            pausa(.1)
        print()

        print(f'{style["Nazul"]}              ➥ Manual da {style["fecha"]}{style["Nverd"]}{text}{pick}{style["fecha"]}')
        pausa(.5)
        print(f'{style["Inv"]}☛', end=' ')
        help(pick)


# Main Code
pyhelp()
