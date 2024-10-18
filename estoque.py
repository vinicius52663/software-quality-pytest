class Estoque:
    def __init__(self):
        self.produtos = [
            {
                "produto": "Pastilha Garoto",
                "grupo": "doces",
                "detalhe": "Pastilha de hortela Garoto 100g",
                "codigo": 12121212,
                "estoque": 20,
                "custo": 3.5,
                "marca": "Garoto"
            },
            {
                "produto": "Chocolate Lacta",
                "grupo": "doces",
                "detalhe": "Chocolate ao leite Lacta 150g",
                "codigo": 12121213,
                "estoque": 15,
                "custo": 4.0,
                "marca": "Lacta"
            },
            {
                "produto": "Refrigerante Coca-Cola",
                "grupo": "bebidas",
                "detalhe": "Refrigerante Coca-Cola 2L",
                "codigo": 12121214,
                "estoque": 30,
                "custo": 5.0,
                "marca": "Coca-Cola"
            },
            {
                "produto": "Suco Del Valle",
                "grupo": "bebidas",
                "detalhe": "Suco Del Valle Laranja 1L",
                "codigo": 12121215,
                "estoque": 25,
                "custo": 3.0,
                "marca": "Del Valle"
            },
            {
                "produto": "Macarrão Nissin",
                "grupo": "alimentos",
                "detalhe": "Macarrão instantâneo Nissin 80g",
                "codigo": 12121216,
                "estoque": 50,
                "custo": 2.0,
                "marca": "Nissin"
            }
        ]
    
    def adicionar_produto(self, produto: dict) -> None:
        if not all(key in produto for key in ["produto", "grupo", "detalhe", "codigo", "estoque", "custo", "marca"]):
            raise ValueError("Produto inválido: Todos os campos são obrigatórios.")
        
        if produto["estoque"] < 0:
            raise ValueError("A quantidade em estoque não pode ser negativa.")
        
        produto_existente = self.buscar_produto(produto["codigo"])
        
        if produto_existente:
            produto_existente["estoque"] += produto["estoque"]
        else:
            self.produtos.append(produto)
    
    def remover_produto(self, codigo: int) -> bool:
        produto = self.buscar_produto(codigo)
        if produto:
            if produto["estoque"] < 5:
                raise ValueError(f"Não é permitido remover o produto {produto['produto']} com estoque baixo.")
            self.produtos = [p for p in self.produtos if p["codigo"] != codigo]
            return True
        return False
    
    def atualizar_estoque(self, codigo: int, quantidade: int) -> bool:
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        
        produto = self.buscar_produto(codigo)
        if produto:
            produto["estoque"] += quantidade
            if produto["estoque"] < 0:
                raise ValueError("O estoque não pode ser negativo.")
            return True
        return False
    
    def buscar_produto(self, codigo: int) -> dict:
        for p in self.produtos:
            if p["codigo"] == codigo:
                return p
    
    def calcular_valor_estoque(self) -> float:
        return sum(p["estoque"] * p["custo"] for p in self.produtos)
    
    def listar_produtos(self) -> list:
        return self.produtos
    
    def filtrar_produtos_por_grupo(self, grupo: str) -> list:
        grupo = grupo.lower()
        return [p for p in self.produtos if p["grupo"].lower() == grupo]
    
    def atualizar_preco_por_produto(self, nome_produto: str, novo_preco: float) -> bool:
        if novo_preco <= 0:
            raise ValueError("O novo preço deve ser maior que zero.")
        
        produto = next((p for p in self.produtos if p["produto"].lower() == nome_produto.lower()), None)
        if produto:
            if novo_preco <= produto["custo"]:
                raise ValueError("O novo preço não pode ser inferior ao custo atual.")
            produto["custo"] = novo_preco
            return True
        else:
            raise ValueError(f"Produto {nome_produto} não encontrado.")