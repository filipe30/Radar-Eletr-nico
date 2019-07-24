carro =float(input('Qual a velocida de do seu carro?'))
if carro > 80:
    multa = (carro - 80) * 7
    print(f'\033[1;31mVoce foi multado em R$ {multa:.2f}!\033[4;33m Dirija com mais atenção! ')

else:
    print('Parabens você é um bom motorista!')