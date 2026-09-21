# -*- coding: utf-8 -*-
"""Blog: índice + artigos."""
from site_engine import (
    page, img, WA_DEFAULT, breadcrumb_ld, faq_ld, faq_block, jsonld, BASE_URL, wa_link,
)

CATEGORIES = {
    "harmonizacao": "Harmonização Orofacial",
    "ortodontia": "Ortodontia",
    "implantes": "Implantes",
    "facetas": "Facetas &amp; Lentes",
    "geral": "Odontologia Geral",
}

AUTHOR = "Equipe Instituto Christian Andrade"

POSTS = [
    {
        "slug": "implante-dentario-doi-recuperacao.html",
        "title": "Implante dentário dói? Como é a recuperação passo a passo",
        "short_title": "Implante dentário dói? Veja a recuperação",
        "description": "Entenda como funciona a cirurgia de implante dentário, o que esperar da recuperação e por que a dor costuma ser bem menor do que se imagina.",
        "category": "implantes",
        "img": "raiox",
        "date": "2026-02-10",
        "read": 7,
        "excerpt": "A cirurgia guiada e a anestesia local mudaram completamente a experiência de quem coloca um implante. Veja o que realmente acontece em cada etapa.",
        "faqs": [
            ("Implante dentário dói durante a cirurgia?", "Não. O procedimento é realizado com anestesia local, então você não sente dor durante a cirurgia — no máximo uma sensação de pressão."),
            ("E depois, no pós-operatório?", "É comum um desconforto leve a moderado nos primeiros dias, controlado com a medicação prescrita pelo dentista."),
            ("Quanto tempo leva para o implante cicatrizar por completo?", "A osseointegração costuma levar de 2 a 6 meses, variando conforme a região e a condição óssea de cada paciente."),
        ],
        "body": '''
        <p>Poucas frases geram tanta ansiedade em um consultório odontológico quanto "você vai precisar de um implante". E, quase sempre, a primeira pergunta que vem à cabeça é: <strong>vai doer?</strong> A boa notícia é que a odontologia mudou muito nas últimas duas décadas — e a experiência de colocar um implante hoje tem pouca relação com o que as pessoas imaginam.</p>

        <h2>O que é, de fato, um implante dentário</h2>
        <p>O implante é um pequeno parafuso, geralmente de titânio, que substitui a raiz de um dente perdido. Ele é instalado no osso da mandíbula ou maxila e, depois de um período de cicatrização, recebe uma coroa protética que devolve a função de mastigação e a estética do sorriso.</p>
        <p>No Instituto Christian Andrade, utilizamos o sistema <strong>Grand Morse Neodent</strong>, referência mundial em estabilidade e biocompatibilidade, o que contribui diretamente para a previsibilidade do resultado e para a <a href="../tratamento-implantes.html">garantia vitalícia</a> oferecida no tratamento.</p>

        <h2>Etapa 1 — Avaliação e planejamento digital</h2>
        <p>Tudo começa com uma tomografia e uma avaliação clínica detalhada. A partir dessas imagens, é possível planejar com precisão milimétrica onde e em que ângulo o implante será posicionado — o que chamamos de <strong>cirurgia guiada</strong>. Esse planejamento reduz a necessidade de cortes maiores e torna o procedimento mais previsível.</p>

        <h2>Etapa 2 — O dia da cirurgia</h2>
        <p>Com anestesia local, a instalação do implante costuma levar entre 30 e 60 minutos por unidade, a depender da complexidade do caso. Graças ao planejamento guiado, muitos procedimentos são realizados sem cortes ou pontos extensos — o que já reduz bastante o inchaço e o desconforto no pós-operatório.</p>
        <p>Em casos indicados, é possível ainda realizar a <strong>carga imediata</strong>: você sai da consulta com um dente provisório fixo no mesmo dia, sem período algum com o espaço vazio.</p>

        <h2>Etapa 3 — O pós-operatório real (sem exageros)</h2>
        <p>É normal sentir um desconforto leve a moderado nas primeiras 48 a 72 horas, parecido com o de uma extração dentária, controlado com analgésicos e anti-inflamatórios comuns prescritos pelo dentista. Pequeno inchaço também pode ocorrer, especialmente em cirurgias múltiplas.</p>
        <ul>
          <li>Evite alimentos muito quentes ou duros nos primeiros dias.</li>
          <li>Mantenha a higienização recomendada pela equipe, mesmo na região operada.</li>
          <li>Compareça aos retornos agendados — eles são parte essencial do sucesso do implante.</li>
        </ul>

        <blockquote>“Fiquei muito feliz com o atendimento, profissionais qualificados e atenciosos, esperei 30 anos para realizar esse sonho.” — Edna Mattar, paciente de implantes</blockquote>

        <h2>Etapa 4 — Osseointegração e prótese final</h2>
        <p>Nas semanas seguintes, o osso se funde ao implante em um processo chamado osseointegração, que costuma levar de 2 a 6 meses. Depois desse período, a coroa definitiva é instalada e ajustada — e a partir daí o cuidado passa a ser o mesmo de um dente natural: escovação, fio dental e check-ups regulares.</p>

        <div class="cta-inline">
          <div><h4>Quer saber se o implante é indicado para o seu caso?</h4><p>Uma avaliação com exame de imagem responde essa pergunta com precisão.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_implantes}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "harmonizacao-orofacial-o-que-e.html",
        "title": "Harmonização orofacial: o que é, para quem é indicada e o que esperar",
        "short_title": "O que é harmonização orofacial?",
        "description": "Guia completo sobre harmonização orofacial: bichectomia, fios de sustentação e preenchimento facial explicados de forma clara.",
        "category": "harmonizacao",
        "img": "clinica_vista",
        "date": "2026-01-22",
        "read": 6,
        "excerpt": "Nem tudo que aparece nas redes sociais é harmonização bem feita. Entenda o que o procedimento realmente propõe: equilíbrio, não transformação.",
        "faqs": [
            ("Harmonização orofacial deixa o rosto artificial?", "Quando bem indicada e executada, o objetivo é justamente o oposto: valorizar as características naturais do rosto, sem efeito de exagero."),
            ("Preciso ser jovem para fazer harmonização?", "Não. A indicação é feita conforme a necessidade e objetivo de cada pessoa, em qualquer faixa etária adulta, após avaliação individual."),
            ("Um dentista pode aplicar preenchimento facial?", "Sim, cirurgiões-dentistas habilitados podem realizar procedimentos de harmonização orofacial dentro do escopo previsto pelo Conselho Federal de Odontologia."),
        ],
        "body": '''
        <p>O termo "harmonização orofacial" ficou popular — e, com a popularidade, vieram também os exageros que se veem nas redes sociais. Mas o conceito por trás da técnica é bem mais sutil (e bem mais interessante) do que parece: trata-se de <strong>equilibrar</strong> as proporções entre boca e rosto, não de transformá-lo.</p>

        <h2>O que realmente é a harmonização orofacial</h2>
        <p>É um conjunto de procedimentos, geralmente minimamente invasivos, que atuam na região perioral (ao redor da boca) e no contorno facial. No Instituto Christian Andrade, os três procedimentos mais realizados são:</p>
        <ul>
          <li><strong>Bichectomia</strong> — remoção parcial da bola de Bichat para afinar o contorno do rosto de forma definitiva.</li>
          <li><strong>Fios de sustentação</strong> — fios bioabsorvíveis que estimulam colágeno e sustentam a pele sem cirurgia.</li>
          <li><strong>Preenchimento facial</strong> — ácido hialurônico para devolver volume a lábios, maçãs do rosto e queixo.</li>
        </ul>
        <p>Veja o detalhamento completo de cada procedimento na página de <a href="../tratamento-harmonizacao-orofacial.html">harmonização orofacial</a>.</p>

        <h2>Para quem é indicada</h2>
        <p>Não existe um perfil único. Pessoas que buscam harmonização geralmente querem corrigir uma assimetria pontual, suavizar sinais de flacidez ou simplesmente valorizar uma característica que já possuem — um contorno de mandíbula, um lábio mais definido. A avaliação individual é o que define se, e qual, procedimento faz sentido.</p>

        <h2>O resultado é permanente?</h2>
        <p>Depende do procedimento. A bichectomia tem efeito definitivo, já que remove tecido adiposo. Fios de sustentação e preenchimentos, por outro lado, têm duração média de 12 a 18 meses, variando conforme metabolismo, técnica utilizada e cuidados pós-procedimento.</p>

        <blockquote>“Recomendo o Instituto pela qualidade do local, do atendimento de toda equipe e dos profissionais qualificados. Já estou a um ano fazendo procedimentos na harmonização facial e me sinto maravilhada.” — Suely Pimpão</blockquote>

        <h2>Como é o dia do procedimento</h2>
        <p>A maioria dos procedimentos de harmonização orofacial é realizada em consultório, com anestesia local, e tem tempo de recuperação curto. Pequenos inchaços ou hematomas no local de aplicação são possíveis e costumam desaparecer em poucos dias.</p>

        <h2>Como saber se é o momento certo</h2>
        <p>Se você já pensou em fazer algum ajuste facial, mas tem dúvidas sobre qual técnica seria indicada, o caminho mais seguro é conversar com quem avalia rosto, mordida e saúde bucal como um conjunto — não só a estética isoladamente.</p>

        <div class="cta-inline">
          <div><h4>Toda indicação começa por uma avaliação individual</h4><p>Marque uma consulta e receba um plano personalizado para o seu rosto.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_harm}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "lentes-de-contato-dental-vs-facetas.html",
        "title": "Lentes de contato dental x facetas: qual a diferença?",
        "short_title": "Lente de contato dental x faceta",
        "description": "Lentes de contato dental e facetas resolvem problemas parecidos, mas não são a mesma coisa. Entenda as diferenças antes de escolher.",
        "category": "facetas",
        "img": "clinica_vermelha",
        "date": "2026-03-02",
        "read": 6,
        "excerpt": "Os dois termos costumam ser usados como sinônimos, mas a espessura, o preparo do dente e a indicação de cada técnica são diferentes.",
        "faqs": [
            ("Lente de contato dental é mais cara que faceta?", "O investimento varia por caso e por material. O mais importante é a indicação correta, definida na avaliação — não o nome do procedimento."),
            ("Dá para fazer só em alguns dentes?", "Sim. Muitos tratamentos são feitos em um grupo específico de dentes visíveis no sorriso, sem necessidade de cobrir toda a arcada."),
            ("As lentes de contato dental mancham com o tempo?", "A porcelana usada nas lentes tem alta resistência a manchas, mantendo a cor estável por muitos anos com bons hábitos de higiene."),
        ],
        "body": '''
        <p>"Quero fazer uma lente" e "quero fazer uma faceta" viraram praticamente sinônimos no vocabulário popular — mas, tecnicamente, não são a mesma coisa. Entender a diferença ajuda a chegar à consulta de avaliação com expectativas mais realistas.</p>

        <h2>Lentes de contato dental</h2>
        <p>São lâminas de porcelana extremamente finas — muitas vezes comparadas a uma lente de contato ocular, daí o nome. Na maioria dos casos, o preparo do dente é mínimo ou inexistente, o que preserva a estrutura dental original. São indicadas principalmente para correção de cor, pequenas alterações de forma e leve realinhamento visual do sorriso.</p>

        <h2>Facetas dentárias</h2>
        <p>As facetas também são lâminas cimentadas sobre o dente, mas costumam ser um pouco mais espessas e podem ser feitas em resina ou porcelana. Por permitirem mais espessura de material, são indicadas para correções mais amplas de forma, tamanho e alinhamento — inclusive em casos que a lente ultrafina não resolveria sozinha.</p>

        <h2>Então qual é a certa para mim?</h2>
        <p>Não existe uma resposta genérica — e qualquer conteúdo que prometa isso está simplificando demais. A escolha depende de:</p>
        <ul>
          <li>Quanto desgaste (se algum) o seu caso permite;</li>
          <li>O tamanho da correção necessária (cor, forma ou alinhamento);</li>
          <li>Sua expectativa de resultado e o planejamento estético do sorriso como um todo.</li>
        </ul>
        <p>Na avaliação, o dentista faz fotos, moldagem (ou escaneamento digital) e, em muitos casos, uma simulação do resultado antes mesmo de iniciar o preparo — veja mais na página de <a href="../tratamento-facetas-lentes.html">facetas e lentes de contato dental</a>.</p>

        <h2>Durabilidade e cuidados</h2>
        <p>Tanto lentes quanto facetas de porcelana, quando bem indicadas e com boa higienização, costumam durar mais de 10 anos. Evitar usar os dentes para abrir embalagens ou morder objetos duros prolonga significativamente a vida útil do trabalho.</p>

        <div class="cta-inline">
          <div><h4>Planeje seu sorriso com uma simulação antes de decidir</h4><p>Marque uma avaliação e veja qual técnica faz mais sentido para o seu caso.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_facetas}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "aparelho-invisivel-ou-metalico.html",
        "title": "Aparelho invisível ou metálico: como escolher o ideal para você",
        "short_title": "Aparelho invisível ou metálico: como escolher",
        "description": "Estético, invisível ou metálico: compare os três tipos de aparelho ortodôntico e entenda qual costuma ser indicado em cada situação.",
        "category": "ortodontia",
        "img": "alinhador",
        "date": "2026-01-08",
        "read": 6,
        "excerpt": "A escolha do aparelho não é só uma questão de estética — envolve o tipo de correção necessária, disciplina de uso e orçamento.",
        "faqs": [
            ("O aparelho invisível é tão eficaz quanto o metálico?", "Para muitos casos, sim — mas exige disciplina, já que os alinhadores precisam ser usados o tempo indicado pelo dentista para funcionar corretamente."),
            ("O aparelho estético de porcelana mancha?", "As braquetes de porcelana têm boa resistência a manchas, mas a linha (elástico) trocada nas manutenções pode escurecer entre uma consulta e outra."),
            ("Posso trocar de tipo de aparelho no meio do tratamento?", "Em alguns casos é possível, mas isso deve ser sempre avaliado pelo ortodontista, considerando a fase do tratamento."),
        ],
        "body": '''
        <p>Antes de decidir entre aparelho estético, invisível ou metálico, vale entender que a pergunta certa não é "qual é o melhor aparelho" — é "qual aparelho é melhor para o meu caso, minha rotina e meu orçamento".</p>

        <h2>Aparelho metálico (tradicional)</h2>
        <p>É a opção com o melhor custo-benefício e décadas de eficácia comprovada. Os bráquetes metálicos permitem grande controle de movimento dentário, o que o torna indicado até para casos ortodônticos mais complexos.</p>

        <h2>Aparelho estético (porcelana)</h2>
        <p>Funciona de forma parecida ao metálico, mas com bráquetes na cor do dente — muito mais discretos no dia a dia. É uma boa escolha para quem quer a eficácia do aparelho fixo tradicional com menos impacto visual.</p>

        <h2>Aparelho invisível (alinhadores)</h2>
        <p>Feito sob medida com escaneamento digital, é composto por uma sequência de alinhadores transparentes e removíveis, trocados periodicamente. A grande vantagem é a discrição e a possibilidade de remover para comer e higienizar — mas isso também exige disciplina: o resultado depende do tempo de uso diário recomendado.</p>

        <h2>Comparando os três</h2>
        <ul>
          <li><strong>Discrição:</strong> invisível &gt; estético &gt; metálico</li>
          <li><strong>Custo-benefício:</strong> metálico &gt; estético &gt; invisível</li>
          <li><strong>Casos complexos:</strong> metálico e estético costumam ter mais versatilidade</li>
          <li><strong>Rotina prática (comer, higienizar):</strong> invisível leva vantagem por ser removível</li>
        </ul>
        <p>Detalhes de cada tipo estão descritos na página de <a href="../tratamento-ortodontia.html">ortodontia</a>.</p>

        <h2>O que realmente define a indicação</h2>
        <p>A avaliação ortodôntica (moldagem ou escaneamento, fotos e análise da mordida) é o que indica, tecnicamente, qual movimento dentário é necessário — e isso, mais do que preferência estética, é o que direciona a recomendação do profissional. Ainda assim, dentro do que é tecnicamente indicado, sua preferência de rotina e orçamento sempre é considerada.</p>

        <blockquote>Independentemente do tipo escolhido, o sucesso do tratamento ortodôntico depende de manutenções regulares — pular consultas atrasa (e pode comprometer) o resultado.</blockquote>

        <div class="cta-inline">
          <div><h4>Descubra qual aparelho é indicado para o seu caso</h4><p>Agende uma avaliação ortodôntica completa.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_ortho}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "bichectomia-cuidados-antes-depois.html",
        "title": "Bichectomia: cuidados antes e depois do procedimento",
        "short_title": "Bichectomia: cuidados antes e depois",
        "description": "O que fazer antes e depois de uma bichectomia para ter uma recuperação tranquila e um resultado definido no contorno do rosto.",
        "category": "harmonizacao",
        "img": "clinica_vista",
        "date": "2026-02-27",
        "read": 5,
        "excerpt": "A bichectomia tem resultado definitivo — o que torna os cuidados no pós-procedimento ainda mais importantes para uma recuperação sem complicações.",
        "faqs": [
            ("Quanto tempo dura o inchaço após a bichectomia?", "O inchaço costuma ser mais evidente nos primeiros 3 a 5 dias, reduzindo progressivamente nas semanas seguintes."),
            ("Posso fazer bichectomia e outro procedimento de harmonização juntos?", "Isso é avaliado individualmente pelo dentista, considerando a extensão dos procedimentos e o tempo de recuperação de cada um."),
            ("O resultado aparece na hora?", "O inchaço inicial disfarça parte do resultado; o contorno definitivo costuma ficar evidente após algumas semanas, quando o edema já baixou."),
        ],
        "body": '''
        <p>A bichectomia — remoção parcial da bola de Bichat, um coxim de gordura na região da bochecha — é um dos procedimentos de harmonização orofacial com resultado mais definitivo. Justamente por isso, os cuidados antes e depois do procedimento merecem atenção redobrada.</p>

        <h2>Antes do procedimento</h2>
        <ul>
          <li>Compareça à consulta de avaliação com seu histórico de saúde completo, incluindo alergias e uso de medicamentos.</li>
          <li>Evite bebidas alcoólicas e cigarro nos dias que antecedem o procedimento — ambos podem interferir na cicatrização.</li>
          <li>Organize sua agenda para os primeiros dias após o procedimento, priorizando descanso.</li>
        </ul>

        <h2>O dia do procedimento</h2>
        <p>Realizada em consultório com anestesia local, a bichectomia costuma durar entre 30 e 45 minutos. O acesso é feito pela parte interna da bochecha, sem cicatriz externa visível.</p>

        <h2>Cuidados na primeira semana</h2>
        <ul>
          <li><strong>Alimentação:</strong> priorize alimentos pastosos e frios nas primeiras 48 horas, evitando mastigação intensa.</li>
          <li><strong>Compressas frias:</strong> ajudam a controlar o inchaço nas primeiras 24 a 48 horas, conforme orientação da equipe.</li>
          <li><strong>Higiene bucal:</strong> mantenha a escovação, com cuidado redobrado na região operada.</li>
          <li><strong>Evite esforço físico intenso</strong> nos primeiros dias, já que pode aumentar o inchaço.</li>
        </ul>

        <blockquote>O inchaço faz parte do processo normal de cicatrização — ele não indica que algo deu errado, apenas que o corpo está respondendo ao procedimento.</blockquote>

        <h2>Quando o resultado aparece</h2>
        <p>Como o inchaço inicial disfarça parte do efeito, é comum a ansiedade de "não estar vendo diferença" nos primeiros dias. O contorno definitivo do rosto costuma ficar evidente após 3 a 4 semanas, quando o edema baixa completamente.</p>

        <h2>Sinais que merecem atenção da equipe</h2>
        <p>Febre, dor que piora progressivamente ou sangramento fora do esperado não são normais e devem ser informados imediatamente à clínica que realizou o procedimento — por isso o acompanhamento pós-procedimento é parte do tratamento, não um extra.</p>

        <div class="cta-inline">
          <div><h4>Quer saber se a bichectomia é indicada para o seu rosto?</h4><p>A avaliação facial individual responde essa pergunta.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_harm}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "canal-dentario-doi-mitos-verdades.html",
        "title": "Canal (endodontia) dói? Mitos e verdades sobre o tratamento",
        "short_title": "Canal dói? Mitos e verdades",
        "description": "O tratamento de canal tem fama de ser doloroso, mas a técnica atual mudou completamente essa experiência. Veja mitos e verdades.",
        "category": "geral",
        "img": "clinica_ampla",
        "date": "2025-12-15",
        "read": 6,
        "excerpt": "\"Dói igual canal\" virou expressão popular — mas está desatualizada. Entenda por que o tratamento moderno de endodontia é bem mais tranquilo.",
        "faqs": [
            ("O tratamento de canal dói mais que uma obturação comum?", "Com anestesia adequada, o desconforto durante o procedimento é semelhante ao de outros tratamentos odontológicos comuns."),
            ("Quantas sessões são necessárias?", "Varia conforme a complexidade do caso — pode ser concluído em uma ou mais sessões, definido na avaliação."),
            ("O dente fica mais fraco depois do canal?", "O dente tratado pode ficar mais frágil estruturalmente, por isso muitas vezes é recomendada uma restauração ou coroa de proteção após o tratamento."),
        ],
        "body": '''
        <p>"Dói igual canal" é uma das expressões mais repetidas quando o assunto é dor — o problema é que ela está desatualizada há pelo menos duas décadas. A endodontia moderna transformou completamente essa experiência.</p>

        <h2>Por que o canal ficou com essa fama</h2>
        <p>A dor que as pessoas associam ao "canal" geralmente não é do tratamento em si, mas da <strong>inflamação ou infecção que motivou a necessidade do procedimento</strong> — uma polpa dentária inflamada dói muito, com ou sem tratamento. O papel do tratamento de canal é justamente remover essa fonte de dor.</p>

        <h2>Como funciona o tratamento de canal hoje</h2>
        <p>Com anestesia local eficaz e instrumentos modernos (muitas vezes rotatórios, com maior precisão), o dentista remove a polpa dentária inflamada ou infectada, limpa e desinfeta os canais internos da raiz e os veda com material específico. Durante o procedimento, o desconforto costuma ser comparável a uma restauração comum.</p>

        <h2>Mitos comuns sobre o canal</h2>
        <ul>
          <li><strong>"Canal sempre dói muito depois."</strong> Falso. Algum desconforto nas primeiras 24 a 48 horas é possível, mas costuma ser leve e controlado com analgésicos comuns.</li>
          <li><strong>"Fazer canal é sempre pior que arrancar o dente."</strong> Falso. Preservar o dente natural, sempre que possível, costuma trazer melhores resultados funcionais a longo prazo do que uma extração.</li>
          <li><strong>"Depois do canal, o dente está resolvido para sempre."</strong> Parcialmente falso. O dente tratado costuma precisar de uma restauração ou coroa de proteção, já que fica estruturalmente mais frágil.</li>
        </ul>

        <blockquote>A tecnologia reduziu bastante o desconforto do tratamento de canal — mas a percepção popular ainda não acompanhou essa mudança.</blockquote>

        <h2>Quando o canal é indicado</h2>
        <p>Sinais como dor espontânea, sensibilidade prolongada a temperaturas, escurecimento do dente ou inchaço na gengiva próxima podem indicar necessidade de avaliação endodôntica. Só um exame clínico (às vezes com radiografia) confirma o diagnóstico.</p>
        <p>Saiba mais sobre esse e outros cuidados na página de <a href="../tratamento-odontologia-geral.html">odontologia geral</a>.</p>

        <div class="cta-inline">
          <div><h4>Sentindo dor ou sensibilidade persistente?</h4><p>Não espere piorar — agende uma avaliação e tire a dúvida.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_geral}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "clareamento-dental-caseiro-ou-consultorio.html",
        "title": "Clareamento dental: caseiro, de consultório ou os dois?",
        "short_title": "Clareamento: caseiro ou de consultório?",
        "description": "Entenda a diferença entre clareamento a gel com moldeira e clareamento de consultório, e qual costuma trazer o melhor resultado.",
        "category": "geral",
        "img": "clinica_ampla",
        "date": "2025-11-30",
        "read": 5,
        "excerpt": "Os dois métodos usam o mesmo princípio ativo, mas em concentrações e tempos diferentes. Veja como escolher — ou combinar — as duas técnicas.",
        "faqs": [
            ("Clareamento dental estraga o esmalte?", "Quando feito com acompanhamento profissional e concentração adequada, o clareamento é considerado seguro para o esmalte dentário."),
            ("O resultado do clareamento é permanente?", "Não. Com o tempo e hábitos alimentares (café, vinho, cigarro), o dente tende a escurecer novamente, sendo comum repetir manutenções periódicas."),
            ("Posso clarear se tenho lentes de contato dental ou facetas?", "Materiais restauradores como porcelana e resina não respondem ao clareamento da mesma forma que o dente natural — por isso o planejamento deve ser feito antes de qualquer trabalho estético."),
        ],
        "body": '''
        <p>Clareamento a laser, caseiro, de farmácia, de consultório — a quantidade de termos por aí confunde mais do que ajuda. Na prática, os protocolos com acompanhamento profissional se resumem a dois grandes grupos, que inclusive podem ser combinados.</p>

        <h2>Clareamento caseiro supervisionado (com moldeira)</h2>
        <p>Feito com uma moldeira personalizada, confeccionada a partir da arcada do paciente, e um gel clareador de concentração mais baixa, indicado para uso em casa por um período determinado pelo dentista — geralmente algumas horas por dia, ao longo de 1 a 3 semanas.</p>
        <p><strong>Vantagens:</strong> resultado gradual, menor sensibilidade e mais controle do paciente sobre o processo.</p>

        <h2>Clareamento de consultório</h2>
        <p>Utiliza um gel de concentração mais alta, aplicado pelo dentista, geralmente ativado por luz especial, em uma ou poucas sessões no consultório.</p>
        <p><strong>Vantagens:</strong> resultado mais rápido, ideal para quem tem um compromisso ou evento em data próxima.</p>

        <h2>Qual é "melhor"?</h2>
        <p>Nenhum dos dois é universalmente superior — a diferença está na velocidade do resultado e na rotina de cada paciente. Muitos protocolos, inclusive, combinam as duas técnicas: uma sessão inicial em consultório seguida de manutenção caseira, otimizando resultado e conforto.</p>

        <blockquote>O fator mais importante não é o método, mas o acompanhamento profissional — concentração inadequada ou tempo de uso incorreto podem causar sensibilidade desnecessária.</blockquote>

        <h2>Sensibilidade: o que é normal</h2>
        <p>É comum sentir os dentes um pouco mais sensíveis a temperaturas durante o período de clareamento. Isso costuma ser temporário e é minimizado com produtos dessensibilizantes indicados pelo dentista.</p>

        <h2>O clareamento funciona em qualquer dente?</h2>
        <p>Não em restaurações, lentes de contato dental ou facetas — esses materiais não reagem ao clareamento como o esmalte natural. Por isso, se você já tem ou planeja fazer algum trabalho estético, o ideal é conversar sobre a ordem dos procedimentos na avaliação. Veja mais em <a href="../tratamento-odontologia-geral.html">odontologia geral</a>.</p>

        <div class="cta-inline">
          <div><h4>Quer saber qual técnica de clareamento é indicada para você?</h4><p>Agende uma avaliação e receba orientação personalizada.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_geral}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "quando-trocar-revisar-implante-dentario.html",
        "title": "Quando é hora de revisar ou trocar um implante dentário",
        "short_title": "Quando revisar ou trocar um implante",
        "description": "Implantes dentários têm garantia vitalícia com os devidos cuidados, mas sinais de alerta merecem avaliação rápida. Veja quais são.",
        "category": "implantes",
        "img": "raiox",
        "date": "2026-03-18",
        "read": 5,
        "excerpt": "Sangramento ao redor do implante, mobilidade ou desconforto ao mastigar são sinais que pedem avaliação — mesmo anos depois da cirurgia.",
        "faqs": [
            ("Implante dentário pode falhar depois de anos de uso?", "É raro, mas pode acontecer, geralmente associado à falta de manutenção, higiene inadequada ou doenças sistêmicas não controladas."),
            ("Toda dor perto do implante significa problema?", "Nem sempre, mas qualquer desconforto persistente na região deve ser avaliado — o diagnóstico precoce evita complicações maiores."),
            ("A garantia vitalícia cobre qualquer situação?", "A garantia se aplica ao implante em si quando os cuidados e retornos recomendados são seguidos — os detalhes são explicados na consulta de indicação."),
        ],
        "body": '''
        <p>Implante dentário bem indicado, bem instalado e bem cuidado tende a durar a vida toda — é justamente por isso que o Instituto Christian Andrade oferece garantia vitalícia nos implantes Grand Morse Neodent. Mas "durar a vida toda" não significa "nunca precisar de atenção".</p>

        <h2>Manutenção não é igual a problema</h2>
        <p>Assim como dentes naturais precisam de check-ups regulares, implantes também se beneficiam de acompanhamento periódico. Isso não significa que algo está errado — é justamente essa manutenção preventiva que sustenta a durabilidade do tratamento a longo prazo.</p>

        <h2>Sinais que merecem avaliação</h2>
        <ul>
          <li><strong>Sangramento ou inchaço na gengiva</strong> ao redor do implante, mesmo meses ou anos após a cirurgia.</li>
          <li><strong>Sensação de mobilidade</strong> na coroa protética ou no próprio implante.</li>
          <li><strong>Desconforto ao mastigar</strong> especificamente naquela região.</li>
          <li><strong>Mau hálito persistente</strong> localizado próximo ao implante.</li>
          <li><strong>Retração da gengiva</strong>, deixando parte do implante mais visível do que antes.</li>
        </ul>
        <p>Nenhum desses sinais significa, automaticamente, que o implante "falhou" — mas todos merecem avaliação para descartar (ou tratar cedo) uma condição chamada peri-implantite, uma inflamação ao redor do implante.</p>

        <blockquote>Diagnóstico precoce é a palavra-chave: quanto antes um sinal é avaliado, menor a chance de intervenções mais complexas.</blockquote>

        <h2>O que fazer para o implante durar a vida toda</h2>
        <ul>
          <li>Escovação e uso de fio dental (ou escova interdental) na região do implante, todos os dias;</li>
          <li>Retornos periódicos com o dentista, mesmo sem sintomas;</li>
          <li>Controle de condições sistêmicas que afetam a cicatrização óssea, como diabetes não controlado;</li>
          <li>Evitar hábitos como bruxismo não tratado, que sobrecarrega a estrutura do implante.</li>
        </ul>

        <h2>E se for necessário revisar?</h2>
        <p>Em alguns casos, o ajuste é simples — como uma nova adaptação da coroa protética. Em outros, pode envolver tratamento da gengiva ao redor do implante. O planejamento digital, o mesmo usado na <a href="../tratamento-implantes.html">cirurgia guiada</a>, também auxilia bastante nesse diagnóstico.</p>

        <div class="cta-inline">
          <div><h4>Notou algum sinal diferente no seu implante?</h4><p>Quanto antes avaliar, mais simples costuma ser a solução.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_implantes}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "primeira-consulta-odontologica-infantil.html",
        "title": "Primeira consulta odontológica infantil: quando levar seu filho",
        "short_title": "Primeira consulta odontológica infantil",
        "description": "Saiba a idade recomendada para a primeira visita ao dentista e como preparar a criança para uma experiência tranquila.",
        "category": "geral",
        "img": "clinica_azul",
        "date": "2025-10-05",
        "read": 5,
        "excerpt": "Levar a criança cedo ao dentista não é sobre tratar problemas — é sobre construir uma relação tranquila com o cuidado bucal desde o início.",
        "faqs": [
            ("Com quantos dentes devo levar meu filho ao dentista?", "A recomendação geral é levar após o nascimento dos primeiros dentinhos, geralmente por volta dos 6 a 12 meses de idade."),
            ("A criança pode ficar com medo do dentista?", "É comum. Consultas precoces e positivas, sem associação com dor, ajudam a construir uma relação tranquila com o cuidado bucal."),
            ("Dente de leite precisa mesmo de cuidado, já que vai cair?", "Sim — dentes de leite saudáveis são importantes para mastigação, fala e para guiar o posicionamento correto dos dentes permanentes."),
        ],
        "body": '''
        <p>Uma dúvida comum entre pais: "para que levar meu filho ao dentista se os dentes de leite vão cair mesmo?" A resposta tem menos a ver com tratar problemas e mais com <strong>construir hábito</strong> — tanto de higiene quanto de relação tranquila com o consultório.</p>

        <h2>Quando fazer a primeira consulta</h2>
        <p>A recomendação geral é que a primeira visita aconteça já nos primeiros meses após o nascimento dos primeiros dentinhos — geralmente entre 6 e 12 meses de idade. Parece cedo, mas o objetivo dessa consulta não é um "tratamento": é orientar os pais sobre higienização, amamentação, uso de mamadeira e hábitos como chupeta.</p>

        <h2>Por que dente de leite importa</h2>
        <ul>
          <li>Guia o posicionamento correto dos dentes permanentes que vão nascer depois;</li>
          <li>É essencial para mastigação adequada e desenvolvimento da fala;</li>
          <li>Cáries não tratadas em dentes de leite podem causar dor e infecção, afetando também o dente permanente correspondente.</li>
        </ul>

        <h2>Como tornar a experiência tranquila</h2>
        <ul>
          <li><strong>Evite palavras associadas a medo</strong> ("não vai doer", "não precisa ter medo") — elas, paradoxalmente, plantam a ideia do medo. Prefira uma linguagem neutra e positiva.</li>
          <li><strong>Não use o dentista como ameaça</strong> ("se não escovar o dente, vai ter que ir ao dentista").</li>
          <li><strong>Leve a criança em consultas de rotina</strong>, mesmo sem queixas, para que ela associe o consultório a algo comum, não a uma emergência.</li>
        </ul>

        <blockquote>Consultas de rotina, sem dor envolvida, são a melhor forma de evitar o "medo de dentista" na vida adulta.</blockquote>

        <h2>Com que frequência retornar</h2>
        <p>Assim como para adultos, o retorno a cada 6 meses costuma ser indicado, mas a frequência ideal é sempre definida pelo dentista, considerando o risco de cárie e os hábitos da criança.</p>
        <p>A odontologia geral cuida de toda a família — veja mais sobre prevenção em <a href="../tratamento-odontologia-geral.html">odontologia geral</a>.</p>

        <div class="cta-inline">
          <div><h4>Ainda não levou seu filho à primeira consulta?</h4><p>Agende um horário tranquilo para conhecer nossa equipe.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_geral}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
    {
        "slug": "preenchimento-labial-natural.html",
        "title": "Preenchimento labial natural: como evitar o exagero",
        "short_title": "Preenchimento labial natural",
        "description": "Preenchimento labial bem feito é sobre proporção, não volume máximo. Veja como funciona o planejamento para um resultado natural.",
        "category": "harmonizacao",
        "img": "clinica_vista",
        "date": "2026-02-01",
        "read": 5,
        "excerpt": "O medo do \"efeito boca de pato\" afasta muita gente do preenchimento labial. Entenda como a técnica correta evita esse resultado.",
        "faqs": [
            ("Preenchimento labial sempre fica artificial?", "Não — o resultado artificial geralmente vem de volume excessivo ou técnica inadequada, não do procedimento em si."),
            ("Quanto tempo dura o preenchimento labial?", "Em média de 6 a 12 meses, variando conforme o produto utilizado e o metabolismo de cada pessoa."),
            ("É possível reverter se eu não gostar do resultado?", "O ácido hialurônico pode ser dissolvido com uma enzima específica em caso de necessidade, o que traz mais segurança ao procedimento."),
        ],
        "body": '''
        <p>O maior medo de quem considera fazer preenchimento labial não é o procedimento em si — é parecer que fez. O tão temido "efeito boca de pato" é, quase sempre, resultado de volume desproporcional ao rosto, não uma consequência inevitável da técnica.</p>

        <h2>O objetivo real do preenchimento labial</h2>
        <p>Um preenchimento bem planejado busca <strong>proporção</strong>: hidratação, contorno definido e simetria entre lábio superior e inferior — não necessariamente "lábios maiores". Em muitos casos, pequenas quantidades de ácido hialurônico já produzem uma mudança perceptível e natural.</p>

        <h2>Como funciona a avaliação</h2>
        <p>Antes de qualquer aplicação, o profissional avalia a proporção entre nariz, boca e queixo, além da anatomia natural do seu lábio — cor, formato, assimetrias pré-existentes. Esse diagnóstico é o que define a quantidade de produto e a técnica de aplicação, evitando o excesso.</p>

        <h2>Por que alguns resultados ficam exagerados</h2>
        <ul>
          <li><strong>Volume acima do que a estrutura facial comporta;</strong></li>
          <li><strong>Aplicações repetidas sem tempo de reabsorção</strong> entre uma sessão e outra, acumulando produto;</li>
          <li><strong>Falta de avaliação individualizada</strong>, aplicando a mesma quantidade "padrão" em todos os pacientes.</li>
        </ul>

        <blockquote>Um bom resultado de preenchimento labial é aquele que os outros notam sem saber apontar exatamente o que mudou.</blockquote>

        <h2>Recuperação e cuidados</h2>
        <p>É comum um pequeno inchaço nas primeiras 24 a 48 horas após a aplicação — parte do resultado final só é percebida depois que esse inchaço inicial baixa completamente, geralmente após alguns dias.</p>

        <h2>Faz parte da harmonização orofacial</h2>
        <p>O preenchimento labial é um dos procedimentos de <a href="../tratamento-harmonizacao-orofacial.html">harmonização orofacial</a> mais procurados, muitas vezes combinado com outras técnicas dentro de um planejamento facial mais amplo.</p>

        <div class="cta-inline">
          <div><h4>Quer um resultado natural, sob medida para o seu rosto?</h4><p>Agende uma avaliação facial individual.</p></div>
          <a class="btn btn-gold js-wa-picker" href="{wa_harm}" target="_blank" rel="noopener">Agendar avaliação</a>
        </div>

        <h2>Perguntas frequentes</h2>
        <div class="faq">{faq_html}</div>
        ''',
    },
]


def blog_posting_ld(p):
    return jsonld({
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p["title"],
        "description": p["description"],
        "image": img(p["img"], 1200, 630),
        "datePublished": p["date"],
        "dateModified": p["date"],
        "author": {"@type": "Organization", "name": AUTHOR},
        "publisher": {"@type": "Organization", "name": "Instituto Christian Andrade",
                       "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/favicon.svg"}},
        "mainEntityOfPage": {"@type": "WebPage", "id": f"{BASE_URL}/blog/{p['slug']}"},
        "articleSection": CATEGORIES[p["category"]].replace("&amp;", "&"),
    })


def related_posts_html(current):
    others = [p for p in POSTS if p["slug"] != current["slug"] and p["category"] == current["category"]]
    if len(others) < 3:
        others += [p for p in POSTS if p["slug"] != current["slug"] and p not in others]
    others = others[:3]
    cards = "\n".join(f'''      <a class="post-card" href="{p['slug']}" data-reveal>
        <div class="thumb"><img src="{img(p['img'], 700, 460)}" alt="{p['title']}" width="700" height="460" loading="lazy"></div>
        <div class="body">
          <span class="cat">{CATEGORIES[p['category']]}</span>
          <h3>{p['title']}</h3>
          <span class="rm">Ler artigo</span>
        </div>
      </a>''' for p in others)
    return f'''  <section class="section on-mist">
    <div class="wrap">
      <div class="section-head" data-reveal><div><p class="eyebrow">Continue lendo</p><h2>Artigos relacionados</h2></div></div>
      <div class="related-grid">
{cards}
      </div>
    </div>
  </section>'''


def build_article(p):
    faq_html = faq_block(p["faqs"]) if p.get("faqs") else ""
    wa_links = {
        "wa_implantes": WA_DEFAULT,
        "wa_harm": WA_DEFAULT,
        "wa_facetas": WA_DEFAULT,
        "wa_ortho": WA_DEFAULT,
        "wa_geral": WA_DEFAULT,
    }
    prose = p["body"].format(faq_html=faq_html, **wa_links)

    body = f'''  <section class="article-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Blog</a> / {p['title']}</p>
      <span class="tag-pill" style="display:inline-block; margin-bottom:1em;">{CATEGORIES[p['category']]}</span>
      <h1 data-reveal>{p['title']}</h1>
      <p class="lede" data-reveal>{p['description']}</p>
      <div class="article-meta">
        <div class="author"><span class="ava">C</span> {AUTHOR}</div>
        <span>{p['date'][8:10]}/{p['date'][5:7]}/{p['date'][0:4]}</span>
        <span>{p['read']} min de leitura</span>
      </div>
      <div class="article-cover" data-reveal="scale">
        <img src="{img(p['img'], 1400, 600)}" alt="{p['title']}" width="1400" height="600" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="prose" data-reveal>
{prose}
      </div>
    </div>
  </section>

