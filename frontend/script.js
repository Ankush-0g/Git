const languageSelect = document.getElementById("languageSelect");

async function loadLanguages() {

    const response = await fetch("/languages");

    const languages = await response.json();

    for (const code in languages) {

        const option = document.createElement("option");

        option.value = code;
        option.textContent =
            `${languages[code]} (${code})`;

        languageSelect.appendChild(option);
    }
}

async function translateText() {

    const text =
        document.getElementById("inputText").value;

    const target =
        languageSelect.value;

    const response = await fetch(
        "/translate",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text,
                target
            })
        }
    );

    const data = await response.json();

    document.getElementById("outputText")
        .textContent = data.translated_text;
}

loadLanguages();
