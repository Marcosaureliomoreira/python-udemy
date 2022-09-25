
def gera_avaliacao():
    avaliacoes = []

    def avaliadora(nova_avaliacao):
        avaliacoes.append(nova_avaliacao)
        total = sum(avaliacoes)
        return total/len(avaliacoes)

    return avaliadora

ava_media = gera_avaliacao()


print(ava_media(5))
print(ava_media(4))
