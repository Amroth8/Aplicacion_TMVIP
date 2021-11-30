CREATE DATABASE TODOMARKET_VIP;

CREATE TABLE Categoria (
	id_cat int not null auto_increment,
    nom varchar(100)
);

CREATE TABLE Producto (
	id_prod int not null auto_increment,
    nom varchar(100),
    cant int,
    cod_bar bigint,
    prec int,
    id_marc int
);


CREATE TABLE Clasificacion_Productos (
	id_cat int not null,
    id_prod int not null
);

CREATE TABLE Marca (
	id_marc int not null auto_increment,
    nom varchar(100)
);

CREATE TABLE Locall (
	id_loc int not null,
    nom varchar(100),
    direc varchar(100)
);

CREATE TABLE Stock_Local(
	id_prod int not null,
    id_loc int not null,
    cant int
);

CREATE TABLE Venta_diaria(
	cod_ven int not null,
    fecha date,
    hora time,
    mon_tot int,
    id_loc int
);

CREATE TABLE Producto_vendido (
	id_prod int,
    cant int,
    cod_ven int
);

CREATE TABLE Proveedor (
	rut varchar(100) not null,
    nomp varchar (100),
    direcp varchar (100),
    mail varchar(100),
    tel varchar(100)
);

CREATE TABLE Bodega (
	id_bod int,
    direcb varchar(100)
);

CREATE TABLE Stock_bodega(
	id_prod int,
    id_bod int,
    cant int
);

CREATE TABLE Catalogo_proveedores (
	rut varchar(100) not null,
    id_prod int
);

