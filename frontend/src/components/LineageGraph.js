import React, { useEffect, useState } from 'react';
import mermaid from 'mermaid';

const LineageGraph = ({ graphDefinition }) => {
    const [graph, setGraph] = useState('');

    useEffect(() => {
        if (graphDefinition) {
            setGraph(graphDefinition);
            mermaid.initialize({ startOnLoad: true });
            mermaid.contentLoaded(); // Re-render mermaid when graphDefinition changes
        }
    }, [graphDefinition]);

    return (
        <div className="lineage-graph">
            <div className="mermaid">
                {graph}
            </div>
        </div>
    );
};

export default LineageGraph;