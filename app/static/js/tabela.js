console.log("tabela.js carregado");


function calcularPureza(dados, tipoCluster) {

    dados = converterDados(
        dados,
        tipoCluster
    );

    const clusters = {};

    dados.forEach(linha => {

        const cluster = linha.cluster;

        if (!clusters[cluster]) {
            clusters[cluster] = [];
        }

        clusters[cluster].push(linha);

    });


    const resultado = [];


    for (const cluster in clusters) {

        const registros = clusters[cluster];

        const usuarios = {};


        registros.forEach(r => {

            if (!usuarios[r.subject]) {
                usuarios[r.subject] = 0;
            }

            usuarios[r.subject]++;

        });


        let dono = "";
        let maior = 0;


        for (const usuario in usuarios) {

            if (usuarios[usuario] > maior) {

                maior = usuarios[usuario];
                dono = usuario;

            }

        }


        const total = registros.length;
        const erros = total - maior;
        const pureza = (maior / total) * 100;


        resultado.push({

            cluster: Number(cluster),
            dono: dono,
            acertos: maior,
            erros: erros,
            total: total,
            pureza: pureza.toFixed(2)

        });

    }


    return resultado;

}



function preencherTabela(dadosTabela, tabelaId) {

    const tabela = document.getElementById(
        tabelaId
    );


    tabela.innerHTML = "";

    tabela.innerHTML += `
        <thead>
            <tr>
                <th>Cluster</th>
                <th>Dono</th>
                <th>Acertos</th>
                <th>Erros</th>
                <th>Total</th>
                <th>Pureza (%)</th>
            </tr>
        </thead>
        <tbody></tbody>
    `;


    const tbody = tabela.querySelector("tbody");


    dadosTabela.forEach(linha => {

        tbody.innerHTML += `
            <tr>
                <td>${linha.cluster}</td>
                <td>${linha.dono}</td>
                <td>${linha.acertos}</td>
                <td>${linha.erros}</td>
                <td>${linha.total}</td>
                <td>${linha.pureza}%</td>
            </tr>
        `;

    });

}



function converterDados(dados, tipoCluster){

    return dados.map(linha => {

        return {

            ...linha,

            subject: linha.subject,

            PCA1: Number(linha.PCA1),
            PCA2: Number(linha.PCA2),
            PCA3: Number(linha.PCA3),

            cluster:

                tipoCluster === "dbscan"
                ?
                Number(linha.cluster_dbscan)
                :
                Number(linha.cluster_kmeans)

        };

    });

}