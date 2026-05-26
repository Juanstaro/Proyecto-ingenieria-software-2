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
            },

            showland: true,
            landcolor: 'rgb(230,230,230)',

            showcountries: true,
            countrycolor: 'rgb(150,150,150)'
        }
    }

    Plotly.newPlot('map', [trace], layout)
})
.catch(error => console.error(error))