console.log("tabela.js carregado");

function calcularPureza(dados) {

    dados = converterDados(dados);

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

function preencherTabela(dadosTabela) {

    const tabela = document.getElementById("kmeans-table");

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

function converterDados(dados){

    return dados.map(linha => {

        return {
            ...linha,
            media_H: Number(linha.media_H),
            media_DD: Number(linha.media_DD),
            media_UD: Number(linha.media_UD),
            cluster: Number(linha.cluster)
        };

    });

}