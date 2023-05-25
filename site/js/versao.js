const divVersao = document.getElementById('div_versao')

const versoes = [
    ['1.3.1', '25/05/2023', 'Correções de BUGS no método add()'],
    ['1.3.0', '24/05/2023', 'Adicionado as funções utilDays, getUtilDay'],
    ['1.2.0', '22/05/2023', 'Adicionado as funções lastDay, lastDate'],
    ['1.1.0', '21/05/2023', 'Adicionado as funções add, datediff'],
    ['1.0.0', '20/05/2023', 'Lançamento da Biblioteca, sendo adicionado o Objeto RelativeDate e as funções addDay, addMonth e addYear'],
]

versoes.forEach( e => {
    console.log(e)
    divVersao.innerHTML += `
    <div class="col-12">
        <h5>Versão: ${e[0]}</h5>
        <h6>${e[1]}</h6> <br>
        <p>
        ${e[2]}
        </p>
        <a href="https://pypi.org/project/relativedate/${e[0]}/" class="btn btn-dark" target="_blank">Link Versão ${e[0]}</a>
        <hr>
    </div>
    `
})