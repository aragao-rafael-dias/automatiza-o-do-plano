from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

app = Flask(__name__)

# Rota para página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o form e gerar o PDF
@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    # Coletar dados do form
    nome_base = request.form.get('nome_base')
    dia = request.form.get('dia')
    local = request.form.get('local')
    horario = request.form.get('horario')
    direcao = request.form.get('direcao')
    codirecao = request.form.get('codirecao')
    objeto = request.form.get('objeto')
    hora1 = request.form.get('hora1')
    hora2 = request.form.get('hora2')
    hora3 = request.form.get('hora3')
    hora4 = request.form.get('hora4')
    hora5 = request.form.get('hora5')
    hora6 = request.form.get('hora6')
    hora7 = request.form.get('hora7')
    hora8 = request.form.get('hora8')

    # Verificação de preenchimento dos campos
    if not nome_base or not dia or not local or not horario or not direcao or not codirecao or not objeto:
        return "Erro: Todos os campos são obrigatórios.", 400

    # Nome do arquivo gerado
    data_hoje = datetime.now().strftime("%d-%m-%y")
    nome_arquivo = f"{nome_base}_{data_hoje}.pdf"
    
    # Limpar caracteres especiais no nome do arquivo
    nome_arquivo = nome_arquivo.replace(" ", "_").replace("!", "_")

    # Caminho absoluto para salvar o PDF no diretório 'static'
    caminho_pdf = os.path.join(os.getcwd(), "static", nome_arquivo)

    # Certificar-se de que a pasta "static" existe
    if not os.path.exists("static"):
        os.makedirs("static")  # Cria a pasta 'static' se não existir

    # Configurações do PDF
    pdf = SimpleDocTemplate(caminho_pdf, pagesize=A4)
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'Times-Roman'

    # Conteúdo do PDF
    story = []
    story.append(Paragraph(f'COLETIVO DE ARTES INTEGRADAS OPERÁRIOS PELA ARTE', styles['Normal']))
    story.append(Paragraph(f'PLANO DE ENCONTRO DIA {dia}', styles['Normal']))
    story.append(Paragraph(f'Local: {local}', styles['Normal']))
    story.append(Paragraph(f'Horário: {horario}', styles['Normal']))
    story.append(Paragraph(f'Direção: {direcao}', styles['Normal']))
    story.append(Paragraph(f'Codireção: {codirecao}', styles['Normal']))
    story.append(Paragraph(f'Objeto de Trabalho: {objeto}', styles['Normal']))
    story.append(Paragraph(f'DIVISÃO DE HORÁRIOS', styles['Normal']))

    # Tabela
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
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Aplicando o estilo à tabela
    table.setStyle(style)
    story.append(table)

    story.append(Paragraph(f'QUÓRUM: 8 membros', styles['Normal']))

    # Gerando o PDF
    pdf.build(story)

    # Verifica se o arquivo foi gerado antes de enviar
    if not os.path.exists(caminho_pdf):
        return f"Erro: O arquivo {nome_arquivo} não foi gerado!", 500

    # Enviar o arquivo gerado para o navegador
    return send_file(caminho_pdf, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
