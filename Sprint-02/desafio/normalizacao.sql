
CREATE TABLE tb_locacao (
    id_locacao INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_carro INTEGER,
    km_carro INTEGER,
    id_vendedor INTEGER,
    id_combustivel INTEGER,
    data_locacao DATETIME,
    hora_locacao TIME,
    qtd_diaria INTEGER,
    vlr_diaria DECIMAL,
    data_entrega DATE,
    hora_entrega TIME,
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente(id_cliente),
    FOREIGN KEY (id_carro) REFERENCES tb_carro(id_carro),
    FOREIGN KEY (id_vendedor) REFERENCES tb_vendedor(id_vendedor)
);
INSERT OR REPLACE INTO tb_locacao(id_locacao, id_cliente, id_carro, id_vendedor, id_combustivel,
					   data_locacao, hora_locacao, qtd_diaria, vlr_diaria, data_entrega, hora_entrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, idcombustivel, dataLocacao, horaLocacao,
	   qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao_original;



CREATE TABLE tb_cliente (
    id_cliente INTEGER PRIMARY KEY,
    nome_cliente VARCHAR(15),
    cidade_cliente VARCHAR(40),
    estado_cliente VARCHAR(18),
    pais_cliente VARCHAR(20),
    id_localizacao INTEGER,
);

INSERT OR REPLACE INTO tb_cliente(id_cliente, nome_cliente, cidade_cliente,
					   estado_cliente, pais_cliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao_original;



CREATE TABLE tb_carro (
    id_carro INTEGER PRIMARY KEY,
    km_carro INTEGER,
    classi_carro VARCHAR(20),
    marca_carro VARCHAR(15),
    modelo_carro VARCHAR(20),
    ano_carro INTEGER,
    id_combustivel INTEGER,
	FOREIGN KEY (id_combustivel) REFERENCES tb_combustivel(id_combustivel)
);

INSERT OR REPLACE INTO tb_carro(id_carro, km_carro, classi_carro, marca_carro, modelo_carro,
								ano_carro, id_combustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao_original;



CREATE TABLE tb_combustivel (
    id_combustivel INTEGER PRIMARY KEY,
    tipo_combustivel VARCHAR(10)
);

INSERT OR REPLACE INTO tb_combustivel(id_combustivel, tipo_combustivel)
SELECT idcombustivel, tipoCombustivel FROM tb_locacao_original;



CREATE TABLE tb_vendedor (
    id_vendedor INTEGER PRIMARY KEY,
    nome_vendedor VARCHAR(15),
    sexo_vendedor SMALLINT,
    estado_vendedor VARCHAR(40)
);

INSERT OR REPLACE INTO tb_vendedor(id_vendedor, nome_vendedor, sexo_vendedor, estado_vendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor FROM tb_locacao_original;
