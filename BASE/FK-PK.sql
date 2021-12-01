ALTER TABLE Categoria ADD PRIMARY KEY (id_cat);
ALTER TABLE Producto ADD PRIMARY KEY (id_prod);
ALTER TABLE Locall ADD PRIMARY KEY (id_loc);
ALTER TABLE Marca ADD PRIMARY KEY (id_marc);
ALTER TABLE Venta_diaria ADD PRIMARY KEY (cod_ven);
ALTER TABLE Proveedor ADD PRIMARY KEY (rut);
ALTER TABLE Bodega ADD PRIMARY KEY (id_bod);

ALTER TABLE clasificacion_productos
    ADD CONSTRAINT fk_cat FOREIGN KEY (id_cat)
	REFERENCES Categoria(id_cat);
    
ALTER TABLE clasificacion_productos
    ADD CONSTRAINT fk_prod_cla FOREIGN KEY (id_prod)
	REFERENCES Producto(id_prod);
    
ALTER TABLE stock_local
    ADD CONSTRAINT fk_prod_st FOREIGN KEY (id_prod)
	REFERENCES Producto(id_prod);
    
ALTER TABLE stock_local
    ADD CONSTRAINT fk_loc FOREIGN KEY (id_loc)
	REFERENCES locall(id_loc);
    
ALTER TABLE venta_diaria
    ADD CONSTRAINT fk_loc_ven FOREIGN KEY (id_loc)
	REFERENCES locall(id_loc);
    
ALTER TABLE producto_vendido
    ADD CONSTRAINT fk_ven FOREIGN KEY (cod_ven)
	REFERENCES venta_diaria(cod_ven);

ALTER TABLE producto_vendido
    ADD CONSTRAINT fk_prod_ven FOREIGN KEY (id_prod)
	REFERENCES producto(id_prod);
    
ALTER TABLE  stock_bodega
    ADD CONSTRAINT fk_bod FOREIGN KEY (id_bod)
	REFERENCES bodega(id_bod);
    
ALTER TABLE stock_bodega
    ADD CONSTRAINT fk_prod FOREIGN KEY (id_prod)
	REFERENCES producto(id_prod);