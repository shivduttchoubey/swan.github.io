 // Simulated data fetching function with prefix
 function graphFetchData(location, database, table, sensor, unit) {
    const graphData = [];
    for (let i = 0; i < 10; i++) {
        graphData.push({
            graph_x_value: i,
            graph_y_value: Math.random() * 10
        });
    }
    return graphData;
}

function graphCreatePlot() {
    const graphLocation = document.getElementById('graphLocation').value;
    const graphDatabase = document.getElementById('graphDatabase').value;
    const graphTable = document.getElementById('graphTable').value;
    const graphSensor = document.getElementById('graphSensor').value;
    const graphUnit = document.getElementById('graphUnit').value;

    const graphData = graphFetchData(graphLocation, graphDatabase, graphTable, graphSensor, graphUnit);

    const graphTrace = {
        x: graphData.map(item => item.graph_x_value),
        y: graphData.map(item => item.graph_y_value),
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Graph Y Values'
    };

    const graphLayout = {
        title: 'Generated Graph',
        xaxis: { title: 'X Axis' },
        yaxis: { title: 'Y Axis' }
    };

    Plotly.newPlot('graphMainContainer', [graphTrace], graphLayout);
    document.getElementById('graphEditToolbar').style.display = 'flex';
}

function graphEditName() {
    const graphNewName = prompt('Enter new graph name:');
    if (graphNewName) {
        const graphLayout = {
            title: graphNewName
        };
        Plotly.relayout('graphMainContainer', graphLayout);
    }
}

function graphEditScaleAndUnit() {
    const graphNewXLabel = prompt('Enter new X-axis unit:');
    const graphNewYLabel = prompt('Enter new Y-axis unit:');
    
    if (graphNewXLabel && graphNewYLabel) {
        const graphLayout = {
            xaxis: { title: graphNewXLabel },
            yaxis: { title: graphNewYLabel }
        };
        Plotly.relayout('graphMainContainer', graphLayout);
    }
}

function graphEditType() {
    const graphType = prompt('Enter graph type (scatter, bar):');
    
    if (graphType) {
        const graphData = graphFetchData(
            document.getElementById('graphLocation').value,
            document.getElementById('graphDatabase').value,
            document.getElementById('graphTable').value,
            document.getElementById('graphSensor').value,
            document.getElementById('graphUnit').value
        );

        const graphTrace = {
            x: graphData.map(item => item.graph_x_value),
            y: graphData.map(item => item.graph_y_value),
            type: graphType === 'bar' ? 'bar' : 'scatter',
            mode: graphType === 'bar' ? 'markers' : 'lines+markers',
            name: 'Graph Y Values'
        };

        Plotly.newPlot('graphMainContainer', [graphTrace]);
    }
}

function graphLabelAxis() {
    const graphNewXLabel = prompt('Enter new X-axis label:');
    const graphNewYLabel = prompt('Enter new Y-axis label:');
    
    if (graphNewXLabel && graphNewYLabel) {
        const graphLayout = {
            xaxis: { title: graphNewXLabel },
            yaxis: { title: graphNewYLabel }
        };
        Plotly.relayout('graphMainContainer', graphLayout);
    }
}

function graphDeletePlot() {
    document.getElementById('graphMainContainer').innerHTML = '';
    document.getElementById('graphEditToolbar').style.display = 'none';
}