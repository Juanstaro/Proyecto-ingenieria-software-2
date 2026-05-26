fetch('http://localhost:8000/airports/plotly/data')
.then(response => response.json())
.then(data => {

    const trace = {
        type: 'scattergeo',
        mode: 'markers',
        lat: data.latitudes,
        lon: data.longitudes,
        text: data.names,
        marker: {
            size: 8
        }
    }

    const layout = {
        title: 'Aeropuertos de Colombia',
        geo: {
            scope: 'south america'
        }
    }

    Plotly.newPlot('map', [trace], layout)
})
