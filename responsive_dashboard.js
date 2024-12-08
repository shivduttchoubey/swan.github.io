// Simulated data fetching function
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

let graphCounter = 0;

function addNewGraphSlot() {
    const graphContainer = document.getElementById('graphContainer');
    
    // Check if we already have 3 graphs in the row


    graphCounter++;
    const graphSlot = document.createElement('div');
    graphSlot.classList.add('graph-slot');
    graphSlot.id = `graphSlot${graphCounter}`;
    graphSlot.innerHTML = `
        <span>Graph Slot ${graphCounter} - Ready to configure</span>
        <button class="graph-slot-close" onclick="removeGraphSlot('${graphSlot.id}')">×</button>
    `;
    
    graphContainer.appendChild(graphSlot);
}

function removeGraphSlot(slotId) {
    const graphSlot = document.getElementById(slotId);
    graphSlot.remove();
}

function graphCreatePlot() {
    // Find the most recently added graph slot or the first empty slot
    const graphContainer = document.getElementById('graphContainer');
    let targetSlot = graphContainer.querySelector('.graph-slot:last-child');

    if (!targetSlot) {
        alert('Please add a graph slot first.');
        return;
    }

    // Get selected parameters
    const graphLocation = document.getElementById('graphLocation').value;
    const graphDatabase = document.getElementById('graphDatabase').value;
    const graphTable = document.getElementById('graphTable').value;
    const graphSensor = document.getElementById('graphSensor').value;
    const graphUnit = document.getElementById('graphUnit').value;

    const graphData = graphFetchData(graphLocation, graphDatabase, graphTable, graphSensor, graphUnit);

    // Create a unique div for Plotly graph
    const graphDiv = document.createElement('div');
    graphDiv.id = `graph-${Date.now()}`;
    graphDiv.style.width = '100%';
    graphDiv.style.height = '300px';
    
    // Clear the slot and add the graph div
    targetSlot.innerHTML = '';
    targetSlot.appendChild(graphDiv);

    // Create Plotly graph
    const graphTrace = {
        x: graphData.map(item => item.graph_x_value),
        y: graphData.map(item => item.graph_y_value),
        type: 'scatter',
        mode: 'lines+markers',
        name: `${graphSensor} - ${graphUnit}`
    };

    const graphLayout = {
        title: `${graphLocation} - ${graphDatabase}`,
        xaxis: { title: 'X Axis' },
        yaxis: { title: graphUnit }
    };

    Plotly.newPlot(graphDiv.id, [graphTrace], graphLayout);

    // Add a close button to the graph
    const closeButton = document.createElement('button');
    closeButton.classList.add('graph-slot-close');
    closeButton.innerHTML = '×';
    closeButton.onclick = () => removeGraphSlot(targetSlot.id);
    targetSlot.appendChild(closeButton);
}