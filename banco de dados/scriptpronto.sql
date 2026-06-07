-- 1. Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS delivery_arabe;
USE delivery_arabe;

-- 2. Criação das Tabelas Independentes
CREATE TABLE cliente (
    id_cpf CHAR(11) PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL, -- Alinhado com o input de login do base.html
    nome_completo VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,          -- Expandido para suportar hash de criptografia seguro
    telefone CHAR(11),
    endereco VARCHAR(300),
    bairro VARCHAR(50)                    -- Adicionado para capturar o select de Joinville do HTML
);

CREATE TABLE restaurante (
    id_restaurante CHAR(3) PRIMARY KEY,
    nome VARCHAR(50),                     -- Aumentado para nomes mais robustos
    cnpj CHAR(18) UNIQUE,
    telefone CHAR(14),
    endereco VARCHAR(300),
    horario_funcionamento TIME,
    taxa_entrega DECIMAL(5,2)
);

CREATE TABLE cupom (
    id_cupom VARCHAR(20) PRIMARY KEY,
    codigo CHAR(10) UNIQUE,               -- Códigos promocionais costumam ser maiores
    desconto DECIMAL(5,2),
    preco DECIMAL(8,2),
    valor_minimo DECIMAL(8,2)             -- Alterado para DECIMAL para permitir cálculos numéricos de validação
);

-- 3. Criação das Tabelas Dependentes

CREATE TABLE cardapio (
    id_item CHAR(4) PRIMARY KEY,
    nome VARCHAR(100),                    -- Expandido para evitar truncamento de pratos gourmet
    descricao VARCHAR(255),               -- Aumentado para descrições mais detalhadas e apetitosas
    preco DECIMAL(8,2),
    disponibilidade VARCHAR(15),          -- Aumentado preventivamente
    id_restaurante CHAR(3),
    CONSTRAINT fk_cardapio_restaurante 
        FOREIGN KEY (id_restaurante) REFERENCES restaurante(id_restaurante) ON DELETE CASCADE
);

CREATE TABLE pedido (
    id_pedido VARCHAR(15) PRIMARY KEY, 
    hora TIME,
    codigo CHAR(4),
    status_do_pedido VARCHAR(50),         -- Aumentado para acomodar atualizações complexas de status
    valor_total DECIMAL(8,2),
    forma_pagamento VARCHAR(20),          -- Aumentado para termos como "cartao_credito"
    endereco_entrega VARCHAR(300),
    id_cpf CHAR(11),
    id_restaurante CHAR(3),
    id_cupom VARCHAR(20),
    CONSTRAINT fk_pedido_cliente 
        FOREIGN KEY (id_cpf) REFERENCES cliente(id_cpf),
    CONSTRAINT fk_pedido_restaurante 
        FOREIGN KEY (id_restaurante) REFERENCES restaurante(id_restaurante),
    CONSTRAINT fk_pedido_cupom 
        FOREIGN KEY (id_cupom) REFERENCES cupom(id_cupom) ON DELETE SET NULL
);

CREATE TABLE itens_pedido (
    id_pedido VARCHAR(15),
    id_item CHAR(4),
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(8,2),
    PRIMARY KEY (id_pedido, id_item),
    CONSTRAINT fk_itens_pedido 
        FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    CONSTRAINT fk_itens_cardapio 
        FOREIGN KEY (id_item) REFERENCES cardapio(id_item)
);