
fetch("/dados")
    .then(response => response.json())
    .then(json => {

        dados = json;

        atualizarGrafico();

        const dadosTabela = calcularPureza(dados);

        console.log(dadosTabela);

        preencherTabela(dadosTabela);

    })
    .catch(error => console.error(error));


function obterClusters() {

    const texto = document
        .getElementById("kmeans-clusters")
        .value
        .trim();

    if (texto === "") {
        return [];
    }

    return texto
        .split("/")
        .map(Number)
        .filter(numero => !isNaN(numero));

}


function filtrarClusters(dados, clusters) {

    if (clusters.length === 0) {
        return dados;
    }

    return dados.filter(linha =>
        clusters.includes(Number(linha.cluster))
    );
}

function desenharGrafico(dadosGrafico) {

    Plotly.newPlot("kmeans-chart", [

        {

            x: dadosGrafico.map(d => d.PCA1),

            y: dadosGrafico.map(d => d.PCA2),

            z: dadosGrafico.map(d => d.PCA3),

            mode: "markers",

            type: "scatter3d",

            marker: {
                size: 4,
                color: dadosGrafico.map(d => d.cluster_kmeans),
                colorscale: "Viridis"
            }

        }

    ]);

}


function atualizarGrafico() {

    const clusters = obterClusters();

    const dadosFiltrados = filtrarClusters(dados, clusters);

    desenharGrafico(dadosFiltrados);

}


document
    .getElementById("kmeans-clusters")
    .addEventListener("input", atualizarGrafico);