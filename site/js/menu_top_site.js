const menu = document.getElementById('menu-top')
const home_link = 'https://jmiante.github.io/relativedate'

menu.innerHTML = `
<header class="masthead mb-auto">
        <div class="inner">
        <div class="bg-dark text-center">  
        <a class="navbar-brand text-white" href="${home_link}" >
          <img src="img/logo.png" alt="" class="img img-fluid" style="max-height: 100px;">
          RelativeDate
          </a>
        </div>
        <div class="shadow">  
          <nav class="nav nav-masthead justify-content-center">
          <a class="nav-link text-dark" href="${home_link}">Home</a>
          <a class="nav-link text-dark" href="documentacao.html">Documentação</a>
          <a class="nav-link text-dark" href="versoes.html">Versões</a>
          </nav>
          </div>
        </div>
      </header>
`
