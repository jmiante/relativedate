<h1>Python Package: relativedate</h1>

<b>Descrição:</b>
<p>
    Biblioteca Python relacionada a datas, onde é criado um objeto "RelativeDate" que possui o atributo datetime, onde é retornado um objeto datetime.
</p>
<p>
    O objetivo desta biblioteca é facilitar a manipulação de datas relativas e calculos com datas, em sua primeira versão estamos trabalhando apenas com a data relativa baseado em mês, onde pode se passar o argumento de meses (positivo e negativo) e retornará a data relativa ao mês desejado
</p>

<hr>
<b>Links</b> <br>
<b>Documentação:</b> <a href="https://jmiante.github.io/relativedate/" target="_blank">https://jmiante.github.io/relativedate</a> <br>
<b>GitHub:</b> <a href="https://github.com/jmiante/relativedate/" target="_blank">https://github.com/jmiante/relativedate</a> <br>
<b>PyPI (last version):</b> <a href="https://pypi.org/project/relativedate/" target="_blank">https://pypi.org/project/relativedate</a> <br>


<hr>
<b>Instalação:</b>
<p>pip install relativedate</p>
<hr>

<hr>
<b>Exemplo Utilização:</b>
    <p>
        from datetime import datetime <br>
        from relativedate import RelativeDate <br>
        <br>
        dt = datetime(year=2023, month=5, day=7)<br>
        rd = RelativeDate(dt)<br>
        print(rd)<br><br>
        rd.addMonth(-9)<br>
        <br>
        print(rd)<br><br>
    </p>
    <hr>
    <p style="background: lightgray; color: black; padding: 20px;">
        <b>RETURN:</b><br>
        >> 2023-05-07 00:00:00 <br>
        >> 2022-08-07 00:00:00
    </p>


<hr>
<hr>
<b>Doação:</b>
<p>Ajude o Projeto a continuar, qualquer doação é bem vinda</p>

<b>CHAVE PIX: </b> d51024a6-4320-4cb6-9241-b0a4d165dfd2 <br>
<b>PIX Copia e Cola: </b> <a href="00020126860014br.gov.bcb.pix0136d51024a6-4320-4cb6-9241-b0a4d165dfd20224Doacao para Projeto PiPY5204000053039865802BR5924Jonathas Henrique Miante6009Sao Paulo62100506Doacao630459B3"> Link </a> <br>
<b>QRCODE PIX: </b> <br> <img src="https://raw.githubusercontent.com/jmiante/relativedate/84840043692a8ddba11572b19379d7c9ad6381d2/site/img/pix.jpg" style="max-width: 300px;">
<hr>
<p><b>Nome: </b>Jonathas Henrique Miante - <b>Banco: </b>PicPay</p>

<hr>
<hr>

