console.log("app.js carregado");


let dados = [];


// ==========================
// CARREGAR DADOS
// ==========================

fetch("/dados")
    .then(response => response.json())
    .then(json => {

        dados = json;

        console.log("Dados carregados:", dados);


        // ==========================
        // TABELAS
        // ==========================

        const tabelaKmeans = calcularPureza(
            dados,
            "kmeans"
        );

        console.log(
            "Tabela KMeans:",
            tabelaKmeans
        );


        preencherTabela(
            tabelaKmeans,
            "kmeans-table"
        );



        const tabelaDbscan = calcularPureza(
            dados,
            "dbscan"
        );


        console.log(
            "Tabela DBSCAN:",
            tabelaDbscan
        );


        preencherTabela(
            tabelaDbscan,
            "dbscan-table"
        );



        // ==========================
        // GRÁFICOS INICIAIS
        // ==========================

        atualizarGraficoKmeans();

        atualizarGraficoDbscan();


    })
    .catch(error =>
        console.error(
            "Erro:",
            error
        )
    );





// ==========================
// PEGAR CLUSTERS DIGITADOS
// ==========================

function obterClusters(id) {


    const texto = document
        .getElementById(id)
        .value
        .trim();



    if (texto === "") {

        return [];

    }



    return texto
        .split("/")
        .map(Number)
        .filter(
            numero => !isNaN(numero)
        );

}





// ==========================
// FILTRAR DADOS
// ==========================

function filtrarClusters(
    dados,
    clusters,
    colunaCluster
) {


    if (clusters.length === 0) {

        return dados;

    }



    return dados.filter(linha =>

        clusters.includes(
            Number(
                linha[colunaCluster]
            )
        )

    );

}





// ==========================
// DESENHAR GRÁFICO 3D
// ==========================

function desenharGrafico(
    elemento,
    dadosGrafico,
    colunaCluster
) {


    Plotly.newPlot(

        elemento,

        [

            {


                x: dadosGrafico.map(
                    d => Number(d.PCA1)
                ),


                y: dadosGrafico.map(
                    d => Number(d.PCA2)
                ),


                z: dadosGrafico.map(
                    d => Number(d.PCA3)
                ),



                mode: "markers",


                type: "scatter3d",



                marker: {


                    size: 4,


                    color: dadosGrafico.map(

                        d =>
                        Number(
                            d[colunaCluster]
                        )

                    ),



                    colorscale:
                        "Viridis"

                }



            }

        ],



        {

            margin: {

                l:0,
                r:0,
                b:0,
                t:0

            }

        }


    );

}





// ==========================
// ATUALIZAR KMEANS
// ==========================

function atualizarGraficoKmeans() {


    const clusters =
        obterClusters(
            "kmeans-clusters"
        );



    const dadosFiltrados =
        filtrarClusters(
            dados,
            clusters,
            "cluster_kmeans"
        );



    desenharGrafico(

        "kmeans-chart",

        dadosFiltrados,

        "cluster_kmeans"

    );

}





// ==========================
// ATUALIZAR DBSCAN
// ==========================

function atualizarGraficoDbscan() {


    const clusters =
        obterClusters(
            "dbscan-clusters"
        );



    const dadosFiltrados =
        filtrarClusters(
            dados,
            clusters,
            "cluster_dbscan"
        );



    desenharGrafico(

        "dbscan-chart",

        dadosFiltrados,

        "cluster_dbscan"

    );

}





// ==========================
// EVENTOS DOS INPUTS
// ==========================


document
    .getElementById(
        "kmeans-clusters"
    )
    .addEventListener(
        "input",
        atualizarGraficoKmeans
    );




document
    .getElementById(
        "dbscan-clusters"
    )
    .addEventListener(
        "input",
        atualizarGraficoDbscan
    );