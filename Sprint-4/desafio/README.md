##   Sprint 4 - Desafio 

### Objetivo
O objetivo desse desafio foi criar imagens e containers que executassem arquivos .py.


### Criação do Dockerfile
Para criar o arquvio de instruções Dockerfile, utilizei as seguintes instruções em ambos os scripts (carguru e hash):

* FROM: especifica a imagem base. Nesse caso, utilizei s versão 3 do python em sua variante "slim", que é mais leve que a versão padrão
* WORKDIR: define o diretório de trabalho dentro do container.
* COPY: copia arquivos do sistema local para o container.
* CMD: define o comando a ser executado quando o container é iniciado.

A única diferença entre os Dockerfiles criados foi o comando no "CMD", que especifica o arquivo a ser executado: "carguru.py" e "hash.py".

<p>Dockerfile de "carguru.py"</p>

![Alt text](../evidencias/dockerfile_carguru.jpg)

<p>Dockerfile de "hash.py"</p>

![Alt text](../evidencias/dockerfile_hash.jpg)


### Carguru
<p>Depois de criar o Dockerfile, utilizei o comando "docker build ." para construir a imagem.</p>

![Alt text](../evidencias/criando_imagem_carguru.jpg)

<p>Após a imagem ser contruída, renomeei ela usando "docker tag <imagem_id> carguru-imagem" </p>

![Alt text](../evidencias/nomeando_imagem_carguru.jpg)

<p>Por fim, nomeei e executei o container com o comando "docker run --name carguru-container carguru-imagem", e o resultado foi exibido em seguida.</p>

![Alt text](../evidencias/rodando_container_carguru.jpg)





