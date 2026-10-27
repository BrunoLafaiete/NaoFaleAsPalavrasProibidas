# Não fale as palavras proibídas!

Jogo web de palavras em português para duas equipes compartilharem um celular. Interface responsiva, sem conta e sem backend.

## Desenvolvimento

Use Node.js 22.12+ (validado com Node 24) e npm.

```sh
npm ci --cache /workspace/.npm-cache
npm run dev
```

O Vite usa a porta 5173 por padrão, com o jogo no caminho `/NaoFaleAsPalavrasProibidas/`. Para conferir a versão de produção:

```sh
npm test
npm run build
npm run preview
```

Publique a pasta `dist/` em uma hospedagem estática com HTTPS. Não há chaves, variáveis de ambiente ou banco de dados necessários. As fontes do Google são opcionais: a interface tem fontes de sistema como alternativa. Não é necessário instalar como PWA.

## Regras

- Uma rodada contém um turno de cada equipe. Padrão: 10 rodadas; configurável de 1 a 99.
- Turnos de 60, 90 ou 120 segundos; 3, 5 ou 7 pulos, renovados a cada turno.
- Verde: +1 ponto e próxima carta. Laranja: consome um pulo e troca de carta.
- Vermelho: descarta sem pontuar ou consumir pulos. No **Modo erro zero!**, encerra o turno, preservando os pontos.
- O cronômetro continua ao trocar de aplicativo ou bloquear o celular. Pausar esconde a carta e congela o tempo.
- 60 cartas próprias, embaralhadas sem repetição até o baralho acabar. Nesse caso, o turno termina e o baralho é reembaralhado no próximo turno, com aviso.
- Empate permite uma rodada extra completa.

A partida é salva no armazenamento local do navegador; o botão “Continuar partida” retoma o estado. Limpar os dados do site apaga a partida. Sons precisam ser ativados pelo botão de som e dependem das permissões/configurações do Safari.

## Próximos passos

Validar fisicamente no Safari do iPhone 15 e ampliar o baralho inicial para 150 cartas. A versão atual não tem multiplayer em aparelhos separados nem funcionamento offline garantido.

## GitHub Pages

O workflow `.github/workflows/deploy-pages.yml` testa, compila e publica a pasta `dist/` a cada push na branch `main`. O caminho `/NaoFaleAsPalavrasProibidas/` está configurado em `vite.config.ts`.

1. Abra **Settings → Pages** no repositório.
2. Em **Build and deployment → Source**, selecione **GitHub Actions**.
3. Na aba **Actions**, abra **Publicar no GitHub Pages**. Se necessário, use **Run workflow** na branch `main` (ou reexecute uma tentativa que falhou antes de ativar Pages).
4. Aguarde os jobs `build` e `deploy` ficarem verdes.

O endereço esperado é https://brunolafaiete.github.io/NaoFale-jogo/ . Só estará disponível depois da publicação bem-sucedida. Abra-o no Safari para validar no iPhone. Repositórios privados precisam de um plano GitHub que ofereça Pages.

O workflow usa a autenticação automática do GitHub Actions, sem token pessoal ou segredo manual.
