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

// Existing code remains the same, with the following additions:

function graphCreatePlot() {
    // Find the most recently added graph slot or the first empty slot
    const graphContainer = document.getElementById('graphContainer');

    let targetSlot =
        graphContainer.querySelector('.graph-slot:last-child');
    if (!targetSlot) {
        alert('Please add a graph slot first.');
        return;
    }
    // Get selected parameters
    const graphLocation =
        document.getElementById('graphLocation').value;
    const graphDatabase =
        document.getElementById('graphDatabase').value;
    const graphTable = document.getElementById('graphTable').value;
    const graphSensor = document.getElementById('graphSensor').value;
    const graphUnit = document.getElementById('graphUnit').value;
    const graphData = graphFetchData(graphLocation, graphDatabase,
        graphTable, graphSensor, graphUnit);
    
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
    
    // Create graph toolbar
    const graphToolbar = document.createElement('div');
    graphToolbar.className = 'graph-toolbar';
    graphToolbar.id = `graphEditToolbar-${graphDiv.id}`;
    graphToolbar.style.display = 'block';
    graphToolbar.innerHTML = `
        <button onclick="graphEditName('${graphDiv.id}')">Edit Graph Name</button>
        <button onclick="graphEditScaleAndUnit('${graphDiv.id}')">Edit Scale/Unit</button>
        <button onclick="graphEditType('${graphDiv.id}')">Edit Graph Type</button>
        <button onclick="graphLabelAxis('${graphDiv.id}')">Label Axis</button>
        <button onclick="graphDeletePlot('${graphDiv.id}')">Delete Graph</button>
    `;
    
    // Add close button and toolbar to the slot
    targetSlot.appendChild(closeButton);
    targetSlot.appendChild(graphToolbar);
}

// New function stubs for graph editing
function graphEditName(graphId) {
    const graphDiv = document.getElementById(graphId);
    const newName = prompt('Enter new graph name:', 'Graph Name');
    
    if (newName) {
        try {
            Plotly.relayout(graphDiv, {title: newName});
        } catch (error) {
            console.error('Error editing graph name:', error);
            alert('Failed to update graph name');
        }
    }
}

function graphEditScaleAndUnit(graphId) {
    const graphDiv = document.getElementById(graphId);
    
    // Prompt for X-axis details
    const xAxisMin = prompt('Enter X-axis minimum value:', '0');
    const xAxisMax = prompt('Enter X-axis maximum value:', '10');
    const xAxisUnit = prompt('Enter X-axis unit:', 'X Unit');
    
    // Prompt for Y-axis details
    const yAxisMin = prompt('Enter Y-axis minimum value:', '0');
    const yAxisMax = prompt('Enter Y-axis maximum value:', '10');
    const yAxisUnit = prompt('Enter Y-axis unit:', 'Y Unit');
    
    try {
        const updateLayout = {
            // X-axis configuration
            'xaxis.title': xAxisUnit,
            'xaxis.range': [
                parseFloat(xAxisMin), 
                parseFloat(xAxisMax)
            ],
            
            // Y-axis configuration
            'yaxis.title': yAxisUnit,
            'yaxis.range': [
                parseFloat(yAxisMin), 
                parseFloat(yAxisMax)
            ]
        };
        
        Plotly.relayout(graphDiv, updateLayout);
    } catch (error) {
        console.error('Error updating axis scales:', error);
        alert('Failed to update axis scales');
    }
}

