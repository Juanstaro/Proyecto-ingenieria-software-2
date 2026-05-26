async function loadAirports() {

    try {

        const response = await fetch(
            'http://localhost:8000/airports'
        )

        const airports = await response.json()

        document.getElementById(
            "airport-count"
        ).innerText = airports.length

        // TABLA
        const table = document.getElementById(
            "airport-table"
        )

        airports.forEach(airport => {

            const row = `
                <tr>
                    <td>${airport.id}</td>
                    <td>${airport.name}</td>
                    <td>${airport.latitude}</td>
                    <td>${airport.longitude}</td>
                </tr>
            `

            table.innerHTML += row
        })

        // MAPA
        const trace = {

            type: 'scattergeo',

            mode: 'markers',

            lat: airports.map(a => a.latitude),

            lon: airports.map(a => a.longitude),

            text: airports.map(a => a.name),

            marker: {
                size: 8,
                color: '#2563eb'
            }
        }

        const layout = {

            title: 'Aeropuertos de Colombia',

            geo: {

                scope: 'south america',

                projection: {
                    type: 'mercator'
                },

                center: {
                    lat: 4.5709,
                    lon: -74.2973
                },

                lataxis: {
                    range: [-5, 15]
                },

                lonaxis: {
                    range: [-82, -66]
                }
            }
        }

        Plotly.newPlot(
            'map',
            [trace],
            layout
        )

    } catch(error) {

        console.error(error)
    }
}

loadAirports()