<h1 align="center">
  <img alt="KenzieHub" title="KenzieHub" src="https://kenzie.com.br/images/logoblue.svg" width="100px" />
</h1>

<h1 align="center">
  Gestão de Hábitos - API
</h1>

<p align = "center">
Este é o backend da aplicação Gestão de hábitos - Uma solução para o acompanhamento de hábitos do usuário e de conexão entre pessoas com hábitos em comum. O objetivo dessa aplicação é conseguir criar um frontend de qualidade em grupo, utilizando o que foi ensinado no módulo - E desenvolver hard skills e soft skills.
</p>

## **Endpoints**

A API tem 25 endpoints listados, sendo em volta principalmente dos grupos de hábitos - possibilitando o usuário a ingressar em grupos, se conectar e criar metas e atividades para o seu grupo. <br/>
Também existe a possibilidade do usuário fazer um tracking pessoal de hábitos dentro da aplicação. <br/>
O JSON para utilizar no Insomnia é este aqui -> https://drive.google.com/file/d/1jyMfmSCTTMP5RIoFeoUxQQk-x5TcJicW/view?usp=sharing
Para importar o JSON no Insomnia é só baixar o arquivo. Na palavra "Insomnia" no canto superior esquerdo. Nesse dropdown é só clicar em "Import / Export > Import Data > From File" e selecionar o arquivo que foi feito download :v:

O url base da API é https://kenzie-habits.herokuapp.com/

### **Sobre o erro: "Not Found - The requested resource was not found on this server."**

Esse erro acontece quando acessado um endpoint sem utilizar uma barra no final do endpoint. Lembre-se sempre de adicionar a barra da seguinte maneira:

:white_check_mark: https://kenzie-habits.herokuapp.com/users/

:x: https://kenzie-habits.herokuapp.com/users

## **Endpoint - Users**

### **Rotas que não precisam de autenticação**

<hr/>

<h2> Listando usuários </h2>

Na listagem de usuários, é recebido 15 itens por vez. Sua paginação é feita pelo query param `page=integer`

`GET /users/ - FORMATO DA REQUISIÇÃO`

```json
{
  "count": 598,
  "next": "https://kenzie-habits.herokuapp.com/users/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "gabriel",
      "email": "gabriel@gmail.com"
    },
    {
      "id": 409,
      "username": "lele",
      "email": "lele@mail.com"
    },
    {
      "id": 3,
      "username": "kenzo2021",
      "email": "kenzo2021@mail.com"
    },
    {
      "id": 4,
      "username": "exe",
      "email": "exe@email.com"
    },
    {
      "id": 5,
      "username": "teste1234",
      "email": "teste1234@gmail.com"
    },
    {
      "id": 6,
      "username": "teste",
      "email": "teste@gmail.com"
    },
    {
      "id": 7,
      "username": "exe1",
      "email": "exe1@email.com"
    },
    {
      "id": 542,
      "username": "Ayana",
      "email": "ayana@mail.com.br"
    }
  ]
}
```

<h2> Acessando recurso de usuário </h2>
É possível acessar um usuário em específico acessando o recurso de seu id, que é um numero inteiro.

`GET /users/:user_id/ - FORMATO DA REQUISIÇÃO`

```json
{
  "id": 1,
  "username": "gabriel-kenzie",
  "email": "gabriel@kenzie.com.br"
}
```

<h2 align ='left'> Criação de usuário </h2>

`POST /users/ - FORMATO DA REQUISIÇÃO`

```json
{
  "username": "gabriel-kenzie",
  "email": "gabriel@kenzie.com.br",
  "password": "123456"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /users/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "username": "gabriel-kenzie",
  "email": "gabriel@kenzie.com.br"
}
```

<h2 align ='left'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:
No exemplo a requisição foi feita faltando o campo "password" e com um nome de usuário que já está cadastrado.

`POST /users/ - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "username": ["A user with that username already exists."],
  "password": ["This field is required."]
}
```

Os erros são descritos por campo, com cada uma de suas especificações. Nessa API o campo email pode ser repetido, porém o username, não.

<h2 align = "left"> Login </h2>

`POST /sessions/ - FORMATO DA REQUISIÇÃO`

