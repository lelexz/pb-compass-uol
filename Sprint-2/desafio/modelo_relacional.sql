-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `locacao` (
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

CREATE TABLE `cliente` (
    `idCliente` int  NOT NULL ,
    `nomeCliente` varchar  NOT NULL ,
    `cidadeCliente` varchar  NOT NULL ,
    `estadoCliente` varchar  NOT NULL ,
    `paisCliente` varchar  NOT NULL ,
    PRIMARY KEY (
        `idCliente`
    )
);

CREATE TABLE `carro` (
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

CREATE TABLE `combustivel` (
    `idCombustivel` int  NOT NULL ,
    `tipoCombustivel` int  NOT NULL ,
    PRIMARY KEY (
        `idCombustivel`
    )
);

CREATE TABLE `vendedor` (
    `idVendedor` int  NOT NULL ,
    `nomeVendedor` varchar  NOT NULL ,
    `sexoVendedor` smallint  NOT NULL ,
    `estadoVendedor` varchar  NOT NULL ,
    PRIMARY KEY (
        `idVendedor`
    )
);

ALTER TABLE `cliente` ADD CONSTRAINT `fk_cliente_idCliente` FOREIGN KEY(`idCliente`)
REFERENCES `locacao` (`idCliente`);

ALTER TABLE `carro` ADD CONSTRAINT `fk_carro_idCarro` FOREIGN KEY(`idCarro`)
REFERENCES `locacao` (`idCarro`);

ALTER TABLE `combustivel` ADD CONSTRAINT `fk_combustivel_tipoCombustivel` FOREIGN KEY(`tipoCombustivel`)
REFERENCES `carro` (`idCombustivel`);

ALTER TABLE `vendedor` ADD CONSTRAINT `fk_vendedor_idVendedor` FOREIGN KEY(`idVendedor`)
REFERENCES `locacao` (`idVendedor`);