function graphEditType(graphId) {
    const graphDiv = document.getElementById(graphId);
    
    // Create a modal for graph type selection
    const typeSelectionModal = document.createElement('div');
    typeSelectionModal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    `;
    
    typeSelectionModal.innerHTML = `
        <div style="background: white; padding: 20px; border-radius: 8px; width: 400px;">
            <h3>Select Graph Type</h3>
            <form id="graphTypeForm">
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">
                    <label style="display: flex; align-items: center;">
                        <input type="radio" name="graphType" value="scatter" style="margin-right: 5px;">
                        <span>Scatter Plot</span>
                    </label>
                    <label style="display: flex; align-items: center;">
                        <input type="radio" name="graphType" value="line" style="margin-right: 5px;">
                        <span>Line Chart</span>
                    </label>
                    <label style="display: flex; align-items: center;">
                        <input type="radio" name="graphType" value="bar" style="margin-right: 5px;">
                        <span>Bar Chart</span>
                    </label>
                    <label style="display: flex; align-items: center;">
                        <input type="radio" name="graphType" value="pie" style="margin-right: 5px;">
                        <span>Pie Chart</span>
                    </label>
                    <label style="display: flex; align-items: center;">
                        <input type="radio" name="graphType" value="histogram" style="margin-right: 5px;">
                        <span>Histogram</span>
                    </label>
                    <label style="display: flex; align-items: center;">
                        <input type="radio" name="graphType" value="box" style="margin-right: 5px;">
                        <span>Box Plot</span>
                    </label>
                </div>
                <div style="margin-top: 15px; display: flex; justify-content: space-between;">
                    <button type="button" id="confirmGraphType" style="padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px;">Confirm</button>
                    <button type="button" id="cancelGraphType" style="padding: 8px 15px; background-color: #6c757d; color: white; border: none; border-radius: 4px;">Cancel</button>
                </div>
            </form>
        </div>
    `;
    
    // Add modal to body
    document.body.appendChild(typeSelectionModal);
    
    // Get form elements
    const form = typeSelectionModal.querySelector('#graphTypeForm');
    const confirmButton = typeSelectionModal.querySelector('#confirmGraphType');
    const cancelButton = typeSelectionModal.querySelector('#cancelGraphType');
    
    // Confirm button handler
    confirmButton.addEventListener('click', () => {
        const selectedType = form.querySelector('input[name="graphType"]:checked');
        
        if (selectedType) {
            const typeChoice = selectedType.value;
            
            try {
                // Get current graph data
                const graphContext = Plotly.getPlotContext(graphDiv);
                const currentData = graphContext.data[0];
                
                // Prepare new trace based on type
                let newTrace;
                switch(typeChoice) {
                    case 'scatter':
                        newTrace = {
                            x: currentData.x,
                            y: currentData.y,
                            type: 'scatter',
                            mode: 'lines+markers'
                        };
                        break;
                    case 'line':
                        newTrace = {
                            x: currentData.x,
                            y: currentData.y,
                            type: 'scatter',
                            mode: 'lines'
                        };
                        break;
                    case 'bar':
                        newTrace = {
                            x: currentData.x,
                            y: currentData.y,
                            type: 'bar'
                        };
                        break;
                    case 'pie':
                        newTrace = {
                            labels: currentData.x,
                            values: currentData.y,
                            type: 'pie'
                        };
                        break;
                    case 'histogram':
                        newTrace = {
                            x: currentData.y,
                            type: 'histogram'
                        };
                        break;
                    case 'box':
                        newTrace = {
                            y: currentData.y,
                            type: 'box'
                        };
                        break;
                }
                
                // Completely redraw the plot with new trace
                Plotly.newPlot(graphDiv, [newTrace], graphContext.layout);
            } catch (error) {
                console.error('Error changing graph type:', error);
                alert('Failed to change graph type');
            }
            
            // Remove modal
            document.body.removeChild(typeSelectionModal);
        } else {
            alert('Please select a graph type');
        }
    });
    
    // Cancel button handler
    cancelButton.addEventListener('click', () => {
        document.body.removeChild(typeSelectionModal);
    });
}
function graphLabelAxis(graphId) {
    const graphDiv = document.getElementById(graphId);
    const xAxisLabel = prompt('Enter X-axis label:', 'X Axis');
    const yAxisLabel = prompt('Enter Y-axis label:', 'Y Axis');
    
    try {
        const updateLayout = {};
        
        if (xAxisLabel) updateLayout['xaxis.title'] = xAxisLabel;
        if (yAxisLabel) updateLayout['yaxis.title'] = yAxisLabel;
        
        Plotly.relayout(graphDiv, updateLayout);
    } catch (error) {
        console.error('Error labeling axes:', error);
        alert('Failed to update axis labels');
    }
}

function graphDeletePlot(graphId) {
    const graphDiv = document.getElementById(graphId);
    const graphSlot = graphDiv.closest('.graph-slot');
    
    // Remove the entire graph slot
    removeGraphSlot(graphSlot.id);
}