```json
{
  "username": "johndoe",
  "password": "123456"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /sessions/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzODgyMDc3MiwianRpIjoiMDJlMWFkOTllYTAzNDQwNDkyNDQ3MDU1NzFhNGNiOTMiLCJ1c2VyX2lkIjoxOX0.PnzZNt-tZ1IuFfWuViVYHgg48Sdq5Bqu0iqinOHBh00",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MTY2MzcyLCJqdGkiOiI4ZWE2ZjJiMWQwZGU0NDJmYTQ1NTBhMDZjZGJlMGRmMCIsInVzZXJfaWQiOjE5fQ.UCTZiSdcxlyNhjqlGhCDann5MmF1taQqqSajKGc-i8A"
}
```

Para nós, o que importa será o token "access". O campo "refresh" não é necessário no momento. Sua utilidade é para criar uma estratégia de refresh token para manter o usuário na aplicação, porém ela não se faz necessária no nosso contexto.

Com o token de "access" em mãos, podemos decodificar ele usando a biblioteca jwt-decode para receber o ID do usuário que fez login e manter isso salvo no frontend.

Link para o jwt-decode: https://www.npmjs.com/package/jwt-decode

<h2 align ='left'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo faltando, a resposta de erro será assim:
No exemplo a requisição foi feita faltando o campo "password".

`POST /sessions/ - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "password": ["This field is required."]
}
```

Quando tentando acessar com um usuário ou senha inválida:

`POST /sessions/ - `
` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "detail": "No active account found with the given credentials"
}
```

### **Rotas que precisam de autenticação**

<h2> Sobre autenticação </h2>

Rotas que necessitam de autorização deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

Sendo que o token, é o campo `access` disponibilizado na resposta do endpoint /sessions/

Caso você tente acessar qualquer endpoint que necessite de autorização, sem passar o token, irá receber o seguinte erro:

`STATUS 401`

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<h2 align ='left'> Atualização de usuário </h2>

Para atualizar um usuário, é necessário um PATCH em /users/:user_id. O id será um inteiro que pode ser descoberto usando o jwt-decode mencionado acima. É possível atualizar para um novo username ainda não utilizado ou atualizar o email.

`PATCH /users/:user_id/ - FORMATO DA REQUISIÇÃO`

```json
{
  "username": "gabriel-kenzie-new",
  "email": "gabriel-new@kenzie.com.br"
}
```

Caso dê tudo certo, a resposta será assim:

`PATCH /users/:user_id/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 19,
  "username": "gabriel-kenzie-new",
  "email": "gabriel-new@kenzie.com.br"
}
```

<h2 align ='left'> Possíveis erros </h2>

É possível receber um erro quando tentar atualizar um perfil que não corresponde com o token informado na autorização. Ou seja = o token deve ser do usuário que está tentando atualizar o perfil.

`PATCH /users/:user_id/ - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "status": "error",
  "message": "Only the owner of the profile can update his own information"
}
```

Tentando atualizar para um username que já está em uso.

`PATCH /users/:user_id/ - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "username": ["A user with that username already exists."]
}
```

## **Endpoints - Habits**

Os endpoints de hábitos, é uma seção para a aplicação ser algo pessoal, voltado para o usuário criar sua rotina de hábitos e atualizar conforme avança nisso.
Na criação do seu frontend, você irá determinar como essas seções podem funcionar e criar sua própria regra de negócio.

:warning: **Importante: Toda essa parte de hábitos necessita de autenticação.**

<h2 align ='left'> Criação de hábitos </h2>

`POST /habits/ - FORMATO DA REQUISIÇÃO`

```json
{
  "title": "Calistenia a tarde (15 minutos)",
  "category": "Sáude",
  "difficulty": "Muito díficil",
  "frequency": "Diária",
  "achieved": false,
  "how_much_achieved": 30,
  "user": 673
}
```

:warning: **Importante: O Campo `user` recebe o user_id que você deve decodificar do token jwt.**

Esse campo irá relacionar o hábito que você está criando com o usuário que recebe ele, que deverá ser o usuário logado na sua aplicação.

OBS: o campo `how_much_achieved` e `achieved`, não são relacionados, sinta-se a vontade para criar uma regra de negócio de como isso pode se comportar no seu frontend.

Caso dê tudo certo, a resposta será assim:

`POST /habits/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 2607,
  "title": "Calistenia a tarde (15 minutos)",
  "category": "Sáude",
  "difficulty": "Muito díficil",
  "frequency": "Diária",
  "achieved": false,
  "how_much_achieved": 30,
  "user": 673
}
```

<h2 align ='left'> Buscando hábitos </h2>

`GET /habits/personal/ - FORMATO DA RESPOSTA - STATUS 201`

