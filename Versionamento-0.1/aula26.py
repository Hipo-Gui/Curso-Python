""""
Formatação Básica de strings 
s - string 
f - float 
.<número de dígitos>f 
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda 
< - Direita
^ - Centro 
= - Força o número a aparecer antes dos zeros
Sinal - + ou - 
Ex : 0>-100,.1f
conversion flags - !r !s !a
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.12345876487162:0=+10,.1f}')
print(f'O hexadecimal de 1800 é {1800:08X}')
print(f'{variavel!r}')


