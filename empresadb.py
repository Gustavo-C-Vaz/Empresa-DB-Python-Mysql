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