```json
[
  {
    "id": 2607,
    "title": "Calistenia a tarde (15 minutos)",
    "category": "Sáude",
    "difficulty": "Muito díficil",
    "frequency": "Diária",
    "achieved": false,
    "how_much_achieved": 30,
    "user": 673
  }
]
```

Irá buscar os hábitos cadastrados anteriormente, que foram relacionados usando o campo `user` na hora da criação.

<h2> Atualizar um hábito </h2>

`PATCH /habits/:habit_id/ - FORMATO DA REQUISIÇÃO`

```json
{
  "achieved": true,
  "how_much_achieved": 100
}
```

`PATCH /habits/:habit_id/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 2607,
  "title": "Calistenia a tarde (15 minutos)",
  "category": "Sáude",
  "difficulty": "Muito díficil",
  "frequency": "Diária",
  "achieved": true,
  "how_much_achieved": 100,
  "user": 673
}
```

<h2> Deletar um hábito </h2>

Para deletar um hábito, basta fazer um DELETE usando o id dele.

`DELETE /habits/:habit_id/ - FORMATO DA RESPOSTA - STATUS 204`

<h2 align ='left'> Possíveis erros </h2>

É possível receber um erro ao tentar deletar um hábito inexistente.

`DELETE /habits/:habit_id/ - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

## **Endpoints - Groups**

Os endpoints de grupos, é uma seção para a aplicação ser algo voltado para conexão entre usuários da aplicação. Dentro dessa parte o usuário pode criar grupos ou procurar grupos existentes para se inscrever e acompanhar as metas e atividades dos grupos que está inscrito.

:warning: **Importante: Toda essa parte de grupos necessita de autenticação.**

<h2> Listando grupos </h2>

Na listagem de grupos, é recebido 15 itens por vez. Sua paginação é feita pelo query param `page=integer`.

Pode ser passado diversos query params nesse endpoint para realizar filtros na resposta.

`search=string` - Usando o search, será buscado nos resultados por nome, descrição e categoria.<br/>
`category=string` - Usando apenas category, é possível filtrar apenas pela categoria.

Isso possibilita que sua aplicação seja nichada por uma categoria ou geral, isso é uma escolha que os dev's frontend podem fazer utilizando essa API.

`GET /groups/ - FORMATO DA REQUISIÇÃO - STATUS 200`

Resposta:

```json
{
  "count": 762,
  "next": "https://kenzie-habits.herokuapp.com/groups/?page=2",
  "previous": null,
  "results": [
    {
      "id": 4,
      "name": "Cow de Wars",
      "description": "fgdgdfgfdgf",
      "category": "Saúde",
      "creator": {
        "id": 13,
        "username": "KenzoTeste",
        "email": ""
      },
      "users_on_group": [
        {
          "id": 1,
          "username": "gabriel",
          "email": "gabriel@gmail.com"
        },
        {
          "id": 4,
          "username": "exe",
          "email": "exe@email.com"
        },
        {
          "id": 58,
          "username": "teste202100",
          "email": "teste202100@gmail.com"
        },
        {
          "id": 145,
          "username": "testestandinho",
          "email": "tetest@hothot.com"
        },
        {
          "id": 302,
          "username": "miaferrari19",
          "email": "mia@gmail.com"
        },
        {
          "id": 566,
          "username": "kenzinhooo",
          "email": "kenzinhooo@mail.com"
        },
        {
          "id": 568,
          "username": "pinguim2",
          "email": "pinguim@teste.com"
        },
        {
          "id": 599,
          "username": "monicaSilva",
          "email": "nica@mail.com"
        },
        {
          "id": 668,
          "username": "VictorTeste2",
          "email": "victor@teste.com.br"
        }
      ],
      "goals": [
        {
          "id": 753,
          "title": "Nenhuma falta na academia",
          "difficulty": "Díficil",
          "achieved": false,
          "how_much_achieved": 10,
          "group": 4
        },
        {
          "id": 148,
          "title": "Eu consigo voar",
          "difficulty": "Díficil",
          "achieved": false,
          "how_much_achieved": 60,
          "group": 4
        }
      ],
      "activities": [
        {
          "id": 210,
          "title": "re",
          "realization_time": "2021-10-19T13:33:00Z",
          "group": 4
        },
        {
          "id": 212,
          "title": "test",
          "realization_time": "2021-10-20T13:47:00Z",
          "group": 4
        },
        {
          "id": 220,
          "title": "Natação profunda em Java",
          "realization_time": "2021-03-10T15:00:00Z",
          "group": 4
        },
        {
          "id": 221,
          "title": "Natação profunda em Flask Django",
          "realization_time": "2021-03-10T15:00:00Z",
          "group": 4
        },
        {
          "id": 361,
          "title": "Spring Boot",
          "realization_time": "1945-12-20T21:47:00Z",
          "group": 4
        },
        {
          "id": 840,
          "title": "Estocar Vento",
          "realization_time": "2069-11-15T00:00:00Z",
          "group": 4
        },
        {
          "id": 211,
          "title": "test",
          "realization_time": "2021-10-20T13:44:00Z",
          "group": 4
        }
      ]
    },
    {
      "id": 11,
      "name": "Grupo de Estudo",
      "description": "Descrição bolada 3",
      "category": "Educação 2",
      "creator": {
        "id": 16,
        "username": "roberto_doidão",
        "email": "roberto9999@gmail.com"
      },
      "users_on_group": [
        {
          "id": 24,
          "username": "teste98",
          "email": "teste1@email.com"
        },
        {
          "id": 16,
          "username": "roberto_doidão",
          "email": "roberto9999@gmail.com"
        },
        {
          "id": 91,
          "username": "maurice",
          "email": "maurice@email.com"
        },
        {
          "id": 120,
          "username": "nvouser74",
          "email": "novimuser@hothot.com"
        },
        {
          "id": 269,
          "username": "tester",
          "email": "test@ndo.com"
        },
        {
          "id": 304,
          "username": "pinguim",
          "email": "asdf@hotmail.com"
        },
        {
          "id": 325,
          "username": "laris",
          "email": "lari@teste.com"
        },
        {
          "id": 555,
          "username": "chico",
          "email": "chico@ka.br"
        },
        {
          "id": 566,
          "username": "kenzinhooo",
          "email": "kenzinhooo@mail.com"
        },
        {
          "id": 626,
          "username": "macacoloucoo",
          "email": "oi@oi.com"
        }
      ],
      "goals": [
        {
          "id": 796,
          "title": "asd",
          "difficulty": "Regular",
          "achieved": false,
          "how_much_achieved": 10,
          "group": 11
        },
        {
          "id": 792,
          "title": "asddsa",
          "difficulty": "Regular",
          "achieved": false,
          "how_much_achieved": 40,
          "group": 11
        }
      ],
      "activities": []
    },
    {
      "id": 30,
      "name": "Natação",
      "description": "Descrição bolada",
      "category": "Saúde",
      "creator": {
        "id": 55,
        "username": "moisesgaioli",
        "email": "moises@gmail.com"
      },
      "users_on_group": [
        {
          "id": 35,
          "username": "herteste",
          "email": "teste@gmail.com"
        },
        {
          "id": 156,
          "username": "felipeSilveira",
          "email": "felipelarson@gmail.com"
        },
        {
          "id": 469,
          "username": "jerlysson",
          "email": "eunovo@hot.com"
        },
        {
          "id": 34,
          "username": "DevRafael",
          "email": "devrafael@gmail.com"
        },
        {
          "id": 610,
          "username": "Nhocco",
          "email": "alesilvasp@gmail.com"
        }
      ],
      "goals": [],
      "activities": []
    }
  ]
}
```

Dentro da listagem, temos as informações do grupo, dos usuários que estão no grupo, as atividades do grupo e suas metas. Também o criador do grupo.

<h2> Criando um grupo </h2>

Para criar um grupo, basta enviar no endpoint as informações de nome, descrição e categoria no body da requisição.

`POST /groups/ - FORMATO DA REQUISIÇÃO `

```json
{
  "name": "Grupo de leitura",
  "description": "Somos um grupo de leitura focado em auto ajuda.",
  "category": "Leitura"
}
```

`POST /groups/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 849,
  "name": "Grupo de leitura",
  "description": "Somos um grupo de leitura focado em auto ajuda.",
  "category": "Leitura",
  "creator": 673,
  "users_on_group": [673],
  "goals": [],
  "activities": []
}
```

Após criar um grupo, o criador é automaticamente inserido no array `users_on_group`

<h2> Editando um grupo </h2>

Para editar o grupo, você deve ser o criador dele, caso contrário não será possível. É possível editar o nome, descrição e categoria.

`PATCH /groups/:group_id/ - FORMATO DA REQUISIÇÃO `

```json
{
  "name": "Grupo de leitura atualizado"
}
```

`PATCH /groups/:group_id/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 849,
  "name": "Grupo de leitura",
  "description": "Somos um grupo de leitura focado em auto ajuda.",
  "category": "Grupo atualizado",
  "creator": {
    "id": 673,
    "username": "gabriel-kenzie",
    "email": "gabriel@kenzie.com.br"
  },
  "users_on_group": [
    {
      "id": 673,
      "username": "gabriel-kenzie",
      "email": "gabriel@kenzie.com.br"
    }
  ],
  "goals": [],
  "activities": []
}
```

<h2> Possíveis erros </h2>

Tentando editar um grupo no qual o usuário logado não é o criador.

`PATCH /groups/:group_id/ - FORMATO DA REQUISIÇÃO `

```json
{
  "name": "Grupo de leitura atualizado"
}
```

`PATCH /groups/:group_id/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "status": "error",
  "message": "Only the group creator can update the group"
}
```

<h2> Se inscrevendo em um grupo </h2>

É possível se inscrever em qualquer grupo cadastrado, utilizando a seguinte requisição:

Não é necessário um corpo da requisição.

`POST /groups/:group_id/subscribe`

Caso dê tudo certo:

```json
{
  "message": "User inserted on group",
  "user": {
    "id": 19,
    "username": "araujooj",
    "email": "gabriel@gmail.com"
  }
}
```

<h2> Possíveis erros </h2>

Tentando se inscrever em um grupo que já está inscrito.

`POST /groups/:group_id/subscribe`

```json
{
  "message": "User already on group"
}
```

<h2> Buscando inscrições </h2>

É possível buscar na API os grupos no qual o usuário logado está inscrito.

`GET /groups/subscriptions/ - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 847,
    "name": "Grupo novo 2",
    "description": "Descrição bolada",
    "category": "Saúde",
    "creator": {
      "id": 673,
      "username": "gabriel-kenzie",
      "email": "gabriel@kenzie.com.br"
    },
    "users_on_group": [
      {
        "id": 673,
        "username": "gabriel-kenzie",
        "email": "gabriel@kenzie.com.br"
      }
    ],
    "goals": [],
    "activities": []
  },
  {
    "id": 849,
    "name": "Grupo de leitura",
    "description": "Somos um grupo de leitura focado em auto ajuda.",
    "category": "Grupo atualizado",
    "creator": {
      "id": 673,
      "username": "gabriel-kenzie",
      "email": "gabriel@kenzie.com.br"
    },
    "users_on_group": [
      {
        "id": 673,
        "username": "gabriel-kenzie",
        "email": "gabriel@kenzie.com.br"
      }
    ],
    "goals": [],
    "activities": []
  },
  {
    "id": 848,
    "name": "Grupo de leitura",
    "description": "Somos um grupo de leitura focado em auto ajuda.",
    "category": "Livros",
    "creator": {
      "id": 673,
      "username": "gabriel-kenzie",
      "email": "gabriel@kenzie.com.br"
    },
    "users_on_group": [
      {
        "id": 673,
        "username": "gabriel-kenzie",
        "email": "gabriel@kenzie.com.br"
      }
    ],
    "goals": [],
    "activities": []
  }
]
```

<h2> Se desinscrevendo de um grupo </h2>

É possível sair de um grupo que o usuário está inscrito

`DELETE /groups/:group_id/unsubscribe`

<h2> Possíveis erros </h2>

Tentando se desinscrever de um grupo que não está inscrito

```json
{
  "message": "User not on group"
}
```

## **Endpoints - Goals**

Essa seção da API é para a criação de metas para o grupo todo seguir. Elas funcionam de maneira parecida com o endpoint de habits, porém com o intuito de ser algo que o grupo especificado irá seguir.

### **:warning: IMPORTANTE! Metas e atividades não são relacionadas entre si na API. Apenas são relacionadas com o grupo.**

:warning: **Importante: Toda a parte de goals necessita de autenticação.**

<h2> Criando metas </h2>

`POST - /goals/ - FORMATO DA REQUISIÇÃO`

```json
{
  "title": "Nenhuma falta na academia cometida pelos membros do grupo na semana",
  "difficulty": "Díficil",
  "how_much_achieved": 100,
  "achieved": false,
  "group": 3
}
```

É importante que o `group`, tenha o id do grupo que será cadastrado determinada meta.

`POST /goals/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 848,
  "title": "Nenhuma falta na academia cometida pelos membros do grupo na semana",
  "difficulty": "Díficil",
  "achieved": false,
  "how_much_achieved": 0,
  "group": 3
}
```

<h2> Possíveis erros </h2>

Tentando cadastrar uma meta para um grupo inexistente

`POST /goals/ - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "group": ["Invalid pk \"1\" - object does not exist."]
}
```

<h2> Buscando metas </h2>

Para buscar metas, devemos informar no query param `group`, qual será o grupo que iremos buscar as metas.
Essas informações também estão disponíveis no GET em `/groups/:group_id`.

Porém, por esse endpoint é possível fazer a paginação dos itens

`GET /goals/?group=4 - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 753,
      "title": "Nenhuma falta na academia",
      "difficulty": "Díficil",
      "achieved": false,
      "how_much_achieved": 10,
      "group": 4
    },
    {
      "id": 148,
      "title": "Eu consigo voar",
      "difficulty": "Díficil",
      "achieved": false,
      "how_much_achieved": 60,
      "group": 4
    }
  ]
}
```

<h2> Atualizando metas </h2>
Para atualizar uma meta, é necessário enviar o id da meta que está dentro do seu objeto.

`PATCH /goals/:goal_id/ - FORMATO DA REQUISIÇÃO`

```json
{
  "achieved": true
}
```

`PATCH /goals/:goal_id/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 753,
  "title": "Nenhuma falta na academia",
  "difficulty": "Díficil",
  "achieved": true,
  "how_much_achieved": 10,
  "group": 4
}
```

<h2> Possíveis erros </h2>

Tentando atualizar uma meta que não existe

`PATCH /goals/:goal_id/ - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

