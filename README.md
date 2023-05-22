<h1>Python Package: relativedate</h1>

<b>Descrição:</b>
<p>
    Biblioteca Python relacionada a datas, onde é criado um objeto "RelativeDate" que possui o atributo datetime, onde é retornado um objeto datetime.
</p>
<p>
    O objetivo desta biblioteca é facilitar a manipulação de datas relativas e calculos com datas, em sua primeira versão estamos trabalhando apenas com a data relativa baseado em mês, onde pode se passar o argumento de meses (positivo e negativo) e retornará a data relativa ao mês desejado
</p>

<hr>
<u><b>Links</b></u> <br>
<b>GitHub:</b> <a href="https://github.com/jmiante/relativedate/">https://github.com/jmiante/relativedate</a> <br>
<b>PyPI:</b> <a href="https://pypi.org/project/relativedate/">https://pypi.org/project/relativedate</a>

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
    rd = RelativeDate(year=2023, month=5, day=22)<br>
    <br>
    print(rd.get_relative_month(-9))<br><br>
</p>
<hr>
<p style="background: lightgray; color: black; padding: 20px;">
    <b>RETURN:</b><br>
    >> 2022-08-07 00:00:00
</p>
