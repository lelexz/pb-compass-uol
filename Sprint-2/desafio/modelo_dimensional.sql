-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `fato_locacao` (
    `idLocacao` int  NOT NULL ,
    `idCliente` int  NOT NULL ,
    `idCarro` int  NOT NULL ,
    `idVendedor` int  NOT NULL ,
    `dataLocacao` datetime  NOT NULL ,
    `horaLocacao` time  NOT NULL ,
    `qtdDiaria` int  NOT NULL ,
    `vlrDiaria` decimal  NOT NULL ,
    `dataEntrega` date  NOT NULL ,
    `horaEntrega` time  NOT NULL ,
    PRIMARY KEY (
        `idLocacao`
    )
);

CREATE TABLE `dim_cliente` (
    `idCliente` int  NOT NULL ,
    `nomeCliente` varchar  NOT NULL ,
    `cidadeCliente` varchar  NOT NULL ,
    `estadoCliente` varchar  NOT NULL ,
    `paisCliente` varchar  NOT NULL ,
    PRIMARY KEY (
        `idCliente`
    )
);

CREATE TABLE `dim_carro` (
    `idCarro` int  NOT NULL ,
    `kmCarro` int  NOT NULL ,
    `classiCarro` varchar  NOT NULL ,
    `marcaCarro` varchar  NOT NULL ,
    `modeloCarro` varchar  NOT NULL ,
    `anoCarro` int  NOT NULL ,
    `idCombustivel` int  NOT NULL ,
    PRIMARY KEY (
        `idCarro`
    )
);

CREATE TABLE `dim_combustivel` (
    `idCombustivel` int  NOT NULL ,
    `tipoCombustivel` int  NOT NULL ,
    PRIMARY KEY (
        `idCombustivel`
    )
);

CREATE TABLE `dim_vendedor` (
    `idVendedor` int  NOT NULL ,
    `nomeVendedor` varchar  NOT NULL ,
    `sexoVendedor` smallint  NOT NULL ,
    `estadoVendedor` varchar  NOT NULL ,
    PRIMARY KEY (
        `idVendedor`
    )
);

ALTER TABLE `fato_locacao` ADD CONSTRAINT `fk_fato_locacao_idCliente` FOREIGN KEY(`idCliente`)
REFERENCES `dim_cliente` (`idCliente`);

ALTER TABLE `fato_locacao` ADD CONSTRAINT `fk_fato_locacao_idCarro` FOREIGN KEY(`idCarro`)
REFERENCES `dim_carro` (`idCarro`);

ALTER TABLE `fato_locacao` ADD CONSTRAINT `fk_fato_locacao_idVendedor` FOREIGN KEY(`idVendedor`)
REFERENCES `dim_vendedor` (`idVendedor`);

ALTER TABLE `dim_carro` ADD CONSTRAINT `fk_dim_carro_idCombustivel` FOREIGN KEY(`idCombustivel`)
REFERENCES `dim_combustivel` (`idCombustivel`);

