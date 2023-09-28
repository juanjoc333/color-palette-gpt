const form = document.getElementById('form')
const container = document.querySelector('.container')

async function fetchColorPaletteColors(query) {
    return fetch('/palette', {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({
            query
        })
    })
}

const generateColorPalette = async (e) => {
    e.preventDefault();

    const query = form.elements.query.value

    const response = await fetchColorPaletteColors(query);

    const {colors} = await response.json()

    container.innerHTML = ''

    for (const color of colors) {
        const div = document.createElement('div')
        div.className = 'color'
        div.style.background = color
        container.appendChild(div)

        const span = document.createElement('span')
        span.innerText = color

        div.appendChild(span)

        div.addEventListener('click', () => {
            navigator.clipboard.writeText(color)
        })
    }
}

form.addEventListener('submit', generateColorPalette)
