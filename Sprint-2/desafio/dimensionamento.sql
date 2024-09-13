CREATE VIEW fato_locacao AS
SELECT 
    l.id_locacao AS idLocacao,
    l.id_cliente AS idCliente,
    l.id_carro AS idCarro,
    l.id_vendedor AS idVendedor,
    l.data_locacao AS dataLocacao,
    l.hora_locacao AS horaLocacao,
    l.qtd_diaria AS qtdDiaria,
    l.vlr_diaria AS vlrDiaria,
    l.data_entrega AS dataEntrega,
    l.hora_entrega AS horaEntrega,
    d.data_completa
FROM tb_locacao l
JOIN dim_datas d ON d.data_completa = l.data_entrega;



CREATE VIEW dim_cliente AS
SELECT 
    id_cliente AS idCliente,
    nome_cliente AS nomeCliente,
    cidade_cliente AS cidadeCliente,
    estado_cliente AS estadoCliente,
    pais_cliente AS paisCliente
FROM tb_cliente;


CREATE VIEW dim_carro AS
SELECT 
    c.id_carro AS idCarro,
    c.km_carro AS kmCarro,
    c.classi_carro AS classiCarro,
    c.marca_carro AS marcaCarro,
    c.modelo_carro AS modeloCarro,
    c.ano_carro AS anoCarro,
    c.id_combustivel AS idCombustivel,
    co.tipo_combustivel AS tipoCombustivel
FROM tb_carro c
JOIN tb_combustivel co ON c.id_combustivel = co.id_combustivel;


CREATE VIEW dim_vendedor AS
SELECT 
    id_vendedor AS idVendedor,
    nome_vendedor AS nomeVendedor,
    sexo_vendedor AS sexoVendedor,
    estado_vendedor AS estadoVendedor
FROM tb_vendedor;



CREATE VIEW dim_datas AS
SELECT DISTINCT 
    data_entrega AS data_completa,
    SUBSTR(CAST(data_entrega AS TEXT), 1, 4) AS ano, 
    SUBSTR(CAST(data_entrega AS TEXT), 5, 2) AS mes, 
    SUBSTR(CAST(data_entrega AS TEXT), 7, 2) AS dia,
    CASE strftime('%w', substr(data_entrega, 1, 4) || '-' || substr(data_entrega, 5, 2) || '-' || substr(data_entrega, 7, 2))
        WHEN '0' THEN 'domingo'
        WHEN '1' THEN 'segunda'
        WHEN '2' THEN 'terça'
        WHEN '3' THEN 'quarta'
        WHEN '4' THEN 'quinta'
        WHEN '5' THEN 'sexta'
        WHEN '6' THEN 'sábado'
    END AS dia_da_semana,
    CASE
        WHEN SUBSTR(data_entrega, 5, 2) BETWEEN '01' AND '03' THEN '1'
        WHEN SUBSTR(data_entrega, 5, 2) BETWEEN '04' AND '06' THEN '2'
        WHEN SUBSTR(data_entrega, 5, 2) BETWEEN '07' AND '09' THEN '3'
        WHEN SUBSTR(data_entrega, 5, 2) BETWEEN '10' AND '12' THEN '4'
    END AS trimestre
FROM tb_locacao;








	   