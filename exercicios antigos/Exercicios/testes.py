try:
    a = int(input())
    b = int(input())
    div = a/b

except (KeyboardInterrupt):

    print(f'O usuario n quis mais')

else:
    print(f'Resultado: {div}')