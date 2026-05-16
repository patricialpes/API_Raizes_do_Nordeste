CREATE DATABASE rede_raizes_do_nordeste;
USE rede_raizes_do_nordeste;


-- CADASTRO DE USUÁRIOS

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(255),
    perfil ENUM('CLIENTE', 'ADMIN', 'GERENTE')
);

INSERT INTO usuarios (id, nome, email, senha, perfil) VALUES
(1,'Ana Souza','ana@gmail.com','123','CLIENTE'),
(2,'Carlos Lima','carlos@gmail.com','123','CLIENTE'),
(3,'Maria Heloisa','maria@gmail.com','123','CLIENTE'),
(4,'João Pedro','joao@gmail.com','123','CLIENTE'),
(5,'Fernanda Alves','fernanda@gmail.com','123','CLIENTE'),
(6,'Bruno Costa','bruno@gmail.com','123','CLIENTE'),
(7,'Patricia Gomes','patricia@gmail.com','123','GERENTE'),
(8,'Ricardo Souza','ricardo@gmail.com','123','ADMIN'),
(9,'Juliana Rocha','juliana@gmail.com','123','CLIENTE'),
(10,'Lucas Martins','lucas@gmail.com','123','CLIENTE'),
(11,'Camila Freitas','camila@gmail.com','123','CLIENTE'),
(12,'Rafael Dias','rafael@gmail.com','123','CLIENTE');


-- UNIDADE

CREATE TABLE unidade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255) NOT NULL
);

INSERT INTO unidade (id, nome, endereco) VALUES
(1,'Unidade Centro','Rua Pedro Porpino, 100'),
(2,'Unidade Norte','Rua Barão de Cametá, 200'),
(3,'Unidade Sul','Rua Santa Rita de Cassia, 300'),
(4,'Unidade Leste','Rua Barão do Rio Branco, 400'),
(5,'Unidade Oeste','Rua E, 500'),
(6,'Unidade Belém','Av. Nazaré, 600'),
(7,'Unidade Castanhal','Av. Central, 700'),
(8,'Unidade Ananindeua','Rua F, 800'),
(9,'Unidade Marituba','Rua G, 900'),
(10,'Unidade Mosqueiro','Rua H, 1000'),
(11,'Unidade Icoaraci','Rua I, 1100'),
(12,'Unidade Bragança','Av Presidente Vargas, 1200');


-- PRODUTOS

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    estoque INT
);

INSERT INTO produtos (id, nome, preco, estoque) VALUES
(1,'Cuscuz',8.00,50),
(2,'Coca cola',5.00,30),
(3,'Bolo de Cenoura',5.00,20),
(4,'Acarajé',10.00,40),
(5,'Tapioca',8.00,60),
(6,'Empada',6.00,25),
(7,'Hamburguer',20.00,15),
(8,'Coxinha',4.00,70),
(9,'Pamonha',6.50,80),
(10,'Canjica',5.00,90),
(11,'Bolo de Milho',9.00,45),
(12,'Café Expresso',4.00,100);


-- PEDIDOS

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    unidade_id INT,
    canal ENUM('APP','TOTEM','BALCAO','PICKUP','WEB'),
    status VARCHAR(50),
    total DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (unidade_id) REFERENCES unidade(id)
);

INSERT INTO pedidos (id, usuario_id, unidade_id, canal, status, total) VALUES
(1,1,1,'APP','FINALIZADO',16.00),
(2,2,2,'WEB','PENDENTE',5.00),
(3,3,3,'BALCAO','FINALIZADO',5.00),
(4,4,4,'TOTEM','CANCELADO',30.00),
(5,5,5,'APP','FINALIZADO',32.00),
(6,6,6,'WEB','PENDENTE',12.00),
(7,7,7,'BALCAO','FINALIZADO',20.00),
(8,8,8,'APP','FINALIZADO',20.00),
(9,9,9,'TOTEM','PENDENTE',13.00),
(10,10,10,'WEB','FINALIZADO',15.00),
(11,11,11,'APP','FINALIZADO',9.00),
(12,12,12,'BALCAO','FINALIZADO',24.00);


-- ITENS DO PEDIDO

CREATE TABLE itens_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    preco_unitario DECIMAL(10,2),

    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

INSERT INTO itens_pedido (id, pedido_id, produto_id, quantidade, preco_unitario) VALUES
(1,1,1,2,8.00),
(2,2,2,1,5.00),
(3,3,3,1,5.00),
(4,4,4,3,10.00),
(5,5,5,4,8.00),
(6,6,6,2,6.00),
(7,7,7,1,20.00),
(8,8,8,5,4.00),
(9,9,9,2,6.50),
(10,10,10,3,5.00),
(11,11,11,1,9.00),
(12,12,12,6,4.00);


-- FORMAS DE PAGAMENTO

CREATE TABLE pagamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL UNIQUE,
    status ENUM('APROVADO', 'RECUSADO') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_pagamento_pedido
        FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
        ON DELETE CASCADE
);

INSERT INTO pagamento (id, pedido_id, status) VALUES
(1,1,'APROVADO'),
(2,2,'RECUSADO'),
(3,3,'APROVADO'),
(4,4,'RECUSADO'),
(5,5,'APROVADO'),
(6,6,'RECUSADO'),
(7,7,'APROVADO'),
(8,8,'APROVADO'),
(9,9,'RECUSADO'),
(10,10,'APROVADO'),
(11,11,'APROVADO'),
(12,12,'APROVADO');


--  FIDELIDADE POR CLIENTE

CREATE TABLE fidelidade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL UNIQUE,
    pontos INT DEFAULT 0,

    CONSTRAINT fk_fidelidade_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        ON DELETE CASCADE
);

INSERT INTO fidelidade (id, usuario_id, pontos) VALUES
(1,1,100),
(2,2,50),
(3,3,200),
(4,4,30);