<h2> Deletar uma meta <h2>

Para deletar uma meta, basta fazer um DELETE usando o id dela.

`DELETE /goals/:goal_id/ - FORMATO DA RESPOSTA - STATUS 204`

## **Endpoints - Activities**

Essa seção da API é para a criação de atividades para o grupo. As atividades são totalmente determinadas a partir do frontend e os campos que são passados são apenas seu título e quando ela será realizada.

Por exemplo um grupo de academia teria atividades relacionadas a exercícios que seriam feitos em grupo.
Um grupo de leitura teria uma atividade de discutir sobre os livros lidos da semana.

### **:warning: IMPORTANTE! Metas e atividades não são relacionadas entre si na API. Apenas são relacionadas com o grupo.**

<h2> Criando atividades </h2>

`POST - /activities/ - FORMATO DA REQUISIÇÃO`

```json
{
  "title": "Treino funcional na praia",
  "realization_time": "2021-03-10T15:00:00Z",
  "group": 2
}
```

É importante que o `group`, tenha o id do grupo que será cadastrado determinada atividade.

`POST /activities/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 918,
  "title": "Treino funcional na praia",
  "realization_time": "2021-03-10T15:00:00Z",
  "group": 753
}
```

<h2> Possíveis erros </h2>

Tentando cadastrar uma atividade para um grupo inexistente

