function verificarResposta(event) {

    event.preventDefault();

    const resposta = document.querySelector(
        'input[name="resposta"]:checked'
    );

    const resultado = document.getElementById("resultado");

    if (resposta.value === "certa") {

        resultado.innerHTML = `
            <div class="correct">
                ✓ Resposta correta!
                <br>
                Sempre confirme a cobrança
                por um canal oficial antes de pagar.
            </div>
        `;

    } else {

        resultado.innerHTML = `
            <div class="incorrect">
                ⚠️ Atenção!
                <br>
                O mais seguro é verificar a cobrança
                diretamente em um canal oficial.
            </div>
        `;
    }
}