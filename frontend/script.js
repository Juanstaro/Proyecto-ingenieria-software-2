async function loadAirports() {
    const response = await fetch(
        'http://localhost:8000/airports'
    )
    const airports = await response.json()

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

    Plotly.newPlot('map', [trace], layout)
}

async function loadItineraries() {
    const response = await fetch(
        'http://localhost:8001/itineraries'
    )
    const itineraries = await response.json()
    const container = document.getElementById(
        'itineraries-list'
    )
    container.innerHTML = ""

    itineraries.forEach(itinerary => {
        container.innerHTML += `
            <div class="itinerary">
                <h3>
                    ${itinerary.user_name}
                </h3>
                <p>
                    Salida: ${itinerary.departure_airport}
                </p>
                <p>
                    Llegada: ${itinerary.arrival_airport}
                </p>
                <p>
                    Fecha: ${itinerary.travel_date}
                </p>
                <p>
                    Duración: ${itinerary.duration_minutes} min
                </p>
                <button class="delete-btn"
                        onclick="deleteItinerary(${itinerary.id})">
                    Eliminar
                </button>
            </div>
        `
    })
}

// Nota: Esta función la dejamos igual ya que no se ejecuta en el top-level,
// sino mediante el atributo "onclick" del HTML.
async function deleteItinerary(id) {
    await fetch(
        `http://localhost:8001/itineraries/${id}`,
        {
            method: 'DELETE'
        }
    )
    loadItineraries()
}

document.getElementById(
    'itinerary-form'
).addEventListener(
    'submit',
    async function(e){
        e.preventDefault()

        const data = {
            user_name: document.getElementById(
                'user_name'
            ).value,
            departure_airport: parseInt(
                document.getElementById(
                    'departure_airport'
                ).value
            ),
            arrival_airport: parseInt(
                document.getElementById(
                    'arrival_airport'
                ).value
            ),
            travel_date: document.getElementById(
                'travel_date'
            ).value,
            duration_minutes: parseInt(
                document.getElementById(
                    'duration_minutes'
                ).value
            )
        }

        const response = await fetch(
            'http://localhost:8001/itineraries',
            {
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(data)
            }
        )

        if(response.ok){
            alert('Itinerario creado')
            loadItineraries()
            document.getElementById(
                'itinerary-form'
            ).reset()
        } else {
            const error = await response.json()
            alert(error.detail)
        }
    }
)

// --- LA SOLUCIÓN AQUÍ ---
// Ejecutamos ambas promesas en paralelo en la raíz del archivo usando Top-level await
try {
    await Promise.all([loadAirports(), loadItineraries()]);
} catch (error) {
    console.error("Error cargando los datos iniciales:", error);
}