# pip install mysql-connector-python
import mysql.connector

con = mysql.connector.connect(
    host ='localhost',
    port =3306,
    user ='root',
    password ='*****',
    )
cur = con.cursor()

exp_sql0 = """ create  database empresa """
cur.execute(exp_sql0)

exp_sql1 = '''
  create table if not exists departamentos (
  id integer not null primary key,
  nome varchar(20));
'''
cur.execute(exp_sql1)

exp_sql2 = '''
  CREATE TABLE if not exists funcionarios(
  codigo DECIMAL(5) NOT NULL PRIMARY KEY,
  nome VARCHAR(30) NOT NULL,
  rg DECIMAL(9) NOT NULL UNIQUE,
  sexo CHAR(1) CHECK(sexo in ("M","F")),
  depto INTEGER,
  endereco VARCHAR(50),
  cidade VARCHAR(50) DEFAULT "Sao Paulo",
  salario DECIMAL(10,2),
  FOREIGN KEY (depto) REFERENCES departamentos(id));
'''
cur.execute(exp_sql2)

exp_sql3 = '''
  create table if not exists competencias(
  id INTEGER not null ,
  nome varchar(30) not null,
  area varchar(30) check(area in("ENGENHARIA","PRODUCAO","MARKETING","VENDAS","OUTRA")),
  primary key (id) );
'''
cur.execute(exp_sql3)

exp_sql4 = '''
  create table if not exists funcionarios_competencias(
  codigo decimal(5) references funcionarios(codigo),
  id decimal(5) references competencias(id),
  data date not null);
'''
cur.execute(exp_sql4)

exp_sql5 = '''alter table competencias modify column id integer not null auto_increment'''
cur.execute(exp_sql5)

exp_sql6 = '''INSERT INTO departamentos(id,nome) VALUES
(1,"Produção"),(2,"Vendas"),(3,"Compras"),(4,"Marketing"),(5,"Informática");'''
cur.execute(exp_sql6)
con.commit()

exp_sql7 = '''INSERT INTO funcionarios(codigo,nome,rg,sexo,depto,endereco,cidade,salario) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'''
registros = [
    (1001,'José da Silva', 111111,"M",1,"Rua Campos,123","São Paulo", 1900.90),
    (1002,'Maria de Almeida', 222222,"F",2,"Rua Vales,124","São Bernardo", 2300.90),
    (1003,'João de Carvalho', 333333,"M",3,"Rua Escarpas,125","Rio de Janeiro", 900.90),
    (1004,'Lúcia de Barros', 444444,"F",4,"Rua Morros,129","Teresina", 3900.90),
    (1005,'José de Lima', 555555,"M",1,"Rua Montanha,126","Campinas", 2800.90),
]
for registro in registros:
    cur.execute(exp_sql7,registro)
con.commit()

exp_sql8 = '''INSERT INTO competencias(nome,area) Values
( "Configurar linha de Produção", "PRODUÇÃO"),
( "Elaborar Plano de Marketing", "MARKETING"),
( "Vender para Mercosul", "VENDAS"),
( "Realizar a manutenção da LP", "PRODUÇÃO"),
( "Operar CAD e CAM", "ENGENHARIA");'''
cur.execute(exp_sql8)
con.commit()

exp_sql9 = '''INSERT INTO funcionarios_competencias(codigo,id,data) values
(1001, 1, '2022-10-10'),
(1002, 3, '2021-11-20'),
(1003, 1, '2021-03-24'),
(2001, 2, '2022-04-27'),
(2002, 3, '2021-01-22'),
(1001, 4, '2021-07-15'),
(1003, 4, '2022-11-21');'''
cur.execute(exp_sql9)  

''' o Mysql guarda as datas como YYY-MM-DD'''

con.commit()

con.close()