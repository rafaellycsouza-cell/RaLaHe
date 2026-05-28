-- 1. Criação do Banco de Dados
CREATE DATABASE delivery_arabe;
USE delivery_arabe;

-- 2. Criação das Tabelas Independentes (sem chaves estrangeiras)
CREATE TABLE cliente (
    id_cpf CHAR(11) PRIMARY KEY,
    nome_completo VARCHAR(100),
    email VARCHAR(100),
    senha CHAR(8),
    telefone CHAR(11),
    endereco VARCHAR(300)
);

CREATE TABLE restaurante (
    id_restaurante CHAR(3) PRIMARY KEY,
    nome VARCHAR(25),
    cnpj CHAR(18),
    telefone CHAR(14),
    endereco VARCHAR(300),
    horario_funcionamento TIME,
    taxa_entrega DECIMAL(5,2)
);

CREATE TABLE cupom (
    id_cupom VARCHAR(20) PRIMARY KEY,
    codigo CHAR(4),
    desconto DECIMAL(5,2),
    preco DECIMAL(8,2),
    valor_minimo VARCHAR(30)
);

-- 3. Criação das Tabelas Dependentes (com chaves estrangeiras)

-- Cardápio está ligado ao Restaurante
CREATE TABLE cardapio (
    id_item CHAR(4) PRIMARY KEY,
    nome VARCHAR(15),
    descricao VARCHAR(100),
    preco DECIMAL(8,2),
    disponibilidade VARCHAR(7),
    id_restaurante CHAR(3),
    CONSTRAINT fk_cardapio_restaurante 
        FOREIGN KEY (id_restaurante) REFERENCES restaurante(id_restaurante)
);

-- Pedido está ligado ao Cliente, ao Restaurante e ao Cupom
CREATE TABLE pedido (
    id_pedido VARCHAR(15) PRIMARY KEY, -- Corrigido de id_item para id_pedido
    hora TIME,
    codigo CHAR(4),
    status_do_pedido VARCHAR(25),
    valor_total DECIMAL(8,2),
    forma_pagamento VARCHAR(10),
    endereco_entrega VARCHAR(300),
    id_cpf CHAR(11),
    id_restaurante CHAR(3),
    id_cupom VARCHAR(20),
    CONSTRAINT fk_pedido_cliente 
        FOREIGN KEY (id_cpf) REFERENCES cliente(id_cpf),
    CONSTRAINT fk_pedido_restaurante 
        FOREIGN KEY (id_restaurante) REFERENCES restaurante(id_restaurante),
    CONSTRAINT fk_pedido_cupom 
        FOREIGN KEY (id_cupom) REFERENCES cupom(id_cupom)
);

-- Tabela Intermediária (Muitos para Muitos entre Pedido e Cardápio)
CREATE TABLE itens_pedido (
    id_pedido VARCHAR(15),
    id_item CHAR(4),
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(8,2),
    PRIMARY KEY (id_pedido, id_item),
    CONSTRAINT fk_itens_pedido 
        FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
    CONSTRAINT fk_itens_cardapio 
        FOREIGN KEY (id_item) REFERENCES cardapio(id_item)
);