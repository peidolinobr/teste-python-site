var url = window.location.href.split("/");
var link = url[0] + "//" + url[1] + url[2];
var botoes = document.getElementsByClassName('links');
var inicial = document.getElementById('inicial');
filtros=filtros;

console.log("a")

Array.from(botoes).forEach(function(botao, index) {
    
	botao.addEventListener('click', function(){
		//console.log(link+"/mapa/"+fotos[index+1].replace('.png', ''))
		window.location.href = link+"/filtro/"+filtros[index]//.replace('.png', '')
	})
});

inicial.addEventListener('click', function(){
    //console.log(link+"/mapa/"+fotos[index+1].replace('.png', ''))
    window.location.href = link
})