{related_posts_html(p)}

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Pronto para agendar sua avaliação?</h2>
      <p>Nossa equipe multidisciplinar cuida de cada etapa, do diagnóstico ao resultado.</p>
      <a class="btn btn-gold js-wa-picker" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    json_ld_list = [
        breadcrumb_ld([("Home", ""), ("Blog", "blog/index.html"), (p["title"], f"blog/{p['slug']}")]),
        blog_posting_ld(p),
    ]
    if p.get("faqs"):
        json_ld_list.append(faq_ld(p["faqs"]))

    seo_title = p.get("short_title", p["title"])
    page(
        f"blog/{p['slug']}",
        f"{seo_title} — Christian Andrade",
        p["description"],
        "blog", body, root="../",
        json_ld_list=json_ld_list,
        og_image=img(p["img"], 1200, 630),
        priority="0.6", changefreq="yearly",
    )


def build_blog_index():
    featured = POSTS[0]
    rest = POSTS[1:]

    pills = "\n        ".join(
        f'<button class="tag-pill{" active" if k == "todos" else ""}" data-filter="{k}">{v}</button>'
        for k, v in [("todos", "Todos")] + list(CATEGORIES.items())
    )

    cards = "\n".join(f'''      <a class="post-card" href="{p['slug']}" data-category="{p['category']}" data-reveal>
        <div class="thumb"><img src="{img(p['img'], 700, 460)}" alt="{p['title']}" width="700" height="460" loading="lazy"></div>
        <div class="body">
          <span class="cat">{CATEGORIES[p['category']]}</span>
          <h3>{p['title']}</h3>
          <p class="excerpt">{p['excerpt']}</p>
          <div class="meta"><span>{p['date'][8:10]}/{p['date'][5:7]}/{p['date'][0:4]}</span><span>{p['read']} min</span></div>
          <span class="rm">Ler artigo</span>
        </div>
      </a>''' for p in rest)

    body = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="../index.html">Home</a> / Blog</p>
      <p class="eyebrow">Conteúdo &amp; cuidado</p>
      <h1 data-reveal>Blog do Instituto Christian Andrade</h1>
      <p class="lede" data-reveal>Informação confiável sobre odontologia e harmonização orofacial, escrita para ajudar você a decidir com segurança.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <a class="post-feat" href="{featured['slug']}" data-reveal>
        <div>
          <span class="cat">{CATEGORIES[featured['category']]}</span>
          <h2 style="margin-top:.5em;">{featured['title']}</h2>
          <p class="lede" style="margin-top:.6em;">{featured['excerpt']}</p>
          <div class="meta" style="display:flex; gap:1em; font-size:.85rem; color:var(--ink-40); margin:1em 0 1.4em;"><span>{featured['date'][8:10]}/{featured['date'][5:7]}/{featured['date'][0:4]}</span><span>{featured['read']} min de leitura</span></div>
          <span class="btn-plain">Ler artigo completo</span>
        </div>
        <div class="thumb"><img src="{img(featured['img'], 900, 700)}" alt="{featured['title']}" width="900" height="700" loading="eager"></div>
      </a>

      <div class="tag-row" data-reveal>
        {pills}
      </div>

      <div class="blog-grid">
{cards}
      </div>
    </div>
  </section>

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Ainda com dúvidas sobre algum tratamento?</h2>
      <p>Fale com a nossa equipe e receba orientação personalizada.</p>
      <a class="btn btn-gold js-wa-picker" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    item_list = jsonld({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f"{BASE_URL}/blog/{p['slug']}", "name": p["title"]}
            for i, p in enumerate(POSTS)
        ],
    })

    page(
        "blog/index.html",
        "Blog — Instituto Christian Andrade",
        "Artigos sobre implantes, harmonização orofacial, ortodontia, facetas e saúde bucal, escritos pela equipe do Instituto Christian Andrade.",
        "blog", body, root="../",
        json_ld_list=[breadcrumb_ld([("Home", ""), ("Blog", "blog/index.html")]), item_list],
        og_image=img(featured["img"], 1200, 630),
        priority="0.9", changefreq="weekly",
    )


def build_all():
    build_blog_index()
    for p in POSTS:
        build_article(p)
