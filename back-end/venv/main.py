from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# NOMEANADO O ARQUIVO ----------------------
nome_base = input('Nome do Arquivo (sem espaços)')
data_hoje = datetime.now().strftime("%d-%m-%y")

nome_arquivo = f"{nome_base}_{data_hoje}.pdf"

pdf = SimpleDocTemplate(f'./{nome_arquivo}', pagesize=A4)  # instacia da biblioteca

# ----------------------------------------------------

# VARIAVEIS DOS CAMPOS A SEREM PREENCHIDOS
dia = input('Data do Encontro ')
local = input('Local de Encontro ')
horario = input('Horário de Encontro ')
direcao = input('Diretor Geral ')
codirecao = input('Codireção ')
objeto = input('Objeto de Trabalho ')
hora1 = input('14h30 ')
hora2 = input('14h50 ')
hora3 = input('15h05 ')
hora4 = input('15h20 ')
hora5 = input('15h35 ')
hora6 = input('15h40 ')
hora7 = input('16h40 ')
hora8 = input('16h50 ')

# ----------------------------------------------------

# Adicionando textos com Paragraph
styles = getSampleStyleSheet()
# Alterando o estilo para usar Times New Roman
styles['Normal'].fontName = 'Times-Roman'

story = []

# Adicionando texto simples com a nova fonte
story.append(Paragraph(f'COLETIVO DE ARTES INTEGRADAS OPERÁRIOS PELA ARTE', styles['Normal']))
story.append(Paragraph(f'PLANO DE ENCONTRO DIA {dia}', styles['Normal']))
story.append(Paragraph(f'Local: {local}', styles['Normal']))
story.append(Paragraph(f'Horário: {horario}', styles['Normal']))
story.append(Paragraph(f'Direção: {direcao}', styles['Normal']))
story.append(Paragraph(f'Codireção: {codirecao}', styles['Normal']))
story.append(Paragraph(f'Objeto de Trabalho: {objeto}', styles['Normal']))
story.append(Paragraph(f'DIVISÃO DE HORÁRIOS', styles['Normal']))
story.append(Paragraph(f'QUÓRUM: 8 membros', styles['Normal']))
story.append(Paragraph(f'  ', styles['Normal']))

# ----------------------------------------------------

# TABELA
data = [
    ["HORÁRIO", "ATIVIDADE"],
    ["14h30", hora1],
    ["14h50", hora2],
    ["15h05", hora3],
    ["15h20", hora4],
    ["15h35", hora5],
    ["15h40", hora6],
    ["16h40", hora7],
    ["16h50", hora8]
]

table = Table(data, colWidths=[100, 300])
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cabeçalho com fundo cinza
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'),  # Mudando a fonte para Times-Roman
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

# Aplicando o estilo à tabela
table.setStyle(style)

# Adicionando a tabela à lista de elementos para o PDF
story.append(table)

# Gerando o PDF
pdf.build(story)
