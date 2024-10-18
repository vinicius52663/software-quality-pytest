import pytest
from estoque import Estoque

@pytest.fixture
def estoque():
    return Estoque()

def test_adicionar_produto(estoque):
    novo_produto = {
        "produto": "Achocolatado Toddynho",
        "grupo": "bebidas",
        "detalhe": "Achocolatado líquido Toddynho 200ml",
        "codigo": 12121217,
        "estoque": 40,
        "custo": 1.5,
        "marca": "Toddynho"
    }
    estoque.adicionar_produto(novo_produto)
    assert len(estoque.produtos) == 6

def test_remover_produto(estoque):
    assert estoque.remover_produto(12121212)
    assert len(estoque.produtos) == 4

def test_atualizar_estoque(estoque):
    assert estoque.atualizar_estoque(12121212, 50)
    assert estoque.buscar_produto(12121212)["estoque"] == 70

def test_buscar_produto(estoque):
    produto = estoque.buscar_produto(12121213)
    assert produto["produto"] == "Chocolate Lacta"

def test_calcular_valor_estoque(estoque):
    valor_total = estoque.calcular_valor_estoque()
    assert valor_total == 455.0

def test_listar_produtos(estoque):
    produtos = estoque.listar_produtos()
    assert len(produtos) == 5

def test_filtrar_produtos_por_grupo(estoque):
    produtos_doces = estoque.filtrar_produtos_por_grupo("doces")
    assert len(produtos_doces) == 2

def test_atualizar_preco_por_produto(estoque):
    estoque.atualizar_preco_por_produto("Pastilha Garoto", 4.0)
    produto = estoque.buscar_produto(12121212)
    assert produto["custo"] == 4.0