`POST /activities/ - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "group": ["Invalid pk \"1\" - object does not exist."]
}
```

<h2> Buscando atividades </h2>

Para buscar atividades, devemos informar no query param `group`, qual será o grupo que iremos buscar as atividades.
Essas informações também estão disponíveis no GET em `/groups/:group_id`.

Porém, por esse endpoint é possível fazer a paginação dos itens

`GET /activities/?group=4 - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 918,
      "title": "Treino funcional na praia",
      "realization_time": "2021-03-10T15:00:00Z",
      "group": 753
    }
  ]
}
```

<h2> Atualizando atividades </h2>
Para atualizar uma atividade, é necessário enviar o id da atividade que está dentro do seu objeto.

`PATCH /activities/:activity_id/ - FORMATO DA REQUISIÇÃO`

```json
{
  "title": "Treino funcional na praia - Atualizado"
}
```

`PATCH /activities/:activity_id/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 918,
  "title": "Treino funcional na praia - atualizado",
  "realization_time": "2021-03-10T15:00:00Z",
  "group": 753
}
```

<h2> Possíveis erros </h2>

Tentando atualizar uma atividade que não existe

`PATCH /activities/:activity_id/ - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

<h2> Deletar uma atividade <h2>

Para deletar uma atividade, basta fazer um DELETE usando o id dela.

`DELETE /activities/:activity_id/ - FORMATO DA RESPOSTA - STATUS 204`

---

Feito com ♥ by araujooj :wave:
