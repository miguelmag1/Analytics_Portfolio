-- Creando tabla de afiliados
CREATE TABLE "AFILIADOS" (
	"TIP_IDENTIFICACION_EMPRESA"	varchar(100),
	"NUM_IDENTIFICACION_EMPRESA"	varchar(100),
	"NUM_IDENT_ANONIMIZADO"	varchar(100),
	"TIP_IDENTIFICACION_AFILIADO"	varchar(100),
	"NUM_ID_AFILIADO"	varchar(100),
	"FEC_NACIMIENTO"	date,
	"GENERO_CCF"	varchar(100),
	"NIVEL_ESCOLARIDAD"	varchar(100),
	"ESTADO_CIVIL"	varchar(100),
	"TIP_AFILIADO"	varchar(100),
	"CATEGORIA_CCF"	varchar(100)
);
-- visualizando tabla de afiliados
SELECT * from AFILIADOS;

-- Creando tabla de empresa o aportantes 

CREATE TABLE IF NOT EXISTS "EmpresaAportantes"(
	"TIP_IDENTIFICACION" varchar(100),
	"NUM_IDENTIFICACION" varchar(100),
	"NUM_IDENT_ANONIMIZADO" varchar(100),
	"COD_MUNICIPIO_DANE" varchar(100),
	"EST_VINCULACION" varchar(100),
	"TIP_APORTANTE" varchar(100),
	"TIP_SECTOR" varchar(100),
	"ACT_ECONOMICA" varchar(100),
	"APO_TOTAL_MENSUAL" integer
);

-- CREANDO TABLA PACS

CREATE TABLE IF NOT EXISTS "PACS" (
  "TIP_IDENTIFICACION_EMPRESA" varchar(100),
  "NUM_IDENT_EMPRESA_ANONIMIZADO" varchar(100),
  "TIP_IDENTIFICACION_AFILIADO" varchar(100),
  "NUM_IDENT_AFILIADO_ANONIMIZADO" varchar(100),
  "TIP_IDENTIFICACION_PERSONA_A_CARGO" varchar(100),
  "NUM_PAC_ANONIMIZADO" varchar(100),
  "FEC_NACIMIENTO_PERSONA_A_CARGO" date,
  "GEN_PERSONA_A_CARGO" varchar(100),
  "PAR_PERSONA_A_CARGO" varchar(100)
);

-- Creando tabla con valores unicos de NUM_IDENT_ANONIMIZADO y valores de interes
CREATE TEMPORARY TABLE  AFILIADOS3 AS 
SELECT DISTINCT NUM_IDENT_ANONIMIZADO, NUM_IDENTIFICACION_EMPRESA, FEC_NACIMIENTO, NUM_ID_AFILIADO
FROM AFILIADOS;

-- Creando tabla EmpresaAportantes con valores unicos 
CREATE TEMPORARY TABLE  EmpresaAportantes3 AS 
SELECT DISTINCT NUM_IDENT_ANONIMIZADO, NUM_IDENTIFICACION , COD_MUNICIPIO_DANE, APO_TOTAL_MENSUAL
FROM EmpresaAportantes;

SELECT *
FROM AFILIADOS3
WHERE NUM_IDENT_ANONIMIZADO="222060794";

SELECT DISTINCT NUM_IDENT_ANONIMIZADO, NUM_IDENTIFICACION , COD_MUNICIPIO_DANE, APO_TOTAL_MENSUAL
FROM EmpresaAportantes3
WHERE NUM_IDENTIFICACION="900427040";

-- haciendo join entre tablas AFILIADOS3 y EmpresaAportantes3

CREATE TEMPORARY TABLE TBCONSULTA3 AS 
SELECT A.NUM_IDENT_ANONIMIZADO, A.NUM_IDENTIFICACION_EMPRESA, A.FEC_NACIMIENTO, A.NUM_ID_AFILIADO, EA.NUM_IDENT_ANONIMIZADO, EA.NUM_IDENTIFICACION , EA.COD_MUNICIPIO_DANE, EA.APO_TOTAL_MENSUAL
FROM AFILIADOS3 AS A
LEFT JOIN EmpresaAportantes3 AS EA
ON A.NUM_IDENT_ANONIMIZADO = EA.NUM_IDENT_ANONIMIZADO;

SELECT* FROM TBCONSULTA3;

CREATE TEMPORARY TABLE  CONSULTA3_EXP AS
SELECT DISTINCT NUM_IDENT_ANONIMIZADO|| NUM_ID_AFILIADO AS IDENTIFICADOR ,NUM_IDENT_ANONIMIZADO, NUM_IDENTIFICACION_EMPRESA, FEC_NACIMIENTO, NUM_ID_AFILIADO, NUM_IDENT_ANONIMIZADO, NUM_IDENTIFICACION , COD_MUNICIPIO_DANE, APO_TOTAL_MENSUAL
FROM TBCONSULTA3;

SELECT * FROM CONSULTA3_EXP;