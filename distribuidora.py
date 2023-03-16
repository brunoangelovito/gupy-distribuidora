import json
import matplotlib.pyplot as plt

class Distribuidora:
    def __init__(self, faturamento):
        self.faturamento = faturamento

    def menor_valor(self):
        return min(self.faturamento)

    def maior_valor(self):
        return max(self.faturamento)

    def dias_acima_media(self):
        media = sum(self.faturamento) / len(self.faturamento)
        return sum(1 for f in self.faturamento if f > media)

    def plot_faturamento(self):
        dias = range(1, len(self.faturamento) + 1)
        plt.bar(dias, self.faturamento, color='blue')
        media = sum(self.faturamento) / len(self.faturamento)
        plt.axhline(media, color='red', linestyle='--')
        plt.xlabel('Dia do mês')
        plt.ylabel('Faturamento')
        plt.title('Faturamento diário da distribuidora')
        plt.show()

# lê o arquivo JSON com o faturamento diário
with open('dias.json', 'r') as f:
    dados = json.load(f)

# cria um objeto Distribuidora com os dados lidos
dist = Distribuidora(dados['faturamento'])

# calcula as estatísticas de faturamento
menor = dist.menor_valor()
maior = dist.maior_valor()
acima_media = dist.dias_acima_media()

# plota o faturamento diário com a média destacada em vermelho
dist.plot_faturamento()

# imprime as estatísticas de faturamento
print(f"Menor valor: R$ {menor:.2f}")
print(f"Maior valor: R$ {maior:.2f}")
print(f"Dias acima da média: {acima_media}")
