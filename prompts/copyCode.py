"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file.uri]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1].uri]

def extract_pdf_pages(pathname: str) -> list[str]:
  parts = [f"--- START OF PDF ${pathname} ---"]
  # Add logic to read the PDF and return a list of pages here.
  pages = []
  for index, page in enumerate(pages):
    parts.append(f"--- PAGE {index} ---")
    parts.append(page)
  return parts

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document0.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document1.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document2.pdf")
  },
  {
    "role": "user",
    "parts": ["\nEste são dados de POCOS da Bacia BACIA DO ARARIPE\nEstes dados fazem parte deste contexto: \nCONTEXTOO Programa de Revitalização da Atividade de Exploração e Produção de Petróleo e Gás Natural em Áreas Terrestres –Reate, foi anunciado pelo MME em 27 de janeiro de 2017 em evento realizado na cidade de Salvador, com os objetivos estratégicos de: revitalizar as atividades de E&P em áreas terrestres no território nacional; estimular o desenvolvimento local e regional; e aumentar a competitividade da indústria petrolífera onshore nacional. O evento teve a participação, além do governo federal, de aproximadamente 200 representantes de empresas e associações da indústria, de produtores independentes de petróleo e gás natural, de secretarias estaduais de desenvolvimento e de meio ambiente, dentre outras.No ano de 2018, o Programa Reate registrou avanços em decorrência das ações constantes do Planejamento Estratégico do MME, quais sejam: - Implementação do sistema de Oferta Permanente de blocos exploratórios e campos marginais pela ANP. - Adequação dos percentuais de royalties de novos contratos aos ambientes de elevado risco exploratório e baixo potencial petrolífero, relativos às bacias maduras e de novas fronteiras. - Simplificação de exigências contratuais para jazidas de baixa materialidade, relativos à medição por exemplo. - Criação de coordenação de E&P terrestre na ANP para facilitar a comunicação e solução de problemas relativos à regulação. Além dos progressos acima destacados cabe mencionar as iniciativas da ANP para a retomada dos investimentos em E&P em áreas terrestres, e ainda em campos maduros em águas rasas. Tem-se ainda os projetos de desinvestimento de campos maduros da Petrobras, denominados por Ártico e Topázio, que podem, com sua conclusão, aumentar o número de operadores em terra.Motivados pelas conquistas no ambiente regulatório e político promovidas do REATE, desde 2017, e pelas transformações ocorridas no mercado em prol da competitividade e atração de novos agentes, o MME lançou a segunda versão do Programa chamado REATE 2020. OBJETIVOBusca avançar ainda mais na implantação de uma política nacional que fortaleça a atividade de E&P de petróleo e gás natural em áreas terrestres no Brasil, criando sinergias entre os produtores, fornecedores e financiadores dessa atividade para aumentar a exploração e produção competitiva de petróleo, e principalmente, gás natural em terra, visando uma indústria de E&P terrestre forte e competitiva, com produção crescente e com pluralidade de operadores e fornecedores de bens e serviços. OBJETIVOS ESTRATÉGICOSRevitalizar as atividades de E&P em áreas terrestres no território nacional;Fomentar o aproveitamento de recursos em reservatórios de baixa permeabilidade;Aumentar a competitividade da indústria petrolífera onshore nacional;Estimular o desenvolvimento local e regional. MISSÃODesenvolver e implantar uma Política Nacional que fortaleça a atividade de exploração e produção de petróleo e gás natural em áreas terrestres no Brasil. VISÃOUma indústria de E&P terrestre forte, competitiva, com produção crescente, pluralidade de operadores e diversidade de fornecedores de bens e serviços. PÚBLICO ALVOPartes interessadas e envolvidas na cadeia de criação de valor que engloba o segmento da indústria de E&P terrestre, e compreende as empresas concessionárias de E&P de petróleo e gás natural e as empresas fornecedoras de bens e serviços, as autoridades municipais e estaduais, academia, sociedade civil e associações patronais. METASPotencial de produção de óleo e gás em, pelo menos, 14 estados da Federação – Alagoas, Amazonas, Bahia, Ceará, Espírito Santo, Goiás, Maranhão, Mato Grosso, Mato Grosso do Sul, Minas Gerais, Piauí, Rio Grande do Norte, Santa Catarina e Sergipe;Meta de duplicação da produção, em 10 anos, com o gás crescendo em um ritmo maior que o do petróleo – a produção até 2030, no mínimo, dobrará, saindo do patamar de 270 mil barris diários de óleo equivalente, para 500 mil barris diários de óleo equivalente. Fruto da sinergia entre os programas “Reate 2020” e o “Novo Mercado de Gás”, sairemos de um nível de produção de gás natural em terra de 25 milhões de metros cúbicos por dia, para mais de 50 milhões;Geração de empregos – considerando a meta do “Reate” de produzir, até 2030, 500 mil barris de óleo equivalente (boe) por dia, estimamos a geração de centenas de milhares de empregos diretos, indiretos e por efeito renda. PILARESInovação e simplificação da regulação, para tornar a indústria permanentemente aberta aos avanços tecnológicos.Estímulo à criação e à atração de empresas de exploração e produção, e de prestadores de bens e serviços, incentivar o surgimento de empresas nacionais, incluindo os startups; e trazer investimentos estrangeiros.Viabilização da produção de gás onshore em larga escala, quer seja convencional ou não, em atendimento às diretrizes do novo mercado de gásPromoção da concorrência e da competitividade, especialmente, na comercialização do petróleo e gás produzidos. RESULTADOS ESPERADOSAumentar agilidade e eficácia do licenciamento ambiental;Aprimorar diretrizes energéticas e regulatórias;Viabilizar a produção de recursos em reservatório de baixa permeabilidade de forma sustentável;Aumentar o número de atores na E&P e em suas cadeias de valor e produtiva.\n\nMeu objetivo é permitir verificações dos dados anexados, como um especialista na indústria de petróleo e gás"]
  },
  {
    "role": "model",
    "parts": ["## Análise dos dados de poços da Bacia do Araripe - Poço 2AP 0001 CE\n\nCom base nos arquivos fornecidos (.txt e .pdf), podemos analisar as informações do poço 2AP 0001 CE da Bacia do Araripe, perfurado pela Petrobras, no contexto do Programa Reate.\n\n**Informações Gerais:**\n\n* **Localização:** Latitude -7.302308, Longitude -40.042413 (SAD-69), Município de Araripe, Ceará.\n* **Classificação:** Estratigráfico, Seco sem indicação de Hidrocarbonetos.\n* **Profundidade:** \n    * Total: 1524.0 m\n    * Perfuração: 1524.0 m\n    * Maior Profundidade Perfis: 1520.5 m\n* **Datas:**\n    * Início: 15/08/1986\n    * Término: 26/09/1986\n    * Última Reclassificação: 26/09/1986\n* **Formação no Fundo do Poço:** Embasa\n* **Revestimentos:**\n    * Superfície: 317.0 m (552.0 m) - 13 3/8\"\n    * Intermediário: 722.0 m (147.0 m) - 9 5/8\"\n\n**Perfis:**\n\nO poço possui uma variedade de perfis adquiridos, incluindo:\n\n* **ISF/ (Induction Spherically Focused Log):** Fornece informações sobre a resistividade da formação.\n* **MSFL/ (Micro-Spherically Focused Log):** Similar ao ISF, porém com maior resolução vertical.\n* **BHC/ (Borehole Compensated Sonic Log):** Mede a velocidade do som na formação, útil para identificar litologias e porosidade.\n* **GR (Gamma Ray Log):** Mede a radioatividade natural da formação, indicando a presença de argilas e folhelhos.\n* **LDL/ (Laterolog Deep Log):** Mede a resistividade da formação, com maior profundidade de investigação que o ISF.\n* **NGS/ (Neutron-Gamma Spectroscopy Log):** Mede a quantidade de hidrogênio na formação, útil para identificar fluidos e porosidade.\n* **CNL (Compensated Neutron Log):** Similar ao NGS, porém mais sensível à porosidade. \n* **EPT (Elemental Capture Spectroscopy Tool):** Mede a composição elementar da formação.\n* **SHDT (Sonic High-Resolution Dipole Tool):**  Mede a velocidade do som em alta resolução.\n* **WST (Wireline Formation Tester):**  Realiza testes de formação para determinar a pressão e as propriedades dos fluidos.\n* **CST(GR)/ (Conventional Sidewall Core):**  Amostras de rocha coletadas da parede do poço, juntamente com o perfil de raios gama. \n\n**Litologia:**\n\nO poço encontrou uma sequência de rochas sedimentares, com predominância de arenitos (52.33%), folhelhos (22.57%) e argilitos (18.01%). Também foram encontrados siltitos, calcarenitos, carvão e rochas ígneas em menor proporção. \n\n**Interpretação e Relevância para o Reate:**\n\nA ausência de hidrocarbonetos neste poço indica um desafio para o programa Reate na Bacia do Araripe. No entanto, a presença de arenitos com boa porosidade e permeabilidade pode ser um indicativo de reservatórios potenciais em outras áreas da bacia. A análise detalhada dos perfis, juntamente com dados sísmicos e geológicos regionais, é crucial para identificar áreas com maior potencial para exploração e produção de petróleo e gás natural.\n\n**Recomendações:**\n\n* **Integração de dados:** Combinar informações de perfis, sísmica, geologia e dados de poços próximos para uma melhor compreensão do sistema petrolífero da bacia.\n* **Estudos de reservatório:** Analisar as características dos arenitos encontrados, como porosidade, permeabilidade e saturação de fluidos, para avaliar seu potencial como reservatórios.\n* **Avaliação de plays exploratórios:** Identificar plays exploratórios com base na análise geológica e geofísica, para direcionar futuros esforços de exploração.\n\n**Conclusão:**\n\nApesar do poço 2AP 0001 CE ser classificado como seco, as informações obtidas a partir dos dados de perfis e litologia são valiosas para a compreensão do potencial da Bacia do Araripe no contexto do programa Reate. A integração de dados e estudos adicionais são necessários para direcionar os esforços de exploração para áreas com maior chance de sucesso na descoberta de hidrocarbonetos."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
for uploaded_file in uploaded_files:
  genai.delete_file(name=uploaded_file.name)